from sqlalchemy import Column, BigInteger, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, index=True)

    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)

    address = Column(String(256), nullable=False)
    phone_number = Column(String(20), nullable=False)

    orders = relationship("Order", back_populates="customer")


class CustomerInsurance(Base):
    __tablename__ = "customer_insurances"

    id = Column(BigInteger, primary_key=True, index=True)

    customer_id = Column(ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="customer_insurances")

    insurance_id = Column(ForeignKey("insurances.id"))
    insurance = relationship("Insurance", back_populates="customer_insurances")
