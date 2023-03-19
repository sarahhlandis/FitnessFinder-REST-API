from flask import jsonify
from models.facilities import Facility
from models.owners import Owner


# repeated helper function

# check owner verification respective to owner details and facility access
def verify_owner_access(facility_ids, owner_id):
    if isinstance(facility_ids, int):
        facility_ids = [facility_ids]
        
    for facility_id in facility_ids:
        # retrieve the facility from the database
        facility = Facility.query.filter_by(id=facility_id).first()

        if facility is None:
            return jsonify({'error': 'Facility not found'}), 404

        # check if the authenticated owner has access to the facility
        if facility.owner_id != owner_id:
            return jsonify({'error': 'You are not authorized to access this facility'}), 403

    # return None if access is granted
    return None


# check owner verification respective to owner details
def verify_ownerdetails_access(owner_id):
    # retrieve the owner from the database
    owner = Owner.query.filter_by(id=owner_id).first()

    if owner is None:
        return jsonify({'error': 'Owner not found'}), 404

    # return None if access is granted
    return None