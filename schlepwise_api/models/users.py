__all__ = ['User']

from sqlalchemy import (
    Column,
    String,
)

from schlepwise_api.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
