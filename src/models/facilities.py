from datetime import time
from models import facility_amenities
from models.facility_types import FacilityType
from app import db

class Facility(db.Model):
    # define the table name for the db
    __tablename__= "facilities"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # Add the rest of the attributes (columns). 
    phone_num = db.Column(db.String(10), nullable=False)
    independent = db.Column(db.Boolean(), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    opening_time = db.Column(db.Time(), nullable=False)
    closing_time = db.Column(db.Time(), nullable=False)

    # Add the foreign keys in the Facilities model
    facility_type_id = db.Column(db.Integer, db.ForeignKey("facility_type.id"), nullable=True, ondelete='SETNULL')
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
    
    # Add the relationships directions to other models
    promotions = db.relationship('Promotion', backref='facility', lazy=True)
    address = db.relationship('Address', backref='facility')
    owner = db.relationship("Owner", backref=db.backref("facilities", cascade="all, delete-orphan"))
    facility_type = db.relationship('FacilityType', backref=db.backref('facilities', lazy=True))

    # Set up join table with amenities
    amenities = db.relationship('Amenity', secondary=facility_amenities, lazy='subquery', backref=db.backref('facilities', lazy='dynamic'))


    def __init__(self, phone_num, independent, business_name, hours_of_op, facility_type, owner_id, address_id):
        self.phone_num = phone_num
        self.independent = independent
        self.business_name = business_name
        self.opening_time = time(hour=hours_of_op.hour, minute=hours_of_op.minute)
        self.closing_time = time(hour=hours_of_op.hour, minute=hours_of_op.minute)
        self.facility_type = FacilityType.query.filter_by(facility_type=facility_type).first()
        self.owner_id = owner_id
        self.address_id = address_id
