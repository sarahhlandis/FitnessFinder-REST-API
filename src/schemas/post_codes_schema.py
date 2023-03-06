from marshmallow import fields
from app import ma
from models.post_codes import PostCode
from marshmallow import validates_schema, validate, ValidationError, Length

class PostCodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PostCode
    
    id = fields.Integer(dump_only=True)
    post_code = fields.String(required=True, validate=[Length(equal=4), validate.Regexp('^\d+$')])

    @validates_schema
    def validate_post_code(self, data):
        if len(data['post_code']) != 4:
            raise ValidationError('Please reenter a valid 4-digit postcode.')