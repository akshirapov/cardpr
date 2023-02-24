from functools import lru_cache
from typing import Any, Dict

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = False
    title: str = "CardPR API"
    version: str = "0.1.0"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {"debug": self.debug, "title": self.title, "version": self.version}


@lru_cache
def get_app_settings() -> AppSettings:
    """Returns a cached instance of the AppSettings object."""
    return AppSettings()
