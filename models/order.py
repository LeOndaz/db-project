from sqlalchemy import Column, BigInteger, ForeignKey, Numeric, Integer
from sqlalchemy.orm import relationship
from .base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(BigInteger, primary_key=True, index=True)
    price = Column(Numeric(12, 3), nullable=False)

    branch = relationship("Order", back_populates="orders")
    branch_id = Column(ForeignKey("branches.id"))

    lines = relationship("OrderLine", back_populates="order")


class OrderLine(Base):
    __tablename__ = "order_lines"

    id = Column(BigInteger, primary_key=True, index=True)

    insurance_id = Column(ForeignKey("insurances.id"))
    insurance = relationship("Insurance", back_populates="lines")

    product_id = Column(ForeignKey("products.id"))
    product = relationship("Product", back_populates="lines")

    order_id = Column(ForeignKey("orders.id"))
    order = relationship("Order", back_populates="lines")

    customer_id = Column(ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="orders")

    quantity = Column(Integer, nullable=False, default=1)
