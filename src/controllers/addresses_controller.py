from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models.facilities import Facility
from schemas.facilities_schema import facilities_schema, facility_schema
from schemas.addresses_schema import address_schema
from schemas.post_codes_schema import postcode_schema
from utilities import *
from app import db


addresses = Blueprint('addresses', __name__, url_prefix='/addresses')


# an address cannot be deleted as it is mandatory for a facility. an address cannot be added
# without having a post_code so no functionality required to add it at a later date

# 1
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
    address_fields = address_schema.load(request.json, partial=True)

    # update the address details with the loaded data
    facility.address.street_num = address_fields.get('street_num', facility.address.street_num)
    facility.address.street = address_fields.get('street', facility.address.street)
    facility.address.suburb = address_fields.get('suburb', facility.address.suburb)
    facility.address.state = address_fields.get('state', facility.address.state)

    # validate the post code and retrieve the post code ID
    post_code = address_fields.get('post_code', '')
    if post_code:
        # validate the post code and retrieve the post code ID
        post_code_data = postcode_schema.load({'post_code': post_code})
        post_code_id = post_code_data['id']
        facility.address.post_code_id = post_code_id

    # commit changes to database
    db.session.commit()

    result = facility_schema.dump(facility)
    return jsonify(result)




# 2
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

    result = address_schema.dump(address)

    return jsonify(result)
