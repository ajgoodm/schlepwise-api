from flask import request
from flask_restx import Resource, reqparse

from schlepwise_api.database import db
from schlepwise_api.data_models.users import Household
from schlepwise_api.resources.models.users import household_input_model, household_model
from schlepwise_api.resources.namespaces import household_ns as ns


@ns.route('/')
class HouseHolds(Resource):
    @ns.doc('list_households')
    @ns.doc(description='Get households')
    @ns.expect(reqparse.RequestParser())
    @ns.marshal_with(household_model)
    def get(self):
        return Household.fetch_all()

    @ns.doc('create_household')
    @ns.doc(description='Create a household')
    @ns.expect(household_input_model, validate=True)
    @ns.marshal_with(household_model)
    def post(self):
        request_data = request.json

        user = Household.create_household(
            name=request_data['name'],
        )
        db.session.commit()

        return user