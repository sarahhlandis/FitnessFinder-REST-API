from flask import jsonify, Blueprint
from models.facility_types import FacilityType

facilities = Blueprint('facilities', __name__, url_prefix="/facilities")


# facility_types are prepopulated so there is no functionality for an owner to need to modify
# there is no functionality to delete a facility_type from a facility as it is required
# there is only functionality to update the facility type (in the facilities controller)

# retrieve a list of all facility types and their id assignments
@facilities.route('/facility_types', methods=['GET'])
def get_facility_types():
    facility_types = FacilityType.query.all()
    facility_types_dict = {}
    for facility_type in facility_types:
        facility_types_dict[facility_type.id] = facility_type.name
    return jsonify(facility_types_dict) 


