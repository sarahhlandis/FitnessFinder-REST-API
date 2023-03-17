from controllers.addresses_controller import addresses
from controllers.amenities_controller import facility_amenities, amenities
from controllers.facilities_controller import facilities, facility_amenities
from controllers.owners_controller import auth, owners
from controllers.promotions_controller import promotions
from controllers.public_controller import public
from controllers.facility_types_controller import facilities


registerable_controllers = [
    addresses,
    facility_amenities,
    facilities,
    owners,
    promotions,
    public,
    auth,
    amenities
]