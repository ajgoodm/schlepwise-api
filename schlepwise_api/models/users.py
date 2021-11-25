__all__ = ['Household', 'User']

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
)
from sqlalchemy.orm import relationship

from schlepwise_api.database import Base


class Household(Base):
    __tablename__ = "households"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    users = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    household_id = Column(String, ForeignKey('households.id'), nullable=False)
