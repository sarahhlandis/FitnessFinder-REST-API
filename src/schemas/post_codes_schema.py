from marshmallow import fields
from app import ma
from models.post_codes import PostCode
from marshmallow import validates_schema, validate, ValidationError
from marshmallow.fields import Length

class PostCodeSchema(ma.Schema):
    class Meta:
        # Define the fields to expose
        fields = ("id", "post_code")

        load_only = ["id"]
    
    post_code = fields.String(required=True, validate=[Length(equal=4), validate.Regexp('^\d+$')])

    @validates_schema
    def validate_post_code(self, data):
        if len(data['post_code']) != 4:
            raise ValidationError('Please reenter a valid 4-digit postcode.')
        
postcode_schema = PostCodeSchema()
postcodes_schema = PostCodeSchema(many=True) 