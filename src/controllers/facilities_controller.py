from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from schemas.facilities_schema import facility_schema, facilities_schema
from schemas.owners_schema import owner_schema, owners_schema
from schemas.facility_amenities_schema import facilityamenities_schema, facilityamenity_schema
from schemas.promotions_schema import promotion_schema, promotions_schema
from schemas.addresses_schema import address_schema, addresses_schema
from models.addresses import Address
from models.facilities import Facility
from models.facility_types import FacilityType
from models.owners import Owner
# from models.facility_amenities import FacilityAmenity
from models.promotions import Promotion
from models.post_codes import PostCode
from utilities import *

facilities = Blueprint('facilities', __name__, url_prefix="/facilities")
facility_amenities = Blueprint('facility_amenities', __name__, url_prefix='/facilities_amenities')


# retrieve a list of all facilities owned by logged-in owner
@facilities.route('/secure', methods=["GET"])
@jwt_required()
def facilities_list():
    # get owner id from access token
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(None, owner_id)
    if access_error:
        return access_error

    # retrieve all facilities associated with the owner id
    facilities = Facility.query.filter_by(owner_id=owner_id).all()

    # serialize the facilities using FacilitySchema
    result = facilities_schema.dump(facilities)

    # return the serialized facilities
    return jsonify(result)




# retrieve a specific facility of a logged-in owner
@facilities.route('/<int:facility_id>/secure', methods=['GET'])
@jwt_required()
def get_owned_facility(facility_id):
    # get owner id from access token
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error
    
    facility = Facility.query.get_or_404(facility_id)

    # serialize the facility
    result = facility_schema.dump(facility)
    return jsonify(result)




# create a new facility for logged-in owner (with or without existing owned facility)
@facilities.route('/secure', methods=['POST'])
@jwt_required()
def create_facility():
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(None, owner_id)
    if access_error:
        return access_error

    # deserialize the request data using FacilitySchema
    facility_fields = facility_schema.load(request.json)

    # deserialize the address field using AddressSchema
    address_fields = address_schema.load(request.json['address'])

    # check if a PostCode object with the provided postcode already exists
    postcode_value = request.json['address']['post_code']['postcode']
    post_code = PostCode.query.filter_by(postcode=postcode_value).first()
    if post_code:
        # if it does, assign its id to the post_code_id field of the newly created Address object
        address_fields['post_code_id'] = post_code.id
    else:
        # if it doesn't, create a new PostCode object with the provided postcode value,
        # assign its id to the post_code_id field of the newly created Address object,
        # and add the new PostCode object to the database
        post_code = PostCode(postcode=postcode_value)
        db.session.add(post_code)
        db.session.flush()  # this will generate the id for the new PostCode object
        address_fields['post_code_id'] = post_code.id


    # merge the deserialized address fields into the facility fields
    facility_fields['address'] = address_fields

    # create a new Facility object with the deserialized data
    facility = Facility(**facility_fields, owner_id=owner_id)

    # add the new Facility object to the database and commit the transaction
    db.session.add(facility)
    db.session.commit()

    # retrieve a list of all facility_types and their IDs
    facility_types = FacilityType.query.all()
    for facility_type in facility_types:
        print(f"Facility Type ID: {facility_type.id} | Name: {facility_type.name}")

    # add facility type to facility object
    facility_type_id = request.json.get('facility_type_id')
    if facility_type_id:
        # validate facility type ID against prepopulated list
        valid_facility_types = [f.id for f in facility_types]
        if facility_type_id not in valid_facility_types:
            return jsonify({'error': 'Invalid facility type ID'}), 400
        facility.facility_type_id = facility_type_id

    # create new amenities for the facility
    if 'amenities' in request.json:
        for amenity_data in request.json['amenities']:
            facility_amenity_fields = facilityamenity_schema.load(amenity_data)
            facility_amenity = Facility.facility_amenities(**facility_amenity_fields, facility_id=facility.id)
            db.session.add(facility_amenity)
        db.session.commit()

    # create new promotions for the facility
    if 'promotions' in request.json:
        for promotion_data in request.json['promotions']:
            promotion_fields = promotion_schema.load(promotion_data)
            promotion = Promotion(**promotion_fields, facility_id=facility.id)
            db.session.add(promotion)
        db.session.commit()

    # serialize the new Facility object using FacilitySchema
    result = facility_schema.dump(facility)

    # return the serialized new Facility object
    return jsonify(result), 201




