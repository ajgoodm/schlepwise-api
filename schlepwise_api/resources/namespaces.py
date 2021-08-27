from flask_restx import Namespace

users_ns = Namespace(
    'users',
    description='schlepwise users'
)
