from sqlalchemy.orm import Session

from app.schemas import (
    AddBalance,
    AddBalanceResponse,
    CreateCustomer,
    CreateCustomerResponse,
    ReadBalance,
    ReadBalanceResponse,
)


def add_balance(*, db: Session, data: AddBalance) -> AddBalanceResponse:
    """Accrues welcome and referral bonuses."""
    return AddBalanceResponse(success=True)


def create_customer(*, db: Session, data: CreateCustomer) -> CreateCustomerResponse:
    """Creates a customer."""
    return CreateCustomerResponse(customer_id="")


def read_balance(*, db: Session, data: ReadBalance) -> ReadBalanceResponse:
    """Returns loyality system info."""
    return ReadBalanceResponse(success=True)
