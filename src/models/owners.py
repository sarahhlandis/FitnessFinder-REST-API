from app import bcrypt
from app import db
from sqlalchemy.orm import validates

class Owner(db.Model):
    # define the table name for the db
    __tablename__= "owners"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    
    # Add the rest of the attributes (columns). 
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    mobile = db.Column(db.String(10), nullable=False, unique=True)
    
    # Add the relationships directions to other models
    facilities = db.relationship('Facility', backref="facility_owners", cascade="all, delete-orphan")


    # # Add a validation for the password field to be >= 8 chars
    # @validates('password')
    # def validate_password(self, password):
    #     if len(password) != 8:
    #         raise ValueError("Password must be 8 characters long. Please try again.")
    #     return password
    
    # @validates('mobile')
    # def validate_mobile(self, mobile):
    #     if len(mobile) != 10:
    #         raise ValueError('Phone number must be 10 digits long.')
        
