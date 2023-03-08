from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.facility_types import FacilityType
from app import db

facilities = Blueprint('facilities', __name__, url_prefix="/facilities")
auth = Blueprint('auth', __name__, url_prefix="/login")
owners = Blueprint('owners', __name__, url_prefix='/owners')


def create_app():
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    # configuring our app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:@dmin1@localhost/fitnessfinder_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # creating our database object! This allows us to use our ORM
    db.init_app(app)
    
    # creating our marshmallow object! This allows us to use schemas
    ma.init_app(app)

    # register and activate blueprints
    app.register_blueprint(auth)
    app.register_blueprint(owners)
    app.register_blueprint(facilities)

    return app

def init_db():
    # check if default facility types have already been added to database
    if FacilityType.query.first() is not None:
        print('Default facility types already exist in database.')
        return

    # add default facility types to the database
    facility_types = [
        FacilityType(name="Pilates Studio"),
        FacilityType(name="Gym"),
        FacilityType(name="Wellness Center"),
        FacilityType(name="Yoga Studio"),
        FacilityType(name="Dance Studio"),
        FacilityType(name="Athletic Club"),
        FacilityType(name="Boxing Gym"),
        # add more facility types as needed
    ]
    with db.session.begin():
        db.session.add_all(facility_types)

