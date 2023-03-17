from app import ma
from marshmallow import fields
from schemas.amenities_schema import AmenitySchema

class FacilityAmenitySchema(ma.Schema):
    class Meta:
        # Define the fields to expose
        fields = ("facility_id", "amenity_id", "name")
        load_only=["id"]

    amenity = fields.Nested(AmenitySchema, attribute='amenity.name')

facilityamenity_schema = FacilityAmenitySchema()
facilityamenities_schema = FacilityAmenitySchema(many=True) 