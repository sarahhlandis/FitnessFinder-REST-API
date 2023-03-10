from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db, facility_amenities
from models.facilities import Facility
from models.amenities import Amenity
from schemas.facilities import FacilitySchema
from schemas.amenities_schema import AmenitySchema
from utilities import *

# owners cannot create new amenities - these are prepopulated into the database 
# therefore there is no functionality use for creation of amenity


# update only amenities respective to owned facility for logged-in owner
@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['PUT'])
@jwt_required()
def update_facility_amenities(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being updated
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error
    
    facility = Facility.query.get_or_404(facility_id)

    # create dictionary with all possible amenities
    amenities = { 
        'parking': False, 
        'pool': False,
        'sauna': False,
        'steam_room': False,
        'fuel_bar': False,    
        'pilates': False,
        'boxing': False,
        'yoga': False,
        'private_training': False,
        'lockers': False,
        'showers': False
    }

    # get the amenities selected by the owner
    selected_amenities = request.json.get('amenities', [])

    # update the dictionary with the selected amenities
    for amenity_name in selected_amenities:
        if amenity_name in amenities:
            amenities[amenity_name] = True

    # use the amenities dictionary to update the facility_amenities table
    for amenity_name, amenity_value in amenities.items():
        amenity = Amenity.query.filter_by(name=amenity_name).first()
        if amenity:
            if amenity_value and amenity not in facility.amenities:
                facility.amenities.append(amenity)
            elif not amenity_value and amenity in facility.amenities:
                facility.amenities.remove(amenity)


    db.session.commit()

    facility_schema = FacilitySchema()
    result = facility_schema.dump(facility)
    return jsonify(result)



# delete selected amenities from a specific facility by a logged-in owner
@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['DELETE'])
@jwt_required()
def delete_facility_amenities(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being updated
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error
    
    facility = Facility.query.get_or_404(facility_id)

    # get the amenities selected by the owner
    selected_amenities = request.json.get('amenities', [])

    # remove the selected amenities from the facility_amenities table
    for amenity_name in selected_amenities:
        amenity = Amenity.query.filter_by(name=amenity_name).first()
        if amenity and amenity in facility.amenities:
            facility.amenities.remove(amenity)

    db.session.commit()
    
    facility_schema = FacilitySchema()
    result = facility_schema.dump(facility)
    return jsonify(result)





# retrieve all amenities for a specified facility by a logged-in owner
@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['GET'])
@jwt_required()
def get_facility_amenities(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being retrieved
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error

    facility = Facility.query.get_or_404(facility_id)

    # use defined SQLAlchemy relationship to get the amenities associated with the facility
    amenities = facility.amenities.all()

    amenity_schema = AmenitySchema(many=True)
    result = amenity_schema.dump(amenities)

    return jsonify(result)
