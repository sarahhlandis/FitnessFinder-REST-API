from app import ma

class AmenitySchema(ma.Schema):
    class Meta:
        ordered = True
        # Define the fields to expose
        fields = ("id", "name", "parking", "pool", "sauna", "steam_room", 
                  "fuel_bar", "pilates", "boxing", "yoga", "private_training", 
                  "lockers", "showers")
    
        dump_only = ("id",)


amenity_schema = AmenitySchema()
amenities_schema = AmenitySchema(many=True) 