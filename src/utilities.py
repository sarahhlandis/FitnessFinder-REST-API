from flask import jsonify
from models.facilities import Facility


# repeated helper function

# check owner verification respective to owner details or facility access
def verify_owner_access(facility_id, owner_id):
    # retrieve the facility from the database
    facility = Facility.query.filter_by(id=facility_id).first()

    if facility is None:
        return jsonify({'error': 'Facility not found'}), 404

    # check if the authenticated owner has access to the facility
    if facility.owner_id != owner_id:
        return jsonify({'error': 'You are not authorized to access this facility'}), 403

    # return None if access is granted
    return None