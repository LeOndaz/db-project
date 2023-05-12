from sqlalchemy import Boolean, Column, Integer, String

from . import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    username = Column(String(256), index=True, unique=True, nullable=False)
    email = Column(String(256), index=True, unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    is_staff = Column(Boolean, default=False)
