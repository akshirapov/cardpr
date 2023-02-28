from sqlalchemy.orm import Session


from app.schemas import (
    AddBalanceResponse,
    Customer,
    ReadBalanceResponse,
)


def add(*, db_session: Session, customer_in: Customer) -> AddBalanceResponse:
    """Accrues welcome and referral bonuses."""

    return AddBalanceResponse(success=True)


def read(*, db_session: Session, customer_in: Customer) -> ReadBalanceResponse:
    """Returns loyality system info."""

    return ReadBalanceResponse(success=True)
