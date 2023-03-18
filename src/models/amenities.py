from app import db
# from models import facility_amenities

class Amenity(db.Model):
    # define the table name for the db
    __tablename__= "amenities"
    # Set the primary key, we need to define that each attribute is also a 
    # column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
