from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from .base import Base


class Branch(Base):
    __tablename__ = "branches"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    address = Column(String(256), nullable=False)
    phone_number = Column(String(20), nullable=False)

    orders = relationship("Order", back_populates="branch")
