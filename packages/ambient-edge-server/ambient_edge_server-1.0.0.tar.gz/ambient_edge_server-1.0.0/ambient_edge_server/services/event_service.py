import asyncio
import fnmatch
import importlib
from abc import ABC, abstractmethod
from typing import Dict, Set, Tuple, Union

from ambient_backend_api_client import Configuration as APIConfiguration
from ambient_base_plugin import BasePlugin
from ambient_base_plugin.models.configuration import ConfigPayload, PluginDefinition
from ambient_event_bus_client import Client, Message, MessageCreate
from result import Err, Result

from ambient_client_common.repositories.docker_repo import DockerRepo
from ambient_client_common.repositories.node_repo import NodeRepo
from ambient_client_common.utils import logger
from ambient_edge_server.config import settings
from ambient_edge_server.repos.plugin_repo import PluginRepo


class EventService(ABC):
    @abstractmethod
    async def start(self) -> None:
        """Start the event service."""

    @abstractmethod
    async def stop(self) -> None:
        """Stop the event service."""

    @abstractmethod
    async def send_event(self, topic: str, msg: str) -> None:
        """Send an event to the event service.

        Args:
            event (Event): Event to send
        """

    @property
    @abstractmethod
    def is_running(self) -> bool:
        """Check if the event service is running.

        Returns:
            bool: True if the event service is running, False otherwise
        """

    @property
    @abstractmethod
    def error(self) -> Union[Result, None]:
        """Get the current error state of the event service.

        Returns:
            Result: The current error state
        """


