from flask_restx import fields

from schlepwise_api.resources.namespaces import (
    household_ns,
    users_ns,
)



user_model = users_ns.model(
    'User',
    {
        'id': fields.String(attribute='orm.id'),
        'name': fields.String(attribute='orm.name'),
        'household_id': fields.String(attribute='orm.household_id')
    },
)

user_input_model = users_ns.model(
    'UserInput',
    {
        'name': fields.String(required=True, min_length=1),
        'household_id': fields.String(required=True, min_length=1),
    },
)


household_model = household_ns.model(
    'Household',
    {
        'id': fields.String(attribute='orm.id'),
        'name': fields.String(attribute='orm.name'),
        'users': fields.List(fields.Nested(user_model, skip_none=True))
    },
)


household_input_model = household_ns.model(
    'Household',
    {
        'name': fields.String(required=True, min_length=1),
    },
)
