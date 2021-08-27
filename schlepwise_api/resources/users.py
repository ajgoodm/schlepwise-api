from flask import request
from flask_restx import Resource, reqparse

from schlepwise_api.database import db
from schlepwise_api.data_models.users import User
from schlepwise_api.resources.models.users import user_input_model, user_model
from schlepwise_api.resources.namespaces import users_ns as ns


@ns.route('/')
class Users(Resource):
    @ns.doc('list_users')
    @ns.doc(description='Get users')
    @ns.expect(reqparse.RequestParser())
    @ns.marshal_with(user_model)
    def get(self):
        return User.fetch_all()


    @ns.doc('create_user')
    @ns.doc(description='Create a user')
    @ns.expect(user_input_model, validate=True)
    @ns.marshal_with(user_model)
    def post(self):
        request_data = request.json

        user = User.create_user(name=request_data['name'])
        db.session.commit()

        return user
