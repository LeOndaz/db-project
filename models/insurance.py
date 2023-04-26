from sqlalchemy import Column, BigInteger, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Insurance(Base):
    __tablename__ = "insurances"

    id = Column(BigInteger, primary_key=True, index=True)

    name = Column(String(256), nullable=False)
    discount_percentage = Column(Integer, nullable=False)

    lines = relationship("OrderLine", back_populates="insurance")
    product_insurances = relationship("ProductInsurance", back_populates="insurances")


class ProductInsurance(Base):
    __tablename__ = "product_insurances"

    id = Column(BigInteger, primary_key=True, index=True)

    insurance_id = Column(ForeignKey("insurances.id"))
    insurance = relationship("Insurance", back_populates="product_insurances")

    product_id = Column(ForeignKey("products.id"))
    product = relationship("Product", back_populates="product_insurances")
