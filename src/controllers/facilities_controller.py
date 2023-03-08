from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from schemas.facilities_schema import facility_schema, FacilitySchema
from schemas.owners_schema import Owner
from models.facilities import Facility, facilities, facility_schema, facilities_schema
from models.owners import Owner
from models.amenities import Amenity


# get a list of all facilities owned by logged-in owner
@facilities.route('/secure', methods=["GET"])
@jwt_required()
def facilities_list():
    # get owner id from access token
    owner_id = get_jwt_identity()

    # retrieve the owner object using the owner id
    owner = Owner.query.get_or_404(owner_id)

    # retrieve all facilities associated with the owner id
    facilities = Facility.query.filter_by(owner_id=owner_id).all()

    # check if each facility in the retrieved facilities list has the same owner as the current logged in owner
    for facility in facilities:
        if facility.owner != owner:
            return jsonify({'message': 'Unauthorized access to facilities'}), 401

    # serialize the facilities using FacilitySchema
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)

    # return the serialized facilities
    return jsonify(result)




# Retrieve a specific facility of a logged-in owner
@facilities.route('/<int:facility_id>/secure', methods=['GET'])
@jwt_required()
def get_owned_facility(facility_id):
    owner_id = get_jwt_identity()
    owner = Owner.query.get_or_404(owner_id)
    facility = Facility.query.get_or_404(facility_id)
    if facility.owner_id != owner_id:
        return jsonify({'message': 'Facility not owned by the specified owner'}), 400
    result = facility_schema.dump(facility)
    return jsonify(result)




# create facility associated with existing owner, or create for a new owner
@facilities.route('/new_facility/secure', methods=["POST"])
@jwt_required()
def facilities_create():
    # get the owner id from the access token
    owner_id = get_jwt_identity()

    # retrieve the owner from the database
    owner = Owner.query.filter_by(id=owner_id).first()

    # deserialize the request data using FacilitySchema
    facility_schema = FacilitySchema()
    facility_fields = facility_schema.load(request.json)

    # check if the owner already owns at least one facility
    if owner.facility is not None:
        # verify that the owner_id in the request matches the owner_id of the facility being created
        if facility_fields["owner_id"] != owner_id:
            return jsonify({'message': 'Unauthorized access to create facility for another owner'}), 401

        # create a new Facility object with the deserialized data
        facility = Facility(**facility_fields)

        # add the new Facility object to the database and commit the transaction
        db.session.add(facility)
        db.session.commit()

        # serialize the new Facility object using FacilitySchema
        result = facility_schema.dump(facility)

        # return the serialized new Facility object
        return jsonify(result)
    else:
        # set the owner id to the authenticated owner id
        facility_fields["owner_id"] = owner_id

        # create a new Facility object with the deserialized data
        facility = Facility(**facility_fields)

        # add the new Facility object to the database and commit the transaction
        db.session.add(facility)
        db.session.commit()

        # serialize the new Facility object using FacilitySchema
        result = facility_schema.dump(facility)

        # return the serialized new Facility object
        return jsonify(result)



# deletion of specific facility unless owner only has 1 facility, in which case, must delete account
@facilities.route('/<int:facility_id>/secure', methods=['DELETE'])
@jwt_required()
def delete_facility(facility_id):
    owner_id = get_jwt_identity()
    facility = Facility.query.get(facility_id)

    if facility is None:
        return jsonify({'error': 'Facility not found'}), 404

    if facility.owner_id != owner_id:
        return jsonify({'error': 'You are not authorized to delete this facility'}), 403

    # Count the number of facilities associated with the owner's account
    num_facilities = Facility.query.filter_by(owner_id=owner_id).count()

    if num_facilities > 1:
        # Allow the owner to delete a specific facility
        db.session.delete(facility)
        db.session.commit()
        return jsonify({'message': 'Facility deleted successfully'}), 200
    elif num_facilities == 1:
        # Delete the owner's account if it has only one facility
        owner = Owner.query.get(owner_id)
        if owner is None:
            return jsonify({'error': 'Owner not found'}), 404
        db.session.delete(owner)
        db.session.delete(facility)
        db.session.commit()
        return jsonify({'message': 'Account and Facility deleted successfully'}), 200
    else:
        # Error case, owner has no facility
        return jsonify({'error': 'You have no facility associated with your account'}), 400




# Update a specific owned facility for a logged-in owner
@facilities.route('/<int:facility_id>/secure', methods=['PUT'])
@jwt_required()
def update_owned_facility(facility_id):
    owner_id = get_jwt_identity()
    owner = Owner.query.get_or_404(owner_id)
    facility = Facility.query.get_or_404(facility_id)
    if facility.owner_id != owner.id:
        return jsonify({'message': 'Facility not owned by the specified owner'}), 400
    
    # Load and validate the request data using FacilitySchema
    facility_schema = FacilitySchema()
    facility_fields = facility_schema.load(request.json)

    # Update the facility object with the validated data
    facility.business_name = facility_fields['business_name']
    facility.hours_of_op = facility_fields['hours_of_op']
    facility.address = facility_fields['address']
    facility.phone_num = facility_fields['phone_num']
    
    db.session.commit()
    result = facility_schema.dump(facility)
    return jsonify(result)



# update amenities respective to owned facility for logged-in owner
@facilities.route('/<int:facility_id>/amenities', methods=['PUT'])
@jwt_required()
def update_facility_amenities(facility_id):
    owner_id = get_jwt_identity()
    facility = Facility.query.get_or_404(facility_id)

    # check if the user is the owner of the facility
    if owner_id != facility.owner_id:
        return jsonify({'error': 'Unauthorized access'}), 401

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

