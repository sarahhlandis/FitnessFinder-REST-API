from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError, EXCLUDE
from app import db
from utilities import *
from models.facilities import Facility
from models.promotions import Promotion
from schemas.promotions_schema import promotion_schema, promotions_schema


promotions = Blueprint('promotions', __name__, url_prefix='/promotions')

# 1
# create a new promotion
@promotions.route('/<int:facility_id>/secure', methods=['POST'])
@jwt_required()
def create_promotion(facility_id):
    owner_id = get_jwt_identity()

    # verify access
    access_check = verify_owner_access(facility_id, owner_id)
    if access_check:
        return access_check

    # Deserialize the request data using PromotionSchema
    # promotion_fields = promotion_schema.load(request.json)
    promotion_fields = promotion_schema.load(request.json)

    try:
        # Validate the dates using the `validate_dates` method in the schema
        promotion_schema.validate(promotion_fields)
    except ValidationError as e:
        return jsonify(e.messages), 400

    # Set the facility_id to the provided facility_id
    promotion_fields["facility_id"] = facility_id

    # Create a new Promotion object with the deserialized data
    promotion = Promotion(**promotion_fields)

    # Add the new Promotion object to the database and commit the transaction
    db.session.add(promotion)
    db.session.commit()

    # Serialize the new Promotion object using PromotionSchema
    result = promotion_schema.dump(promotion)

    # Return the serialized new Promotion object
    return jsonify(result), 201




# 2
# update a promotion for a specific facility of a logged-in owner
@promotions.route('/<int:facility_id>/<int:promotion_id>/secure', methods=['PUT'])
@jwt_required()
def update_facility_promotion(facility_id, promotion_id):
    # get owner id from access token
    owner_id = get_jwt_identity()

    # verify access
    access_error = verify_owner_access(facility_id, owner_id)
    if access_error:
        return access_error

    # retrieve promotion from the database
    promotion = Promotion.query.get_or_404(promotion_id)

    # load and validate the request data using FacilitySchema
    promotion_fields = promotion_schema.load(request.json)

    # update the facility object with the validated data
    promotion.name = promotion_fields['name']
    promotion.start_date = promotion_fields['start_date']
    promotion.end_date = promotion_fields['end_date']
    promotion.discount = promotion_fields['discount_percent']

    db.session.commit()
    result = promotion_schema.dump(promotion)
    return jsonify(result)



# 3
# delete a single promotion for a selected facility by a logged-in owner
@promotions.route('/<int:promotion_id>/secure', methods=['DELETE'])
@jwt_required()
def delete_promotion(promotion_id):
    owner_id = get_jwt_identity()

    promotion = Promotion.query.get(promotion_id)
    
    # verify access
    access_check = verify_owner_access(promotion.facility_id, owner_id)
    if access_check:
        return access_check


    db.session.delete(promotion)
    db.session.commit()
    return jsonify({'message': 'Promotion deleted successfully'}), 200


