from fastapi import FastAPI

from app.routes import router
from app.config import get_app_settings


def get_application() -> FastAPI:
    settings = get_app_settings()
    application = FastAPI(**settings.fastapi_kwargs)
    application.include_router(router)
    return application


app = get_application()
