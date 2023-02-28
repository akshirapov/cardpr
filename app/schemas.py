from datetime import datetime as dt
from uuid import UUID

from pydantic import BaseConfig, BaseModel, validator


def convert_field_to_camel_case(string: str) -> str:
    return "".join(word if index == 0 else word.capitalize() for index, word in enumerate(string.split("_")))


class CardPRBase(BaseModel):
    class Config(BaseConfig):
        orm_mode = True
        allow_population_by_field_name = True
        alias_generator = convert_field_to_camel_case


class Customer(CardPRBase):
    name: str = ""
    surname: str = ""
    middlename: str = ""

    email: str = ""
    phone: str
    birthday: str | dt = ""

    card_numbers: list[str] = []
    card_tracks: list[dict[str, str]] = []

    extra: str | dict[str, str] = {}

    promo: str = ""
    refer_customer_phone: str = ""

    sum: int = 0
    transaction_id: str | UUID = ""

    discount: float = 0.00
    bonus: float = 0.00
    balance: float = 0.00

    link: str = ""
    form_url: str = ""

    @validator("birthday")
    def parse_birthdate(cls, value):
        if isinstance(value, str):
            return dt.strptime(value, "%d.%m.%Y")
        return value

    @validator("extra")
    def parse_extra(cls, value: dict):
        if isinstance(value, dict):
            r = []
            for k, v in value.items():
                r.append(f"{k}:{v}")
            return ";".join(r)
        return value


class Webhook(CardPRBase):
    crm_key: str | UUID = ""
    method: str
    customer: Customer


class AddBalanceResponse(CardPRBase):
    success: bool


class ReadBalanceResponse(CardPRBase):
    success: bool
    bonus: str = ""
    balance: str = ""
    discount: str = ""
