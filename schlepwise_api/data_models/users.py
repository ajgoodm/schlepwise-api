from __future__ import annotations

import attr
from attr.validators import instance_of
import typing as T

from schlepwise_api.database import db
from schlepwise_api.models.users import User as UserORM
from schlepwise_api.utils import short_id


@attr.s(frozen=True, slots=True)
class User:
    orm: UserORM = attr.ib(validator=instance_of(UserORM))

    @classmethod
    def fetch_all(cls) -> T.List[User]:
        users = []
        user_orms = UserORM.query.all()

        for orm in user_orms:
            users.append(
                cls(orm=orm)
            )
        
        return users
    
    @classmethod
    def create_user(cls, name: str, commit: bool=False) -> User:
        user_orm = UserORM(
            id=short_id(),
            name=name,
        )

        db.session.add(user_orm)
        if commit:
            db.session.commit()

        return cls(orm=user_orm)
