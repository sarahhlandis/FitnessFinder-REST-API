from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.facilities import Facility
from schemas.facilities_schema import FacilitySchema
from schemas.owners_schema import Owner
from app import facilities

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

# create facility associated with existing owner, or create for a new owner
@facilities.route("", methods=["POST"])
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
    if owner.facilities:
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
    else:
        # if the owner does not already own a facility
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

@facilities.route("/<int:facility_id>", methods=["DELETE"])
@jwt_required()
def facilities_delete(facility_id):
    # get owner id from access token
    owner_id = get_jwt_identity()

    # retrieve the facility with the given id
    facility = Facility.query.get(facility_id)

    # check if facility exists
    if not facility:
        return jsonify({"message": "Facility not found"}), 404

    # check if logged-in owner is the owner of the facility
    if facility.owner_id != owner_id:
        return jsonify({"message": "You are not authorized to delete this facility."}), 401

    # delete the facility from the database and commit the transaction
    db.session.delete(facility)
    db.session.commit()

    return jsonify({"message": "Facility deleted successfully"}), 200
