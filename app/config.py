from functools import lru_cache
from typing import Any, Dict

from pydantic import BaseSettings, PostgresDsn, SecretStr


class AppSettings(BaseSettings):
    debug: bool = False
    title: str = "CardPR API"
    version: str = "0.1.0"
    secret_key: SecretStr
    database_url: PostgresDsn

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {"debug": self.debug, "title": self.title, "version": self.version}

    class Config:
        env_file = ".env"


@lru_cache
def get_app_settings() -> AppSettings:
    """Returns a cached instance of the AppSettings object."""
    return AppSettings()
