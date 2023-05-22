from typing import List

from sqlalchemy.orm import Session

import models
import schemas
from utils import (
    delete_by_entity_by_id,
    get_db_entity_by_id,
    get_db_entity_list,
    get_object_or_404,
    update_db_entity, get_order_total,
)


def get_order_by_id(db: Session, id) -> models.Order:
    return get_db_entity_by_id(db, models.Order, id)


def get_orders(db: Session, branch_id=None) -> List[models.Order]:
    filters = {}

    if branch_id:
        filters["branch_id"] = branch_id

    return get_db_entity_list(db, models.Order, **filters)


def delete_order(db: Session, id) -> models.Order:
    return delete_by_entity_by_id(db, models.Order, schemas.Order, id)


def create_order(db: Session, data: schemas.OrderCreate) -> models.Order:
    branch = get_object_or_404(db, models.Branch, "id", data.branch_id)
    customer = get_object_or_404(db, models.Customer, "id", data.customer_id)

    order = models.Order(branch=branch, customer=customer)
    db.add(order)
    db.commit()

    lines = []

    for line_data in data.lines:
        product = get_object_or_404(db, models.Product, "id", line_data.product_id)
        line = models.OrderLine(
            product=product, quantity=line_data.quantity, order=order
        )
        lines.append(line)

    order.price = get_order_total(customer, lines)
    db.add_all(lines)
    db.commit()

    db.refresh(order)

    return order


def update_order_by_id(db: Session, id: int, data: schemas.OrderUpdate) -> models.Order:
    return update_db_entity(db, models.Order, id, data)
