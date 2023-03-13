from app import ma
from marshmallow import fields

class FacilityAmenitySchema(ma.Schema):
    class Meta:
        # Define the fields to expose
        fields = ("id", "facility_id", "amenity_id")

facilityamenity_schema = FacilityAmenitySchema()
facilityamenities_schema = FacilityAmenitySchema(many=True) 