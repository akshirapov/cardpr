import re

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

from app.config import get_app_settings

settings = get_app_settings()

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def resolve_table_name(name: str) -> str:
    """Resolves table names to their mapped names."""
    names = re.split("(?=[A-Z])", name)  # noqa
    return "_".join([x.lower() for x in names if x])


class CustomBase:
    @declared_attr  # type: ignore
    def __tablename__(self) -> str:
        return resolve_table_name(self.__name__)  # type: ignore

    def dict(self):
        """Returns a dict representation of a model."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}  # type: ignore


Base = declarative_base(cls=CustomBase)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
