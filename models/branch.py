from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Branch(Base):
    __tablename__ = "branches"

    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(String(256), nullable=False)
    address = Column(String(256), nullable=False)
    phone_number = Column(String(20), nullable=False)

    orders = relationship("Order", back_populates="branch", cascade="all")
    inventories = relationship("Inventory", back_populates="branch", cascade="all")
    sales = relationship("Sale", back_populates="branch")
