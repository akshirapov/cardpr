from fastapi import APIRouter, Body

from app.services import add_balance, create_customer, read_balance

router = APIRouter()


ALLOWED_METHODS = ("addBalance", "createCustomer", "readBalance")


@router.post("/webhook")
def webhook(hook_data: dict = Body(...)):
    method = hook_data.get("method", "")
    if method not in ALLOWED_METHODS:
        return {"error": f"unsupported method <{method}>"}

    if method == "addBalance":
        return add_balance(hook_data)
    elif method == "createCustomer":
        return create_customer(hook_data)
    elif method == "readBalance":
        return read_balance(hook_data)
