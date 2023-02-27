import uuid
from datetime import datetime

from sqlalchemy import UUID, Boolean, Column, DateTime, Integer, Numeric, String, Text

from app.db.core import Base


class Customer(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4, index=True)

    name = Column(String(255), default="", nullable=False)
    surname = Column(String(255), default="", nullable=False)
    middlename = Column(String(255), default="", nullable=False)

    email = Column(String(255), default="", nullable=False)
    phone = Column(String(10), unique=True, nullable=False, index=True)
    birthday = Column(DateTime, default=datetime.min, nullable=False)

    discount = Column(Numeric(5, 2), default=0, nullable=False)
    bonus = Column(Numeric(5, 2), default=0, nullable=False)
    balance = Column(Numeric(15, 2), default=0, nullable=False)

    promo = Column(String(50), default="", nullable=False)
    refer_customer_phone = Column(String(10), default="", nullable=False)

    link = Column(Text, default="", nullable=False)
    form_url = Column(Text, default="", nullable=False)

    # TODO: Add relations
    extra = Column(Text, default="", nullable=False)

    # TODO: Add relations
    # cards


class Card(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4, index=True)
    # TODO: Add relations
    # customer_id = Column(UUID, nullable=False)
    number = Column(Integer, default=0, nullable=False)
    track = Column(String(50), default="", nullable=False)
    install = Column(Boolean, default=False, nullable=False)
    url = Column(Text, default="", nullable=False)
    gpay_url = Column(Text, default="", nullable=False)


class Extra(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4, index=True)
    # TODO: Add relations
    # customer_id = Column(UUID, nullable=False)
    field = Column(String(255), default="", nullable=False)
    value = Column(String(255), default="", nullable=False)
