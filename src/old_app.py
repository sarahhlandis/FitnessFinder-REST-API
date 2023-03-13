from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Creating the flask app object - this is the core of our app!
app = Flask(__name__)


# configuring our app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:@dmin1@localhost/fitnessfinder_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(app.config['SQLALCHEMY_DATABASE_URI'])  # added print statement


# creating our database object! This allows us to use our ORM
db = SQLAlchemy(app)

# creating our marshmallow object! This allows us to use schemas
ma = Marshmallow(app)


def init_db():
    from models.facility_types import FacilityType

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
    with app.app_context():
        with db.session.begin():
            db.session.add_all(facility_types)

def create_app():
    db.init_app(app)
    
    # call init_db() function and pass app.config to it
    with app.app_context():
        init_db(app.config)

    ma.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
