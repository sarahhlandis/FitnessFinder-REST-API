from marshmallow import fields
from app import ma
from models.facility_amenities import FacilityAmenity

class FacilityAmenitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FacilityAmenity
    
    id = fields.Integer(dump_only=True)
    facility_id = fields.Integer(required=True)
    amenity_id = fields.Integer(required=True)
