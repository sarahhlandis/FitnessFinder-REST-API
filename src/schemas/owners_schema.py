from marshmallow import fields
from flask_marshmallow import Marshmallow
from marshmallow.validate import Length
from models import Owner

ma = Marshmallow()

class OwnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Owner

    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    # load only so pw doesnt not get output
    password = fields.String(required=True, load_only=True, validate=Length(min=8, max=15))
    email = fields.Email(required=True)
    mobile = fields.String(required=True)
    # exclude owner to avoid circ ref
    facilities = fields.Nested('FacilitySchema', many=True, exclude=('owner',)) 