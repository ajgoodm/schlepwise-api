from flask_restx import Resource, reqparse

from schlepwise_api.data_models.users import User
from schlepwise_api.resources.models.users import user_model
from schlepwise_api.resources.namespaces import users_ns as ns


@ns.route('/')
class Users(Resource):
    @ns.doc('list_users')
    @ns.doc(description='Get users')
    @ns.expect(reqparse.RequestParser())
    @ns.marshal_with(user_model)
    def get(self):
        return User.fetch_all()
