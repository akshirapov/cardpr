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


def get_by_phone(*, db_session: Session, customer_phone: str) -> models.Customer | None:
    """Returns a customer based on the given phone."""

    if not customer_phone:
        return None
    return db_session.query(models.Customer).filter(models.Customer.phone == customer_phone).first()


def update(*, db_session: Session, customer: models.Customer, customer_in: Customer) -> models.Customer:
    """Updates a customer."""

    customer_data = customer.dict()
    update_data = customer_in.dict(skip_defaults=True, exclude={})

    for field in customer_data:
        if field in update_data:
            setattr(customer, field, update_data[field])

    db_session.commit()
    return customer


def update_or_create(*, db_session: Session, customer_in: Customer) -> models.Customer:
    "Updates a customer, creating a new one if necessary."

    customer = get_by_phone(db_session=db_session, customer_phone=customer_in.phone)
    if customer:
        return update(db_session=db_session, customer=customer, customer_in=customer_in)
    return create(db_session=db_session, customer_in=customer_in)
