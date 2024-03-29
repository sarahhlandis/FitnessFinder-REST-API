from marshmallow import fields, validates_schema, validate, ValidationError
from marshmallow.fields import Length
from app import ma
from datetime import time
from schemas.addresses_schema import AddressSchema

class FacilitySchema(ma.Schema):
    class Meta:
        ordered = True
        # Define the fields to expose
        fields = ("business_name", "independent", "phone_num", "opening_time", 
                "closing_time", "address", "amenities", "promotions", "facility_type")
        
        load_only = ["owner_id","facility_type_id","address_id", "id"]
        
    phone_num = fields.String(required=True, validate=[Length(equal=10), validate.Regexp('^\d+$')])
    opening_time = fields.Time(required=True, format='%H:%M')
    closing_time = fields.Time(required=True, format='%H:%M')

    # address = ma.Nested("AddressSchema")
    address = ma.Nested(AddressSchema)

    # amenities = ma.Nested("AmenitySchema", many=True)
    amenities = fields.List(fields.Nested("FacilityAmenitySchema"))
    promotions = fields.List(fields.Nested("PromotionSchema"))

    # Nested field to include facility type with name
    # don't forget to add "facility_type" into fields at the top to expose
    # facility_type = fields.Nested(FacilityTypeSchema, attribute='facility_type', only=('name',))

   
    

    def validate_phone_num(self, data, **kwargs):
        if len(data['phone_num']) != 10:
            raise ValidationError('Phone number must be 10 digits long.')
        

    @validates_schema
    def validate_opening_closing_times(self, data, **kwargs):
        opening_time = data.get('opening_time')
        closing_time = data.get('closing_time')

        if opening_time is None or closing_time is None:
            # ff either opening time or closing time is missing, we can't do validation
            return

        try:
            # parse the opening and closing times into time objects
            opening_time = time.fromisoformat(opening_time.isoformat())
            closing_time = time.fromisoformat(closing_time.isoformat())

            # check opening time is before the closing time
            if opening_time >= closing_time:
                raise ValidationError('Opening time must be before closing time.')

        except:
            raise ValidationError("Incorrect time format.")


facility_schema = FacilitySchema()
facilities_schema = FacilitySchema(many=True) 