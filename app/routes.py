from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.core import get_db
from app.schemas import Customer, Webhook
from app.services import balance as svcs_balance, customer as svcs_customer

router = APIRouter()


ALLOWED_METHODS = ("addBalance", "createCustomer", "readBalance")


@router.post("/webhook")
def webhook(*, db_session: Session = Depends(get_db), webhook_in: Webhook):
    """A webhook from the wallet cards service ."""

    webhook_data = webhook_in.dict()

    method = webhook_data.get("method", "")
    if method not in ALLOWED_METHODS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"error": f"unsupported method <{method}>"}],
        )
    customer_dict = webhook_data.get("customer", {})
    customer_data = Customer(**customer_dict)

    if method == "createCustomer":
        return create_customer(db_session=db_session, customer_in=customer_data)
    elif method == "addBalance":
        return add_balance(db_session=db_session, customer_in=customer_data)
    elif method == "readBalance":
        return read_balance(db_session=db_session, customer_in=customer_data)


@router.post("/createCustomer")
def create_customer(*, db_session: Session = Depends(get_db), customer_in: Customer):
    """Creates a new customer."""

    customer = svcs_customer.create(db_session=db_session, customer_in=customer_in)
    return customer.guid


@router.post("/addBalance")
def add_balance(*, db_session: Session = Depends(get_db), customer_in: Customer):
    """Accrues welcome and referral bonuses for a customer."""
    return svcs_balance.add(db_session=db_session, customer_in=customer_in)


@router.post("/readBalance")
def read_balance(*, db_session: Session = Depends(get_db), customer_in: Customer):
    """Returns the loyality system info of a customer."""
    return svcs_balance.read(db_session=db_session, customer_in=customer_in)
