from marshmallow import fields
from app import ma
from models.amenities import Amenity

class AmenitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Amenity
    
    id = fields.Integer(dump_only=True)
    parking = fields.Boolean(required=False)
    pool = fields.Boolean(required=False)
    sauna = fields.Boolean(required=False)
    steam_room = fields.Boolean(required=False)
    fuel_bar = fields.Boolean(required=False)
    pilates = fields.Boolean(required=False)
    boxing = fields.Boolean(required=False)
    yoga = fields.Boolean(required=False)
    private_training = fields.Boolean(required=False)
    lockers = fields.Boolean(required=False)
    showers = fields.Boolean(required=False)
    
