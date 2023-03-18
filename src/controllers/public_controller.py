from flask import jsonify, Blueprint
from models.facilities import Facility
from schemas.facilities_schema import facilities_schema
# from models.facility_amenities import FacilityAmenity
from models.facility_types import FacilityType
from models.promotions import Promotion
from models.amenities import Amenity
from models.addresses import Address
from models.post_codes import PostCode
from models.facilities import facility_amenities
from sqlalchemy import cast, String, text, and_
from sqlalchemy.orm import joinedload, subqueryload
from sqlalchemy.sql import exists
from datetime import datetime
from app import db

public = Blueprint('public', __name__, url_prefix='/public')

# 1
# query facilities based on post_code
# returns all facilities with specified post_code will be returned
@public.route('/facilities/postcode/<string:post_code>', methods=['GET'])
def get_facilities_by_postcode(post_code):
    facilities = db.session.query(Facility).join(Address).join(PostCode).filter(PostCode.post_code == post_code).all()
    result = facilities_schema.dump(facilities)
    return jsonify(result)




# 2
# query facilities based on promotion end date
# returns all facilities with running promotions that have not yet expired from day of query
@public.route('/facilities/promotions/current', methods=['GET'])
def get_upcoming_promotions():
    current_time = datetime.now()
    facilities = Facility.query.join(Promotion).filter(Promotion.end_date >= current_time).order_by(Promotion.end_date).all()
    result = facilities_schema.dump(facilities)
    return jsonify(result)




# 3
# query facilities based on facility_type
# returns all facilities that are classed as specified facility type
@public.route('/facilities/type/<string:facility_type>', methods=['GET'])
def get_facilities_by_type(facility_type):
    facilities = Facility.query.join(FacilityType).filter(FacilityType.name == facility_type).all()
    result = facilities_schema.dump(facilities)
    return jsonify(result)




# THIS RETURNS ANY FACILITIES THAT HAVE ATLEAST 1 OF SPECIFIED AMENS. 
# CHECK FUNCTIONALITY AND/OR
# 4
# query facilities based on an amenity list
# returns all facilities that have the specified amenities
@public.route('/amenities/<string:amenity_ids>', methods=['GET'])
def get_facilities_by_amenities(amenity_ids):
    # convert comma-separated string of amenity IDs to a list of integers
    amenity_ids = [int(amenity_id) for amenity_id in amenity_ids.split(',')]

    # query facilities that have the selected amenities
    facilities = Facility.query.filter(Facility.amenities.any(Amenity.id.in_(amenity_ids))).all()
    result = facilities_schema.dump(facilities)

    return jsonify(result)




# 5
# query facilities based on specified opening/closing hours
@public.route('/facilities/hours/<string:opening_time>/<string:closing_time>', methods=['GET'])
def facilities_hours(opening_time, closing_time):
    facilities = Facility.query.filter(Facility.opening_time <= opening_time)\
                              .filter(Facility.closing_time >= closing_time)\
                              .all()
    result = facilities_schema.dump(facilities)
    return jsonify(result)




# THIS RETURNS IF EITHER TIME IS WITHIN BOUNDS. 
# CHECK OVER DESIRED FUNCTIONALITY AND VS OR
# 6
# query all facilities of a specific type that are open for certain hours
@public.route('/facilities/<string:facility_type>/hours/<string:opening_time>/<string:closing_time>', methods=['GET'])
def get_facilities_open_hours(facility_type, opening_time, closing_time):
    facilities = Facility.query.filter_by(facility_type=facility_type)\
                              .filter(Facility.opening_time <= opening_time)\
                              .filter(Facility.closing_time >= closing_time)\
                              .all()
    result = facilities_schema.dump(facilities)
    return jsonify(result)




# 7
# query all facilities in a specified post_code that have the specified amenities
# returns all facilities within post_code and also have desired amenities
@public.route('/facilities/postcode/<string:post_code>/amenities/<string:amenity_ids>', methods=['GET'])
def local_facilities_with_amenities(post_code, amenity_ids):
    # Split comma-separated amenity IDs into a list
    amenity_ids_list = amenity_ids.split(',')
    
    # Query facilities with matching postcode and amenities
    facilities = Facility.query \
        .join(Facility.address) \
        .join(Facility.facility_amenities) \
        .filter(and_(Address.post_code.has(post_code=post_code), Facility.facility_amenities.any(Amenity.id.in_(amenity_ids_list)))) \
        .all()
    
    result = facilities_schema.dump(facilities)
    return jsonify(result)




# 8
# query all facilities that are running promotions in a specified post_code
# returns all facilities within post_code that are also running promotions
@public.route('/facilities/postcode/<string:post_code>/promotions', methods=['GET'])
def local_with_promotions(post_code):
    # Query facilities with matching postcode and active promotions
    facilities = Facility.query \
        .join(Facility.address) \
        .join(Facility.promotions) \
        .filter(Address.post_code.has(post_code=post_code), Promotion.start_date <= datetime.now(), Promotion.end_date >= datetime.now()) \
        .all()
    
    result = facilities_schema.dump(facilities)
    return jsonify(result)
