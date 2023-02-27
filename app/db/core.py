import re

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

from app.config import get_app_settings

settings = get_app_settings()

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def resolve_table_name(name: str) -> str:
    """Resolves table names to their mapped names."""
    names = re.split("(?=[A-Z])", name)  # noqa
    return "_".join([x.lower() for x in names if x])


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        return resolve_table_name(self.__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
