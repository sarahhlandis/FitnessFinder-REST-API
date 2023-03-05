from app import db

class FacilityType(db.Model):
    # define the table name for the db
    __tablename__= "facility_types"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    
    # Add the rest of the attributes (columns). 
    facility_type: db.Column(db.String(25), nullable=False, default=None)
    
    # Add the foreign keys in the Facility_types model - none

    # Add the relationships directions to other models
    facilities = db.relationship('Facility', backref='facility_type', lazy=True)