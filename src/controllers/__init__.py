from controllers.addresses_controller import addresses
from controllers.amenities_controller import amenities
from controllers.facilities_controller import facilities
from controllers.facility_types_controller import facility_types
from controllers.owners_controller import owners
from controllers.promotions_controller import promotions
from controllers.public_controller import public

registerable_controllers = [
    addresses,
    amenities,
    facilities,
    facility_types,
    owners,
    promotions,
    public
]