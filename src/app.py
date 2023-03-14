from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# # from config import Config
# from dotenv import load_dotenv
# from config import app_config


# load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")
    
    # app.config.from_object(Config)
    # app.config.from_object(app_config)

    # creating our database object! This allows us to use our ORM
    db.init_app(app)
    
    # creating our marshmallow object! This allows us to use schemas
    ma.init_app(app)

    #creating the jwt and bcrypt objects! this allows us to use authentication
    bcrypt.init_app(app)
    jwt.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    # import the controllers and activate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    
    # def init_db():
    #     from models.facility_types import FacilityType

    #     # check if default facility types have already been added to database
    #     if FacilityType.query.first() is not None:
    #         print('Default facility types already exist in database.')
    #         return

    #     # add default facility types to the database
    #     facility_types = [
    #         FacilityType(name="Pilates Studio"),
    #         FacilityType(name="Gym"),
    #         FacilityType(name="Wellness Center"),
    #         FacilityType(name="Yoga Studio"),
    #         FacilityType(name="Dance Studio"),
    #         FacilityType(name="Athletic Club"),
    #         FacilityType(name="Boxing Gym"),
    #         # add more facility types as needed
    #     ]
    #     with app.app_context():
    #         with db.session.begin():
    #             db.session.add_all(facility_types)
    
    # init_db()
    return app