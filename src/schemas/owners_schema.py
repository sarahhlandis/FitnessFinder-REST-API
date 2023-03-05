from marshmallow import fields, validate, validates_schema, ValidationError
from flask_marshmallow import Marshmallow
from marshmallow.validate import Length
from models import Owner
from sqlalchemy import orm

ma = Marshmallow()

class OwnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Owner

    id = fields.Integer(dump_only=True)
    # load only so pw doesnt not get output
    password = fields.String(required=True, load_only=True, validate=Length(min=8, max=15))
    email = fields.Email(required=True, validate=validate.Email())
    mobile = fields.String(required=True, validate=[Length(equal=10), validate.Regexp('^\d+$')])
    # exclude owner to avoid circ ref
    facilities = fields.Nested('FacilitySchema', many=True, exclude=('owner',)) 

    @validates_schema
    def validate_mobile(self, data):
        if len(data['mobile']) != 10:
            raise ValidationError('Phone number must be 10 digits long. Please try again.')
        
    @validates_schema
    def validate_password(self, data):
        if len(data['password']) < 8 or len(data['password']) > 15:
            raise ValidationError('Please enter a valid password - must be between 8 and 15 characters.')
    