# deletion of specific facility unless owner only has 1 facility, in which case, must delete account
@facilities.route('/<int:facility_id>/secure', methods=['DELETE'])
@jwt_required()
def delete_facility(facility_id):
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error
    
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



# # update a specific facility of a logged-in owner
# @facilities.route('/<int:facility_id>/secure', methods=['PUT'])
# @jwt_required()
# def update_owned_facility(facility_id):
#     owner_id = get_jwt_identity()

#     # verify that the owner_id in the request matches the owner_id of the facility being updated
#     if not verify_owner_access(owner_id, facility.owner_id):
#         return jsonify({'message': 'Unauthorized access to update facility'}), 401

#     # retrieve facility from the database
#     facility = Facility.query.get_or_404(facility_id)

#     # load and validate the request data using FacilitySchema
#     facility_fields = facility_schema.load(request.json)

#     # update the facility object with the validated data
#     facility.business_name = facility_fields['business_name']
#     facility.hours_of_op = facility_fields['hours_of_op']
#     facility.address = facility_fields['address']
#     facility.phone_num = facility_fields['phone_num']

#     db.session.commit()
#     result = facility_schema.dump(facility)
#     return jsonify(result)



# update a specific facility of a logged-in owner
@facilities.route('/<int:facility_id>/secure', methods=['PUT'])
@jwt_required()
def update_owned_facility(facility_id):
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error

    # retrieve facility from the database
    facility = Facility.query.get_or_404(facility_id)

    # load and validate the request data using FacilitySchema
    facility_fields = facility_schema.load(request.json)

    # update the facility object with the validated data
    facility.business_name = facility_fields['business_name']
    facility.opening_time = facility_fields['opening_time']
    facility.closing_time = facility_fields['closing_time']
    facility.address = facility_fields['address']
    facility.phone_num = facility_fields['phone_num']

    # update address
    address_fields = address_schema.load(request.json['address'])
    facility.address.street_num = address_fields['street_num']
    facility.address.street = address_fields['street']
    facility.address.suburb = address_fields['suburb']
    facility.address.state = address_fields['state']

    # update address post code
    if 'post_code' in request.json['address']:
        post_code_value = request.json['address']['post_code']['postcode']
        post_code = PostCode.query.filter_by(postcode=post_code_value).first()
        if post_code:
            # if it does, assign its id to the post_code_id field of the existing Address object
            facility.address.post_code_id = post_code.id
        else:
            # if it doesn't, create a new PostCode object with the provided postcode value,
            # assign its id to the post_code_id field of the existing Address object,
            # and add the new PostCode object to the database
            post_code = PostCode(postcode=post_code_value)
            db.session.add(post_code)
            db.session.flush()  # this will generate the id for the new PostCode object
            facility.address.post_code_id = post_code.id

    # retrieve a list of all facility_types and their IDs
    facility_types = FacilityType.query.all()

    # update facility type to facility object
    facility_type_id = request.json.get('facility_type_id')
    if facility_type_id:
        # validate facility type ID against prepopulated list
        valid_facility_types = [f.id for f in facility_types]
    if facility_type_id not in valid_facility_types:
        return jsonify({'error': 'Invalid facility type ID'}), 400
    facility.facility_type_id = facility_type_id

    # update amenities
    if 'amenities' in request.json:
        amenities, errors = facilityamenities_schema.load(request.json['amenities'])
        if errors:
            return jsonify(errors), 422
        facility.amenities = amenities

    # update promotions
    if 'promotions' in request.json:
        promotions, errors = promotions_schema.load(request.json['promotions'])
        if errors:
            return jsonify(errors), 422
        facility.promotions = promotions

    db.session.commit()
    result = facility_schema.dump(facility)
    return jsonify(result)


