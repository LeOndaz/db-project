from datetime import date

from sqlalchemy import Column, Date, Enum, Integer, Numeric, String
from sqlalchemy.orm import relationship

from utils.enums import ProductType

from .base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    price = Column(Numeric(12, 3), nullable=False)

    expiration_date = Column(Date, default=date.today, nullable=False)
    barcode = Column(String, nullable=False)
    type = Column(Enum(ProductType), default=ProductType.DRUG)

    lines = relationship("OrderLine", back_populates="product", cascade="all")
    product_insurances = relationship(
        "ProductInsurance", back_populates="product", cascade="all"
    )
    inventory_products = relationship(
        "InventoryProduct", back_populates="product", cascade="all"
    )

    sales = relationship("Sale", back_populates="product")
