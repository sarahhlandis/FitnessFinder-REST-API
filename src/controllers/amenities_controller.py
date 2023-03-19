from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from sqlalchemy import text, Table, delete, insert, select
from models.facilities import Facility, facility_amenities
from models.amenities import Amenity
from schemas.facilities_schema import facilities_schema, facility_schema
from schemas.amenities_schema import amenities_schema, amenity_schema
from utilities import *

facility_amens = Blueprint('facility_amenities', __name__, url_prefix='/facility_amens')
amenities = Blueprint('amenities', __name__, url_prefix='/amenities')

# owners cannot create new amenities - these are prepopulated into the database 
# therefore there is no functionality use for creation of amenity


# 1
# retrieve all amenities for a specified facility by a logged-in owner
@facility_amens.route('/<int:facility_id>/amenities/secure', methods=['GET'])
@jwt_required()
def get_facility_amenities(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being retrieved
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error

    facility = Facility.query.get_or_404(facility_id)

    # retrieve the amenities associated with the facility
    amenities = facility.amenities

    result = amenities_schema.dump(amenities)

    return jsonify(result)




# 2
# add/remove (update) amenities for a specific facility by a logged-in owner
@facility_amens.route('/<int:facility_id>/amenities/secure', methods=['PUT', 'DELETE'])
@jwt_required()
def update_facility_amenities(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being updated
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error
    
    facility = Facility.query.get_or_404(facility_id)

    if request.method == 'DELETE':
        # remove selected amenities from facility_amenities table
        selected_amenities = request.json.get('amenities', [])

        if selected_amenities:
            facility_amenities_table = Table('facility_amenities', db.metadata, autoload=True, autoload_with=db.engine)

            for amenity_name in selected_amenities:
                amenity = Amenity.query.filter_by(name=amenity_name).first()
                if amenity:
                    db.session.execute(delete(facility_amenities_table).where(facility_amenities_table.c.facility_id == facility.id).where(facility_amenities_table.c.amenity_id == amenity.id))

        db.session.commit()

        result = facility_schema.dump(facility)
        return jsonify(result, {'message': 'Amenities removed successfully!'})

    elif request.method == 'PUT':
        # add selected amenities to facility_amenities table
        selected_amenities = request.json.get('amenities', [])

        if selected_amenities:
            facility_amenities_table = Table('facility_amenities', db.metadata, autoload=True, autoload_with=db.engine)

            # remove all current amenities associated with the facility
            db.session.execute(delete(facility_amenities_table).where(facility_amenities_table.c.facility_id == facility.id))

            # add selected amenities
            amenities_to_add = []
            for amenity_name in selected_amenities:
                amenity = Amenity.query.filter_by(name=amenity_name).first()
                if amenity:
                    amenities_to_add.append({'facility_id': facility.id, 'amenity_id': amenity.id, 'has_amenity': True})
            
            if amenities_to_add:
                db.session.execute(insert(facility_amenities_table), amenities_to_add)

        db.session.commit()

        result = facility_schema.dump(facility)
        return jsonify(result, {'message': 'Amenities added successfully!'})




# 3
# retrieve all amenities and their id assignments
@amenities.route('/all_amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.all()
    amenities_dict = {}
    for amenity in amenities:
        amenities_dict[amenity.id] = amenity.name
    return jsonify(amenities_dict)
