from app import db
from flask import Flask
from flask import Blueprint
from app import bcrypt
from datetime import date
from models.facilities import Facility
from models.owners import Owner

db_commands = Blueprint("db", __name__)
app = Flask(__name__)

# to run the app
@app.cli.command()
def run():
    app.run()

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands .cli.command("seed")
def seed_db():

    # Create owners before facilities as owner id is needed in the facility model as an fkey
    owner1 = Owner(
        email = "owner1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        mobile = "04100475528"
    )
    db.session.add(owner1)
    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()

    facility = Facility(
        email = "admin@email.com",
        mobile = bcrypt.generate_password_hash("password123").decode("utf-8"),
    )
    db.session.add(facility)

    # create the card object
    card1 = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title = "Start the project",
        description = "Stage 1, creating the database",
        status = "To Do",
        priority = "High",
        date = date.today(),
        user_id = user1.id
    )
    # Add the object as a new row to the table
    db.session.add(card1)

    card2 = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title = "SQLAlchemy and Marshmallow",
        description = "Stage 2, integrate both modules in the project",
        status = "Ongoing",
        priority = "High",
        date = date.today(),
        # it also can be done this way
        user = user1
    )
    # Add the object as a new row to the tablef
    db.session.add(card2)

    # Commit changes between the creation of the users and cards. That way the user object 
    # will have its id available to add it to the card. Without this extra commit user's id is None.
    db.session.commit()
    print("Table seeded") 


@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 