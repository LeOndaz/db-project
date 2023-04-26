from sqlalchemy import String, Column, Integer, Numeric, Enum, Date, BigInteger
from sqlalchemy.orm import relationship

from .base import Base
from datetime import date
import enum


class Product(Base):
    class ProductType(enum.Enum):
        DRUG = 0
        BEAUTY = 1

    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, index=True)

    name = Column(String, nullable=False)
    price = Column(Numeric(12, 3), nullable=False)

    expiration_date = Column(Date, default=date.today, nullable=False)
    barcode = Column(String, nullable=False)
    type = Column(Enum(ProductType))

    lines = relationship("OrderLine", back_populates="product")
    product_insurances = relationship("ProductInsurance", back_populates="product")
