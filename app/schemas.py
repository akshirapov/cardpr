from uuid import UUID

from pydantic import BaseConfig, BaseModel


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
    birthday: str = ""
    card_numbers: list[str] = []
    card_tracks: list[dict[str, str]] = []
    extra: dict[str, str] = {}
    promo: str = ""
    refer_customer_phone: str = ""
    sum: int = 0
    transaction_id: str | UUID = ""


class AddBalance(CardPRBase):
    crm_key: str | UUID = ""
    method: str
    customer: Customer


class CreateCustomer(CardPRBase):
    method: str
    customer: Customer


class ReadBalance(CardPRBase):
    crm_key: str | UUID = ""
    method: str
    customer: Customer


class AddBalanceResponse(CardPRBase):
    success: bool


class CreateCustomerResponse(CardPRBase):
    customer_id: str | UUID


class ReadBalanceResponse(CardPRBase):
    success: bool
    bonus: str = ""
    balance: str = ""
    discount: str = ""
