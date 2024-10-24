import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AUTH_TOKEN: str = ""
    REGISTRY_URL: str = "ws://localhost:8080"
    NODE_MODE: str = "httpserver"
    HTTP_PORT: int = 8000
    AGENTIC_CONFIG_PATH: str = "src/agentic/agentic_config.py"
    HTTP_HEALTHCHECK : bool = False
    LOG_LEVEL: str = "INFO"

    
settings = Settings()

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
}

_env_level = settings.LOG_LEVEL
_log_level = logging.INFO
if _env_level not in _nameToLevel:
    print(f"Invalid log level: {_env_level}. Defaulting to INFO")
else:
    _log_level = _nameToLevel[_env_level]
print("Setting log level to: ", _log_level) 

logging.basicConfig(
    level=_log_level,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)