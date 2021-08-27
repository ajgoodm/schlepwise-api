from flask import Flask

from schlepwise_api.database import db, migrate
from schlepwise_api.models import *
from schlepwise_api.settings import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app=app, db=db, compare_type=True, compare_server_default=True)

    return app
