from app import ma, db
from models.addresses import Address
from models.post_codes import PostCode
from marshmallow import fields, validates_schema, validate, ValidationError, Length
from schemas.post_codes_schema import PostCodeSchema


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        include_fk = True
    
    id = fields.Integer(dump_only=True)
    street_num = fields.Integer(required=True, validate=validate.Regexp('^\d+$'))
    street = fields.String(required=True)
    suburb = fields.String(required=True)
    state = fields.String(required=True, validate=Length(equal=3))
    post_code_id = fields.Integer()

    # foreign keys below
    post_code = fields.Nested(PostCodeSchema)

    # validates the state is formatted correctly
    @validates_schema
    def validate_state(self, data):
        if len(data['state']) != 3:
            raise ValidationError('Please enter the state abbreviation (e.g. VIC, NSW, etc.)')

        
    @validates_schema
    def validate_post_code_id(self, data):
        post_code = data.get('post_code')
        if post_code:
            # looks for the entered post_code in the post_codes table and retrieves first match
            existing_post_code = PostCode.query.filter_by(post_code=post_code).first()
            # if the post_code exists, retrieve post_code id and assign to this address entry
            if existing_post_code:
                data['post_code_id'] = existing_post_code.id
            # otherwise, add the new post code to the post_code table in the db
            # retrieve the new post_code id from the post_codes table
            # assign the new post_code_id to the new address entry
            else:
                new_post_code = PostCode(post_code=post_code)
                db.session.add(new_post_code)
                # makes sure the new post code is added to the database before getting its id
                db.session.flush()  
                data['post_code_id'] = new_post_code.id
            
    