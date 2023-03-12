from datetime import date
from app import db

class Promotion(db.Model):
    # define the table name for the db
    __tablename__= "promotions"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # Add the rest of the attributes (columns). 
    name = db.columb(db.String(100), nullable=False, default=None)
    start_date = db.Column(db.Date(), nullable=False, default=None)
    end_date = db.Column(db.Date(), nullable=False, default=None)
    discount = db.Column(db.Integer(), nullable=False)
    
    # Add the foreign keys in the Promotions model
    facility_id = db.Column(db.Integer, db.ForeignKey("facilities.id"), nullable=False)

    # Add the relationships directions to other models
    facility = db.relationship('Facility', backref='promotions')

