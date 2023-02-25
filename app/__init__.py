from flask import Flask

from app.db import db
from app.models import CultureOrganization, Photo


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
