from flask import Blueprint
from flask_restx import Api, Resource, Swagger

from schlepwise_api.resources import users
from schlepwise_api.settings import Config

api_blueprint = Blueprint('api', __name__)


def register_api(app):
    app.register_blueprint(
        api_blueprint, url_prefix=f'/api/'
    )


api = Api(api_blueprint,
    version=Config.API_VERSION,
    title='Schlepwise API',
)


api.add_namespace(users.ns)
