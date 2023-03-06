from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


auth = Blueprint('auth', __name__, url_prefix="/auth")
owners = Blueprint('owners', __name__, url_prefix='/owners')

def create_app():
    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

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

    return app