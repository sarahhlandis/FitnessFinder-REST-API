from app import db

class FacilityType(db.Model):
    __tablename__ = "facility_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Add the relationships directions to other models
    facilities = db.relationship('Facility', backref='facility_types', lazy=True)
