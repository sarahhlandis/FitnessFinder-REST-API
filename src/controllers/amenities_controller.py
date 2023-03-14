from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.facilities import Facility
from models.amenities import Amenity
from schemas.facilities_schema import facilities_schema, facility_schema
from schemas.amenities_schema import amenities_schema, amenity_schema
from utilities import *

facility_amenities = Blueprint('facility_amenities', __name__, url_prefix='/facilities_amenities')

# owners cannot create new amenities - these are prepopulated into the database 
# therefore there is no functionality use for creation of amenity


@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['PUT'])
@jwt_required()
def update_facility_amenities(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being updated
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error
    
    facility = Facility.query.get_or_404(facility_id)

    # get the amenities selected by the owner
    selected_amenities = request.json.get('amenities', [])

    # remove all current amenities associated with the facility
    for facility_amenity in facility.facility_amenities:
        db.session.delete(facility_amenity)

    # add selected amenities to facility_amenities table
    for amenity_name in selected_amenities:
        amenity = Amenity.query.filter_by(name=amenity_name).first()
        if amenity:
            facility_amenity = facility_amenities(facility_id=facility.id, amenity_id=amenity.id, has_amenity=True)
            db.session.add(facility_amenity)

    db.session.commit()

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
            # remove the FacilityAmenities object from the database
            facility_amenity = facility_amenities.query.filter_by(facility_id=facility_id, amenity_id=amenity.id).first()
            db.session.delete(facility_amenity)
            # remove the amenity from the list of amenities associated with the facility
            facility.amenities.remove(amenity)

    db.session.commit()

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
    amenities = [amenity for amenity in facility.amenities if amenity.has_amenity]

    result = amenities_schema.dump(amenities)

    return jsonify(result)