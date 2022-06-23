
from cgitb import reset
from flask import Flask
from .participants import participants
from .participants import reset_database


def create_app():
    '''Initialises microservice'''
    app = Flask(__name__)

    # Register participant endpoints
    app.register_blueprint(participants, url_prefix='/api')
    reset_database()

    return app
