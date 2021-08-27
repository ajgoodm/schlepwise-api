from flask_restx import fields

from schlepwise_api.resources.namespaces import users_ns as ns


user_model = ns.model(
    'User',
    {
        'id': fields.String(attribute='orm.id'),
        'name': fields.String(attribute='orm.name'),
    },
)

user_input_model = ns.model(
    'UserInput',
    {
        'name': fields.String(required=True, min_length=1),
    },
)
