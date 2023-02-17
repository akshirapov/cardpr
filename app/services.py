from app.schemas import (
    AddBalance,
    AddBalanceResponse,
    CreateCustomer,
    CreateCustomerResponse,
    ReadBalance,
    ReadBalanceResponse,
)


def add_balance(data: AddBalance) -> AddBalanceResponse:
    """Accrues welcome and referral bonuses."""
    return AddBalanceResponse(success=True)


def create_customer(data: CreateCustomer) -> CreateCustomerResponse:
    """Creates a customer."""
    return CreateCustomerResponse(customer_id="")


def read_balance(data: ReadBalance) -> ReadBalanceResponse:
    """Returns loyality system info."""
    return ReadBalanceResponse(success=True)
