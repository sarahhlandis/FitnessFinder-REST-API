from app import db

class FacilityAmenity(db.Model):
    __tablename__ = 'facility_amenities'
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.id'), primary_key=True)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
    db.Column('has_amenity', db.Boolean, default=True)