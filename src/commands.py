from app import db, bcrypt
from flask import Blueprint
from datetime import date
from models.owners import Owner
from models.amenities import Amenity
from models.facilities import Facility
from models.addresses import Address
from models.promotions import Promotion
from models.post_codes import PostCode
from models.facility_types import FacilityType


db_commands = Blueprint("db", __name__)


# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
# cli command to create all tables
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")



# cli command to initialize database with prepopulated values
@db_commands .cli.command("init")
def init_db():
    try:
        # check if default facility types have already been added to database
        if FacilityType.query.first() is not None:
            print('Default facility types already exist in database.')
            return

        # add default facility types to the database
        facility_types = [
            FacilityType(name="Pilates Studio"),
            FacilityType(name="Gym"),
            FacilityType(name="Wellness Center"),
            FacilityType(name="Yoga Studio"),
            FacilityType(name="Dance Studio"),
            FacilityType(name="Athletic Club"),
            FacilityType(name="Boxing Gym"),
            # add more facility types as needed
        ]
        db.session.add_all(facility_types)
        db.session.commit()
        print('Default facility types added to database.')


        # check if default amenities have already been added to database
        if Amenity.query.first() is not None:
            print('Default amenities already exist in database.')
            return
        
        # prepopulate amenities table
        amenities = [
            {"name": "parking"},
            {"name": "pool"},
            {"name": "sauna"},
            {"name": "steam_room"},
            {"name": "fuel_bar"},
            {"name": "pilates"},
            {"name": "boxing"},
            {"name": "yoga"},
            {"name": "private_training"},
            {"name": "lockers"},
            {"name": "showers"}
            # add more amenities here
        ]

        for amenity in amenities:
            db.session.add(Amenity(name=amenity["name"]))
        db.session.commit()

        print('Default amenities added to database.')
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.session.rollback()
        raise e



