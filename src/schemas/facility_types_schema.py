from app import ma

class FacilityTypeSchema(ma.Schema):
    class Meta:
        # Define the fields to expose
        fields = ("id", "name")

facilitytype_schema = FacilityTypeSchema()
facilitytypes_schema = FacilityTypeSchema(many=True) 