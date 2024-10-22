import platform
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    version: str = "1.0.2"
    ambient_log_level: str = "INFO"
    ambient_log_lines: int = 1000
    ambient_config: str = "~/.ambientctl/config.json"

    backend_api_url: str = "https://api.ambientlabs.io"
    event_bus_api: str = "https://events.ambientlabs.io"
    connection_service_url: str = "wss://sockets.ambientlabs.io"

    package_location: Path = Path(__file__).parent
    service_template_location: str = "./templates/ambient_edge_server.service.jinja2"
    platform: str = platform.system().lower()

    word_art_path: str = "./assets/word_art.txt"
    default_delay: int = 3


settings = Settings()