# cli command to seed database with sample data
@db_commands .cli.command("seed")
def seed_db():
    try:
        # seed OWNERS table first as facilities table 
        # relies on owner_id as fkey
        owner1 = Owner(
            name="Jane Doe",
            email="owner1@example.com",
            password=bcrypt.generate_password_hash("hello111").decode("utf-8"),
            mobile="0412345681"
        )
        db.session.add(owner1)

        owner2 = Owner(
            name="Mary Davis",
            email="owner2@example.com",
            password=bcrypt.generate_password_hash("hello222").decode("utf-8"),
            mobile="0412345682"
        )
        db.session.add(owner2)

        owner3 = Owner(
            name="Alex Johnson",
            email="owner3@example.com",
            password=bcrypt.generate_password_hash("hello333").decode("utf-8"),
            mobile="0412345683"
        )
        db.session.add(owner3)

        owner4 = Owner(
            name="John Smith",
            email="owner4@example.com",
            password=bcrypt.generate_password_hash("hello444").decode("utf-8"),
            mobile="0412345684"
        )
        db.session.add(owner4)

        owner5 = Owner(
            name="Sally Williams",
            email="owner5@example.com",
            password=bcrypt.generate_password_hash("hello555").decode("utf-8"),
            mobile="0412345685"
        )
        db.session.add(owner5)

        owner6 = Owner(
            name="Will Brown",
            email="owner6@example.com",
            password=bcrypt.generate_password_hash("hello666").decode("utf-8"),
            mobile="0412345686"
        )
        db.session.add(owner6)


        # commit all owner entries to database
        db.session.commit()


        # seed POST_CODES table next as post_code_id is an fkey
        # in addresses table
        post_code1=PostCode(
            post_code="2000"
        )
        db.session.add(post_code1)

        post_code2=PostCode(
            post_code="2000"
        )
        db.session.add(post_code2)

        post_code3=PostCode(
            post_code="2481"
        )
        db.session.add(post_code3)

        post_code4=PostCode(
            post_code="2267"
        )
        db.session.add(post_code4)

        post_code5=PostCode(
            post_code="2101"
        )
        db.session.add(post_code5)

        post_code6=PostCode(
            post_code="2481"
        )
        db.session.add(post_code6)

        # commit all post_code entries to database
        db.session.commit()


        # seed ADDRESSES table before FACILITIES table as facilities
        # use address_id as an fkey
        address1 = Address(
            street_num=5,
            street="George Street",
            suburb="Sydney",
            state="NSW",
            post_code_id=post_code1.id
        )
        db.session.add(address1)

        address2 = Address(
            street_num=210,
            street="Banksia Drive",
            suburb="Sydney",
            state="NSW",
            post_code_id=post_code2.id
        )
        db.session.add(address2)

        address3 = Address(
            street_num=4,
            street="Acacia Street",
            suburb="Byron Bay",
            state="NSW",
            post_code_id=post_code3.id
        )
        db.session.add(address3)

        address4 = Address(
            street_num=18,
            street="Cavannbah Road",
            suburb="Newcastle",
            state="NSW",
            post_code_id=post_code4.id
        )
        db.session.add(address4)

        address5 = Address(
            street_num=73,
            street="Castlereagh Street",
            suburb="Newport",
            state="NSW",
            post_code_id=post_code5.id
        )
        db.session.add(address5)

        address6 = Address(
            street_num=5,
            street="Browning Street",
            suburb="Byron Bay",
            state="NSW",
            post_code_id=post_code6.id
        )
        db.session.add(address6)
    
        # commit all address entries to database
        db.session.commit()


        # seed FACILITIES table next as promotions and amenities
        # must have facility_id as fkeys in their tables
        facility1 = Facility(
            business_name="BodyFit",
            independent=True,
            phone_num="0234567891",
            opening_time="08:00",
            closing_time="18:00",
            facility_type=2,
            address_id=address1.id,
            owner_id=owner1.id
        )
        db.session.add(facility1)

        facility2 = Facility(
            business_name="Lifetime",
            independent=False,
            phone_num="0234567892",
            opening_time="6:00",
            closing_time="20:00",
            facility_type=3,
            address_id=address2.id,
            owner_id=owner2.id
        )
        db.session.add(facility2)

        facility3 = Facility(
            business_name="MindBody Boxing",
            independent=True,
            phone_num="0234567893",
            opening_time="5:00",
            closing_time="14:00",
            facility_type=7,
            address_id=address3.id,
            owner_id=owner3.id
        )
        db.session.add(facility3)

        facility4 = Facility(
            business_name="Space Yoga",
            independent=True,
            phone_num="0234567894",
            opening_time="9:30", 
            closing_time="19:30",
            facility_type=4,
            address_id=address4.id,
            owner_id=owner4.id
        )
        db.session.add(facility4)

        facility5 = Facility(
            business_name="Pilates101",
            independent=True,
            phone_num="0234567895",
            opening_time="6:30", 
            closing_time="18:30",
            facility_type=1,
            address_id=address5.id,
            owner_id=owner5.id
        )
        db.session.add(facility5)

        facility6 = Facility(
            business_name="Pure Barre",
            independent=False,
            phone_num="0234567896",
            opening_time="8:00", 
            closing_time="18:00",
            facility_type=1,
            address_id=address6.id,
            owner_id=owner6.id
        )
        db.session.add(facility6)

        # commit all facility entries to database
        db.session.commit()


        # seed AMENITIES table next 
        amenity1 = Amenity.query.filter_by(name='sauna').first()
        amenity2 = Amenity.query.filter_by(name='pool').first()

        db.session.add(amenity1)
        db.session.add(amenity2)

        amenity3 = Amenity.query.filter_by(name='boxing').first()
        amenity4 = Amenity.query.filter_by(name='pool').first()
        amenity5 = Amenity.query.filter_by(name='steam_room').first()
        amenity6 = Amenity.query.filter_by(name='showers').first()
        amenity7 = Amenity.query.filter_by(name='fuel_bar').first()
        amenity8 = Amenity.query.filter_by(name='parking').first()

        db.session.add(amenity3)
        db.session.add(amenity4)
        db.session.add(amenity5)
        db.session.add(amenity6)
        db.session.add(amenity7)
        db.session.add(amenity8)

        amenity9 = Amenity.query.filter_by(name='boxing').first()
        amenity10 = Amenity.query.filter_by(name='lockers').first()

        db.session.add(amenity9)
        db.session.add(amenity10)

        amenity11 = Amenity.query.filter_by(name='yoga').first()
        amenity12 = Amenity.query.filter_by(name='private_training').first()

        db.session.add(amenity11)
        db.session.add(amenity12)

        amenity13 = Amenity.query.filter_by(name='yoga').first()
        amenity14 = Amenity.query.filter_by(name='pilates').first()

        db.session.add(amenity13)
        db.session.add(amenity14)

        # commit all amenity entries to database
        db.session.commit()


        # seed PROMOTIONS table last
        promotion1 = Promotion(
            name="Easter offer",
            discount_percent=15,
            start_date=date(2023, 4, 1),
            end_date=date(2023, 4, 15),
            facility_id=facility1.id
        )
        db.session.add(promotion1)

        promotion2 = Promotion(
            name="March Promo",
            discount_percent=20,
            start_date=date(2023, 3, 1),
            end_date=date(2023, 3, 31),
            facility_id=facility2.id
        )
        db.session.add(promotion2)

        promotion3 = Promotion(
            name="Beginner's Barre Special",
            discount_percent=5,
            start_date=date(2023, 3, 1),
            end_date=date(2023, 9, 30),
            facility_id=facility6.id
        )
        db.session.add(promotion3)

        # commit all promotion entries to database
        db.session.commit()


        # define associations
        # associate objects with each other
        facility1.owner = owner1
        facility1.address = address1
        facility1.post_code = post_code1
        facility1.amenities.append(amenity1)
        facility1.amenities.append(amenity2)
        facility1.promotions.append(promotion1)

        # associate objects with each other
        facility2.owner = owner2
        facility2.address = address2
        facility2.post_code = post_code2
        facility2.amenities.append(amenity3)
        facility2.amenities.append(amenity4)
        facility2.amenities.append(amenity5)
        facility2.amenities.append(amenity7)
        facility2.amenities.append(amenity6)
        facility2.amenities.append(amenity8)
        facility2.promotions.append(promotion2)

        # associate objects with each other
        facility3.owner = owner3
        facility3.address = address3
        facility3.post_code = post_code3
        facility3.amenities.append(amenity9)
        facility3.amenities.append(amenity10)

        # associate objects with each other
        facility4.owner = owner4
        facility4.address = address4
        facility4.post_code = post_code4
        facility4.amenities.append(amenity11)
        facility4.amenities.append(amenity12)

        # associate objects with each other
        facility5.owner = owner5
        facility5.address = address5
        facility5.post_code = post_code5

        # associate objects with each other
        facility6.owner = owner6
        facility6.address = address6
        facility6.post_code = post_code6
        facility6.amenities.append(amenity13)
        facility6.amenities.append(amenity14)

        db.session.commit()
        print("Database seeded!")
       
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.session.rollback()
        raise e



    
# cli command to delete all tables from database
@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 


    
# cli command to restart db after some changes
@db_commands .cli.command("reset")
def reset_db():
    db.drop_all()
    print("Tables dropped")

    db.create_all()
    print("Tables created")

    init_db()
    seed_db()
    print("Tables seeded")