from app import db
# from models import facility_amenities

class Amenity(db.Model):
    # define the table name for the db
    __tablename__= "amenities"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    # # Add the rest of the attributes (columns). 
    # parking = db.Column(db.Boolean(), nullable=True)
    # pool = db.Column(db.Boolean(), nullable=True)
    # sauna = db.Column(db.Boolean(), nullable=True)
    # steam_room = db.Column(db.Boolean(), nullable=True)
    # fuel_bar = db.Column(db.Boolean(), nullable=True)    
    # pilates = db.Column(db.Boolean(), nullable=True)
    # boxing = db.Column(db.Boolean(), nullable=True)
    # yoga = db.Column(db.Boolean(), nullable=True)
    # private_training = db.Column(db.Boolean(), nullable=True)
    # lockers = db.Column(db.Boolean(), nullable=True)
    # showers = db.Column(db.Boolean(), nullable=True)

    # Add the foreign keys in the Amenities model - none

    # # Set up join table with amenities
    # facilities = db.relationship('Facility', secondary=facility_amenities, lazy='subquery', backref=db.backref('amenities', lazy=True))
