from app import ma
from marshmallow import fields

class AmenitySchema(ma.Schema):
    class Meta:
        ordered = True
        # Define the fields to expose
        fields = ("id", "parking", "pool", "sauna", "steam_room", 
                  "fuel_bar", "pilates", "boxing", "yoga", "private_training", 
                  "lockers", "showers")
    
    
amenity_schema = AmenitySchema()
amenities_schema = AmenitySchema(many=True) 