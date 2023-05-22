from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    price = Column(Numeric(12, 3), nullable=True)
    amount_paid = Column(Numeric(12, 3), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    branch = relationship("Branch", back_populates="orders")
    branch_id = Column(ForeignKey("branches.id"))

    customer = relationship("Customer", back_populates="orders")
    customer_id = Column(ForeignKey("customers.id"))

    lines = relationship("OrderLine", back_populates="order", cascade="all")


class OrderLine(Base):
    __tablename__ = "order_lines"

    id = Column(Integer, primary_key=True, index=True)

    insurance_id = Column(ForeignKey("insurances.id"), nullable=True)
    insurance = relationship("Insurance", back_populates="lines")

    product_id = Column(ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates="lines")

    order_id = Column(ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="lines")

    # customer_id = Column(ForeignKey("customers.id"), nullable=False)
    # customer = relationship("Customer", back_populates="lines")

    quantity = Column(Integer, nullable=False, default=1)
