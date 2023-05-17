from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from .base import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(
        Integer,
        primary_key=True,
    )

    starts_at = Column(DateTime)
    ends_at = Column(DateTime)

    percentage = Column(Numeric(4, 2), nullable=True)
    amount = Column(Numeric(10, 2), nullable=True)

    branch = relationship("Branch", back_populates="sales")
    branch_id = Column(ForeignKey("branches.id"), nullable=True)

    product_id = Column(ForeignKey("products.id"))
    product = relationship("Product", back_populates="sales", cascade="all")
