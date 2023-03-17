from marshmallow import fields, validate, validates_schema, ValidationError
from flask_marshmallow import Marshmallow
from marshmallow.validate import Length
from models.owners import Owner

ma = Marshmallow()

class OwnerSchema(ma.Schema):
    class Meta:
        ordered = True
        # Define the fields to expose
        fields = ("name", "email", "mobile", "password")

        load_only = ["id"]

    # set the password's length to exactly 8 character long
    password = ma.String(validate=[Length(equal=8)])
    # check the mobile num is 10 digits and contains no letters
    mobile = ma.String(validate=[Length(equal=10), validate.Regexp('^\d+$')])
    # exclude owner to avoid circ ref
    facilities = fields.List(fields.Nested("FacilitySchema", many=True, exclude=('owner', )))

    # validate mobile number length
    @validates_schema
    def validate_mobile(self, data):
        if len(data['mobile']) != 10:
            raise ValidationError('Phone number must be 10 digits long. Please try again.')
        
    # validate password length
    @validates_schema
    def validate_password(self, data):
        if len(data['password']) != 8:
            raise ValidationError('Please enter a valid password - must be exactly 8 characters.')
    

owner_schema = OwnerSchema()
owners_schema = OwnerSchema(many=True) 