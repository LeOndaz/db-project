from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from .base import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)

    address = Column(String(256), nullable=False)
    phone_number = Column(String(20), nullable=False)

    orders = relationship("Order", back_populates="customer", cascade="all")
    # lines = relationship("OrderLine", back_populates="customer")

    created_at = Column(DateTime, default=datetime.utcnow)

    customer_insurances = relationship(
        "CustomerInsurance", back_populates="customer", cascade="all"
    )


class CustomerInsurance(Base):
    __tablename__ = "customer_insurances"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(ForeignKey("customers.id"))
    customer = relationship(
        "Customer", back_populates="customer_insurances", cascade="all"
    )

    insurance_id = Column(ForeignKey("insurances.id"))
    insurance = relationship(
        "Insurance", back_populates="customer_insurances", cascade="all"
    )
