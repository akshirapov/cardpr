import uuid
from datetime import datetime

from sqlalchemy import (
    UUID,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.core import Base


class Customer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    guid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[str] = mapped_column(String(50))
    middlname: Mapped[str] = mapped_column(String(50))

    email: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(12), index=True)
    birthday: Mapped[datetime] = mapped_column(DateTime)

    discount: Mapped[float] = mapped_column(Numeric(5, 2))
    bonus: Mapped[float] = mapped_column(Numeric(5, 2))
    balance: Mapped[float] = mapped_column(Numeric(15, 2))
    promo: Mapped[str] = mapped_column(String(50))
    refer_customer_phone: Mapped[str] = mapped_column(String(12))

    cards: Mapped[list["Card"]] = relationship(back_populates="customer")

    link: Mapped[str] = mapped_column(Text)
    form_url: Mapped[str] = mapped_column(Text)

    extra: Mapped[str] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, name={self.name!r}, phone={self.phone!r})"


class Card(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    number: Mapped[int] = mapped_column(Integer)
    track: Mapped[int] = mapped_column(String(50))
    install: Mapped[bool] = mapped_column(Boolean)
    url: Mapped[str] = mapped_column(Text)
    gpay_url: Mapped[str] = mapped_column(Text)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped["Customer"] = relationship(back_populates="cards")

    def __repr__(self) -> str:
        return f"Card(id={self.id!r}, number={self.number!r}, customer_id={self.customer_id!r})"
