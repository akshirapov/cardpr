from sqlalchemy.orm import Session

from app import models
from app.schemas import Customer


def create(*, db_session: Session, customer_in: Customer) -> models.Customer:
    """Creates a customer."""

    customer_data = customer_in.dict(exclude={"sum", "transaction_id", "card_numbers", "card_tracks"})

    customer = models.Customer(**customer_data)

    db_session.add(customer)
    db_session.commit()

    return customer
