from fastapi import APIRouter, Body

from app.schemas import AddBalance, CreateCustomer, ReadBalance
from app.services import add_balance, create_customer, read_balance

router = APIRouter()


ALLOWED_METHODS = ("addBalance", "createCustomer", "readBalance")


@router.post("/carpdr")
def capdpr_webhook(payload: dict = Body(...)):
    """Webhook from the service."""

    method = payload.get("method", "")
    if method not in ALLOWED_METHODS:
        return {"error": f"unsupported method <{method}>"}

    if method == "addBalance":
        return add_balance(AddBalance(**payload))
    elif method == "createCustomer":
        return create_customer(CreateCustomer(**payload))
    elif method == "readBalance":
        return read_balance(ReadBalance(**payload))
