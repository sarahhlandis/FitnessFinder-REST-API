from app import db

class Address(db.Model):
    # define the table name for the db
    __tablename__= "addresses"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    
    # Add the rest of the attributes (columns). 
    street_num = db.Column(db.Integer(), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    suburb =  db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(3), nullable=False)

    # Add the foreign keys in the Addresses model
    post_code_id = db.Column(db.Integer, db.ForeignKey("post_codes.id"), nullable=False)

    # Add the relationships directions to other models
    post_code = db.relationship('PostCode', backref='post_code_addresses')