from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from app.db.core import get_db
from app.schemas import AddBalance, CreateCustomer, ReadBalance
from app.services import add_balance, create_customer, read_balance

router = APIRouter()


ALLOWED_METHODS = ("addBalance", "createCustomer", "readBalance")


@router.post("/cardpr")
def cardpr_webhook(*, db: Session = Depends(get_db), payload: dict = Body(...)):
    """Webhook from the service."""

    method = payload.get("method", "")
    if method not in ALLOWED_METHODS:
        return {"error": f"unsupported method <{method}>"}

    if method == "addBalance":
        return add_balance(db=db, data=AddBalance(**payload))
    elif method == "createCustomer":
        return create_customer(db=db, data=CreateCustomer(**payload))
    elif method == "readBalance":
        return read_balance(db=db, data=ReadBalance(**payload))
