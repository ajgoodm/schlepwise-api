from __future__ import annotations

import attr
from attr.validators import instance_of
import typing as T

from schlepwise_api.database import db
from schlepwise_api.models.users import Household as HouseholdORM
from schlepwise_api.models.users import User as UserORM
from schlepwise_api.utils import short_id


@attr.s(frozen=True, slots=True)
class Household:
    orm: HouseholdORM = attr.ib(validator=instance_of(HouseholdORM))

    @classmethod
    def fetch_all(cls) -> T.List[User]:
        households = []
        user_orms = HouseholdORM.query.all()

        for orm in user_orms:
            households.append(
                cls(orm=orm)
            )
        
        return households

    @classmethod
    def fetch_by_id(cls, household_id: str) -> T.Optional[Household]:
        household_orm = HouseholdORM.query.filter(HouseholdORM.id == household_id).one_or_none()
        if household_orm is not None:
            return cls(orm=household_orm)

    @classmethod
    def create_household(cls, name: str, commit: bool=False) -> User:
        household_orm = HouseholdORM(
            id=short_id(),
            name=name,
        )

        db.session.add(household_orm)
        if commit:
            db.session.commit()

        return cls(orm=household_orm)


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
    def fetch_by_id(cls, user_id: str) -> T.Optional[User]:
        user_orm = UserORM.query.filter(UserORM.id == user_id).one_or_none()
        if user_orm is not None:
            return cls(orm=user_orm)

    @classmethod
    def create_user(cls, name: str, household_id: str, commit: bool=False) -> User:
        user_orm = UserORM(
            id=short_id(),
            name=name,
            household_id=household_id,
        )

        db.session.add(user_orm)
        if commit:
            db.session.commit()

        return cls(orm=user_orm)
