from typing import List

from sqlalchemy.orm import Session

import models
import schemas
from utils import (
    create_db_entity,
    delete_by_entity_by_id,
    get_db_entity_by_id,
    get_db_entity_list,
    get_object_or_404,
    update_db_entity,
)


def get_inventory_by_id(db: Session, id) -> models.Inventory:
    return get_db_entity_by_id(db, models.Inventory, id)


def get_inventories(db: Session) -> List[models.Inventory]:
    return get_db_entity_list(db, models.Inventory)


def delete_inventory(db: Session, id) -> models.Inventory:
    return delete_by_entity_by_id(db, models.Inventory, schemas.Inventory, id)


def create_inventory(db: Session, data: schemas.InventoryCreate) -> models.Inventory:
    return create_db_entity(db, models.Inventory, data)


def update_inventory_by_id(
    db: Session, id: int, data: schemas.InventoryUpdate
) -> models.Inventory:
    return update_db_entity(db, models.Inventory, id, data)


def get_inventory_product(db: Session, inventory_id: int, product_id: int):
    return db.get(
        models.InventoryProduct,
        {"inventory_id": inventory_id, "product_id": product_id},
    )


def add_product_to_inventory(
    db: Session, inventory_id: int, data: schemas.AddProductToInventory
) -> models.Inventory:
    inventory: models.Inventory = get_object_or_404(
        db, models.Inventory, "id", inventory_id
    )
    product: models.Product = get_object_or_404(
        db, models.Product, "id", data.product_id
    )
    inventory_product = get_inventory_product(db, inventory_id, data.product_id)

    if inventory_product:
        inventory_product.quantity += data.quantity
    else:
        inventory_product = models.InventoryProduct(
            inventory=inventory, product=product, quantity=data.quantity
        )
        db.add(inventory_product)

    db.commit()
    db.refresh(inventory)

    return inventory


def remove_product_from_inventory(
    db: Session, inventory_id, product_id
) -> models.Inventory:
    inventory = get_object_or_404(db, models.Inventory, "id", inventory_id)

    inventory_product = get_inventory_product(db, inventory_id, product_id)

    db.delete(inventory_product)
    db.commit()
    db.refresh(inventory)

    return inventory
