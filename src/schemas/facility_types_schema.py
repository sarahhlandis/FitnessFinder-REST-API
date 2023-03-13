from marshmallow import fields
from app import ma

class FacilityTypeSchema(ma.Schema):
    class Meta:
        # Define the fields to expose
        fields = ("id", "facility_type")


facilitytype_schema = FacilityTypeSchema()
facilitytypes_schema = FacilityTypeSchema(many=True) 