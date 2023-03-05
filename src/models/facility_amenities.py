from app import db

class FacilityAmenity(db.Model):
    __tablename__ = "facility_amenities"
    id = db.Column(db.Integer, primary_key=True)
    facility_id = db.Column(db.Integer, db.ForeignKey("facilities.id"), nullable=False)
    amenity_id = db.Column(db.Integer, db.ForeignKey("amenities.id"), nullable=False)