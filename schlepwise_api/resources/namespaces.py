from flask_restx import Namespace

household_ns = Namespace(
    'households',
    description='schlepwise households'    
)


users_ns = Namespace(
    'users',
    description='schlepwise users'
)
