from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models.facilities import Facility
from schemas.post_codes_schema import PostCodeSchema
from schemas.addresses_schema import AddressSchema
from schemas.facilities import FacilitySchema
from utilities import *
from app import db, addresses


addresses = Blueprint('addresses', __name__, url_prefix='/addresses')


# an address cannot be deleted as it is mandatory for a facility. an address cannot be added
# without having a post_code so no functionality required to add it at a later date


# update an address for a singular facility by a logged-in owner
@addresses.route('/<int:facility_id>/secure', methods=['PUT'])
@jwt_required()
def update_facility_address(facility_id):
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error

    # retrieve facility from the database
    facility = Facility.query.get_or_404(facility_id)

    # load and validate the request data using AddressSchema
    address_schema = AddressSchema()
    address_fields = address_schema.load(request.json)

    # validate the post code and retrieve the post code ID
    # handle the case where no post code is provided in the request
    address_fields['post_code'] = address_fields.get('post_code', '')
    # set the initial value of the post code ID to None
    address_fields['post_code_id'] = None
    if address_fields['post_code']:
        # validate the post code and retrieve the post code ID
        post_code_schema = PostCodeSchema(only=('post_code',))
        post_code_data = post_code_schema.load({'post_code': address_fields['post_code']})
        post_code_id = post_code_data['id']
        address_fields['post_code_id'] = post_code_id

    # update the facility object with the validated data
    facility.address.street_num = address_fields['street_num']
    facility.address.street = address_fields['street']
    facility.address.suburb = address_fields['suburb']
    facility.address.state = address_fields['state']
    facility.address.post_code_id = address_fields['post_code_id']

    db.session.commit()

    facility_schema = FacilitySchema()
    result = facility_schema.dump(facility)
    return jsonify(result)




# retrieve a single address for a specified facility by a logged-in owner
@addresses.route('/<int:facility_id>/secure', methods=['GET'])
@jwt_required()
def get_address(facility_id):
    owner_id = get_jwt_identity()

    # verify that the owner_id in the request matches the owner_id of the facility being retrieved
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error

    # retrieve the facility and its associated address
    facility = Facility.query.get_or_404(facility_id)
    address = facility.address

    address_schema = AddressSchema()
    result = address_schema.dump(address)

    return jsonify(result)