class AmbientBusEventService(EventService):
    def __init__(
        self,
        client: Client,
        node_repo: NodeRepo,
        plugin_repo: PluginRepo,
        docker_repo: DockerRepo,
    ) -> None:
        self.client = client
        self.node_repo = node_repo
        self.plugin_repo = plugin_repo
        self.docker_repo = docker_repo
        self.tasks: Set[asyncio.Task] = set()
        self._error = None
        self._is_connected = False
        self.plugins: Dict[str, Tuple[BasePlugin, PluginDefinition]] = {}

    async def load_plugins(self, api_config: APIConfiguration) -> None:
        logger.info("Loading plugins ...")
        plugins = self.plugin_repo.load_plugins()
        logger.info("Loaded {} plugins.", len(plugins))

        # Register the dynamic hooks with the plugin manager
        logger.info("Registering hooks with pluggy ...")
        for plugin in plugins:
            await self.register_plugin(plugin, api_config)
        logger.info("Plugins loaded.")

    async def register_plugin(
        self, plugin_config: PluginDefinition, api_config: APIConfiguration
    ) -> None:
        """Register a plugin.

        Args:
            plugin_config (PluginDefinition): Plugin Definition
            api_config (APIConfiguration): API configuration
        """
        try:
            logger.debug("Registering plugin: {}", plugin_config.class_name)
            module = importlib.import_module(plugin_config.module)
            logger.debug("Imported module: {}", plugin_config.module)
            plugin_class = getattr(module, plugin_config.class_name)
            logger.debug("Got plugin class: {}", plugin_config.class_name)
            plugin_instance: BasePlugin = plugin_class()
            logger.info("Registered plugin: {}", plugin_config.class_name)
            config_payload = self.build_config_payload(plugin_config, api_config)
            logger.debug(
                "Config payload:\n{}", config_payload.model_dump_json(indent=4)
            )
            await plugin_instance.configure(config=config_payload, logger=logger)
            logger.info("Configured plugin: {}", plugin_config.class_name)

            self.plugins[plugin_config.name] = (plugin_instance, plugin_config)
            logger.info("Plugin registered: {}", plugin_config.class_name)
        except ImportError as e:
            logger.error("Could not import module {}: {}", plugin_config.module, e)
        except AttributeError as e:
            logger.error(
                "Attribute error registering plugin {}: {}", plugin_config.class_name, e
            )
            logger.debug(e.with_traceback(e.__traceback__))
        except Exception as e:
            logger.error("Error registering plugin {}: {}", plugin_config.class_name, e)

    def build_config_payload(
        self, plugin_definition: PluginDefinition, api_config: APIConfiguration
    ) -> ConfigPayload:
        logger.info("Building config payload for plugin: {}", plugin_definition.name)
        node_data = self.node_repo.get_node_data()
        config_payload = ConfigPayload(
            node_id=node_data.id,
            plugin_config=plugin_definition,
        )
        if plugin_definition.request_api_config:
            logger.info("Adding API configuration to payload ...")
            config_payload.api_config = api_config
        if plugin_definition.request_platform:
            logger.info("Adding platform to payload ...")
            config_payload.platform = settings.platform
        if plugin_definition.request_node_repo:
            logger.info("Adding node repo to payload ...")
            config_payload.node_repo = self.node_repo
        if plugin_definition.request_docker_repo:
            logger.info("Adding docker repo to payload ...")
            config_payload.docker_repo = self.docker_repo

        logger.debug("Config payload:\n{}", config_payload.model_dump_json(indent=4))
        return config_payload

    async def start(self, api_config: APIConfiguration) -> None:
        logger.info("Starting event service ...")
        await self.client.init_client()
        node = self.node_repo.get_node_data()
        if node:
            await self.client.add_subscription(f"node-{node.id}/*")
        logger.debug("event client initialized.")

        logger.info("Starting subscription loop ...")
        sub_loop_task = asyncio.create_task(self._subscription_loop())
        sub_loop_task.add_done_callback(self._done_callback)
        sub_loop_task.set_name("subscription_loop_task")
        self.tasks.add(sub_loop_task)
        logger.info("subscription loop started.")

        await self.load_plugins(api_config)

    async def stop(self) -> None:
        logger.info("Stopping event service ...")
        for task in self.tasks:
            logger.debug("cancelling task: {}", task.get_name())
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    async def send_event(self, topic: str, msg: str) -> None:
        message_data = MessageCreate(topic=topic, message=msg)
        logger.debug("Publishing message:\n{}", message_data.model_dump_json(indent=4))
        await self.client.publish(msg)

    @property
    def is_running(self) -> bool:
        return all((self._is_connected, not self._error))

    @property
    def error(self) -> Union[Err, None]:
        return self._error

    async def _handle_event(self, msg: Message) -> None:
        logger.debug(f"Handling event for topic: {msg.topic}")

        matched_plugins: Dict[str, Tuple[BasePlugin, PluginDefinition]] = {}
        for plugin_name, plugin in self.plugins.items():
            logger.debug(f"Checking hook: {plugin_name}")
            plugin_instance, plugin_definition = plugin
            for topic in plugin_definition.topics:
                if fnmatch.fnmatch(msg.topic, topic):
                    matched_plugins[plugin_name] = plugin
                    break

        if matched_plugins:
            logger.debug(
                f"Found matching hooks for topic {msg.topic}: {matched_plugins.keys()}"
            )
            for plugin_name, plugin in matched_plugins.items():
                plugin_instance, plugin_definition = plugin
                logger.debug(f"Handling event for plugin: {plugin_name}")
                await plugin_instance.handle_event(msg)
                logger.debug(f"Event handled for plugin: {plugin_name}")
        else:
            logger.warning(f"No matching hooks found for topic: {msg.topic}")

    async def _subscription_loop(self) -> None:
        logger.info("Starting subscription loop ...")
        while True:
            self._error = None
            self._is_connected = True
            try:
                async for message_result in self.client.subscribe():
                    if message_result.is_err():
                        self._error = message_result
                        logger.error(
                            "Error subscribing to messages: {}", message_result
                        )
                        break
                    message = message_result.unwrap()
                    logger.debug(
                        "Received message:\n{}", message.model_dump_json(indent=4)
                    )
                    await self._handle_event(message)
            except Exception as e:
                self._error = Err(e)

    async def _done_callback(self, task: asyncio.Task) -> None:
        err_msg = f"task {task.get_name()} ended. \
Result: {task.result() if task.done() else task.exception()}"
        logger.warning(err_msg)
        self._error = Err(err_msg)

        logger.debug("removing task from tasks set ...")
        self.tasks.remove(task)

        logger.info("restarting subscription loop ...")
        sub_loop_task = asyncio.create_task(self._subscription_loop())
        sub_loop_task.add_done_callback(self._done_callback)
        sub_loop_task.set_name("subscription_loop_task")
        self.tasks.add(sub_loop_task)
        logger.info("subscription loop restarted.")
