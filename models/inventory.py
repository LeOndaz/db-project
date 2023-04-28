from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Inventory(Base):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    barcode = Column(String, nullable=False)

    branch = relationship("Branch", back_populates="inventories", cascade="all")
    branch_id = Column(ForeignKey("branches.id"))

    inventory_products = relationship(
        "InventoryProduct", back_populates="inventory", cascade="all"
    )


class InventoryProduct(Base):
    __tablename__ = "inventory_products"

    id = Column(Integer, primary_key=True, index=True)

    inventory_id = Column(ForeignKey("inventories.id"), nullable=False)
    inventory = relationship(
        "Inventory", back_populates="inventory_products", cascade="all"
    )

    product_id = Column(ForeignKey("products.id"), nullable=False)
    product = relationship(
        "Product", back_populates="inventory_products", cascade="all"
    )

    quantity = Column(Integer, nullable=False)
