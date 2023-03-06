from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.facilities import Facility
from schemas.facilities_schema import FacilitySchema

facilities = Blueprint('facilities', __name__, url_prefix="/facilities")

# retrieve associated facilities for an existing owner
@facilities.route("", methods=["GET"])
@jwt_required()
def facilities_list():
    # get owner id from access token
    owner_id = get_jwt_identity()

    # retrieve all facilities associated with the owner id
    facilities = Facility.query.filter_by(owner_id=owner_id).all()

    # serialize the facilities using FacilitySchema
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)

    # return the serialized facilities
    return jsonify(result)

# create facility associated with existing owner
@facilities.route("", methods=["POST"])
@jwt_required()
def facilities_create():
    # get the owner id from the access token
    owner_id = get_jwt_identity()

    # deserialize the request data using FacilitySchema
    facility_schema = FacilitySchema()
    facility_fields = facility_schema.load(request.json)

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

