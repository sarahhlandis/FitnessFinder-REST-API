from marshmallow import fields, Length
from app import ma
from models.facility_types import FacilityType

class FacilityTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FacilityType
    
    id = fields.Integer(dump_only=True)
    facility_type = fields.String(required=True)
