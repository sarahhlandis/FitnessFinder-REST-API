from flask import jsonify
from models.facilities import Facility
from schemas.facilities import FacilitySchema
from models.facility_amenities import FacilityAmenity
from models.promotions import Promotion
from models.amenities import Amenity
from models.addresses import Address
from app import public
from sqlalchemy import desc
from datetime import datetime

# query facilities based on post_code
# returns all facilities with specified post_code will be returned
@public.route('/facilities/postcode/<string:post_code>', methods=['GET'])
def get_facilities_by_postcode(post_code):
    facilities = Facility.query.filter_by(post_code=post_code).all()
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)
    return jsonify(result)





# query facilities based on promotion end date
# returns all facilities with running promotions that have not yet expired from day of query
@public.route('/facilities/promotions/current', methods=['GET'])
def get_upcoming_promotions():
    current_time = datetime.now()
    facilities = Facility.query.filter(Facility.promotions.any(Promotion.end_date >= current_time)).order_by(Promotion.end_date).all()
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)
    return jsonify(result)




# query facilities based on facility_type
# returns all facilities that are classed as specified facility type
@public.route('/facilities/type/<string:facility_type>', methods=['GET'])
def get_facilities_by_type(facility_type):
    facilities = Facility.query.filter_by(facility_type=facility_type).all()
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)
    return jsonify(result)




# query facilities based on an amenity list
# returns all facilities that have the specified amenities
@public.route('/amenities/<string:amenity_ids>', methods=['GET'])
def get_facilities_by_amenities(amenity_ids):
    # convert comma-separated string of amenity IDs to a list of integers
    amenity_ids = [int(amenity_id) for amenity_id in amenity_ids.split(',')]

    # query facilities that have the selected amenities
    facilities = Facility.query.filter(Facility.amenities.any(Amenity.id.in_(amenity_ids))).all()

    # serialize the facilities data using FacilitySchema
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)

    return jsonify(result)



# query all facilities of a specific type that are open for certain hours
@public.route('/facilities/<string:facility_type>/hours/<string:hours_of_op>', methods=['GET'])
def get_facilities_open_hours(facility_type, hours_of_op):
    facilities = Facility.query.filter_by(facility_type=facility_type, hours_of_op=hours_of_op).all()
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)
    return jsonify(result)





# query all facilities in a specified post_code that have the specified amenities
# returns all facilities within post_code and also have desired amenities
@public.route('/facilities/postcode/<string:post_code>/amenities/<string:amenity_ids>', methods=['GET'])
def local_facilities_with_amenities(post_code, amenity_ids):
    # Split comma-separated amenity IDs into a list
    amenity_ids_list = amenity_ids.split(',')
    
    # Query facilities with matching postcode and amenities
    facilities = Facility.query \
        .join(Facility.address) \
        .join(Facility.amenities) \
        .filter(Address.post_code == post_code, FacilityAmenity.id.in_(amenity_ids_list)) \
        .all()
    
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)
    return jsonify(result)




# query all facilities that are running promotions in a specified post_code
# returns all facilities within post_code that are also running promotions
@public.route('/facilities/postcode/<string:post_code>/promotions', methods=['GET'])
def local_with_promotions(post_code):
    # Query facilities with matching postcode and active promotions
    facilities = Facility.query \
        .join(Facility.address) \
        .join(Facility.promotions) \
        .filter(Address.post_code == post_code, Promotion.start_date <= datetime.now(), Promotion.end_date >= datetime.now()) \
        .all()
    
    facility_schema = FacilitySchema(many=True)
    result = facility_schema.dump(facilities)
    return jsonify(result)
