from app import db

class PostCode(db.Model):
    # define the table name for the db
    __tablename__= "post_codes"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    
    # Add the rest of the attributes (columns). 
    post_code = db.Column(db.String(4), nullable=False)
    
    # Add the foreign keys in the Post_codes model - none

    # Add the relationships directions to other models
    addresses = db.relationship('Address', backref='post_code')