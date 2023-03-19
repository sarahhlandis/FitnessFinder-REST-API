from app import db


# define the join table for facility amenities (many-many)
facility_amenities = db.Table('facility_amenities',
    db.Column('facility_id', db.Integer, db.ForeignKey('facilities.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True),
    db.Column('has_amenity', db.Boolean, default=True)
)

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
    facility_type = db.Column(db.Integer, db.ForeignKey("facility_types.id"), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id", ondelete='CASCADE'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
    
    # Add the relationships directions to other models
    promotions = db.relationship('Promotion', backref='facility_promotions', lazy=True, cascade="all, delete-orphan")
    address = db.relationship('Address', backref='facility')
    # facility_type = db.relationship('FacilityType', backref='facility_types', lazy=True)
    owner = db.relationship('Owner', backref="owner_facilities", cascade="all, delete-orphan", single_parent=True)
    amenities = db.relationship('Amenity', secondary=facility_amenities, lazy='subquery', backref=db.backref('facilities', lazy='dynamic'))


    # # Set up join table with amenities
    # facility_amenities = db.relationship('Amenity', secondary=facility_amenities, lazy='subquery', backref='facilities_amenities', extend_existing=True)

