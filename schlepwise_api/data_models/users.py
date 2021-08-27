import attr
from attr.validators import instance_of

from schlepwise_api.models.users import User as UserORM


@attr.s(frozen=True, slots=True)
class User:
    orm: UserORM = attr.ib(validator=instance_of(UserORM))

    @classmethod
    def fetch_all(cls):
        users = []
        user_orms = UserORM.query.all()

        for orm in user_orms:
            users.append(
                cls(orm=orm)
            )
        
        return user_orms
