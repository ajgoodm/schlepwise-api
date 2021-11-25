__all__ = ['Task', 'Chore']

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.sql import func

from schlepwise_api.database import Base


class Task(Base):
    """User defined list of household tasks separated
    from scheduling or performance
    """
    __tablename__ = "tasks"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)


class Chore(Base):
    """An instance of a scheduled task
    """
    __tablename__ = "chores"
    task_id = Column(String, ForeignKey('tasks.id'), nullable=False, primary_key=True)
    household_id = Column(String, ForeignKey('households.id'), nullable=False, primary_key=True)
    requested_by_id = Column(String, ForeignKey('users.id'), nullable=False, primary_key=True)
    requested_at = Column(DateTime, nullable=False, primary_key=True, server_default=func.now())
