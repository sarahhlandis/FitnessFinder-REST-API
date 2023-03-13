from app import db, bcrypt
from flask import Blueprint
from datetime import date
from models.owners import Owner
from models.amenities import Amenity
from models.facilities import Facility
from models.addresses import Address
from models.promotions import Promotion
from models.post_codes import PostCode


db_commands = Blueprint("db", __name__)


# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands .cli.command("seed")
def seed_db():
    try:
        # SAMPLE 1
        # Create owners before facilities as owner id is needed in the facility model as an fkey
        owner1 = Owner(
            email="owner1@example.com",
            password=bcrypt.generate_password_hash("hello111").decode("utf-8"),
            mobile="0412345681"
        )

        db.session.add(owner1)
        db.session.commit()

        facility1 = Facility(
            business_name="BodyFit",
            independent=True,
            phone_num="0234567891",
            opening_time="08:00",
            closing_time="18:00",
            facility_type="Gym"
        )
        
        address1 = Address(
            street_num=5,
            street="George Street",
            suburb="Sydney",
            state="NSW",
        )

        post_code1=PostCode(post_code="2000")

        amenity1 = Amenity.query.filter_by(sauna=True).first()
        amenity2 = Amenity.query.filter_by(pool=True).first()

        promotion1 = Promotion(
            name="Easter offer",
            discount=15,
            start_date=date(2023, 4, 1),
            end_date=date(2023, 4, 15)
        )

        # associate objects with each other
        facility1.owner = owner1
        facility1.address = address1
        facility1.post_code = post_code1
        facility1.amenities.append(amenity1)
        facility1.amenities.append(amenity2)
        facility1.promotions.append(promotion1)

        # add all objects to the session and commit changes
        db.session.add_all([owner1, facility1, address1, post_code1, amenity1, amenity2, promotion1])

        # SAMPLE 2
        # Create owners before facilities as owner id is needed in the facility model as an fkey
        owner2 = Owner(
            email="owner2@example.com",
            password=bcrypt.generate_password_hash("hello222").decode("utf-8"),
            mobile="0412345682"
        )

        facility2 = Facility(
            business_name="Lifetime",
            independent=False,
            phone_num="0234567892",
            opening_time="6:00",
            closing_time="20:00",
            facility_type="Wellness Center"
        )

        address2 = Address(
            street_num=210,
            street="Banksia Drive",
            suburb="Sydney",
            state="NSW",
        )

        post_code2=PostCode(post_code="2000")

        amenity3 = Amenity.query.filter_by(boxing=True).first()
        amenity4 = Amenity.query.filter_by(pool=True).first()
        amenity5 = Amenity.query.filter_by(steam_room=True).first()
        amenity6 = Amenity.query.filter_by(showers=True).first()
        amenity7 = Amenity.query.filter_by(fuel_bar=True).first()
        amenity8 = Amenity.query.filter_by(parking=True).first()

        promotion2 = Promotion(
            name="March Promo",
            discount=20,
            start_date=date(2023, 3, 1),
            end_date=date(2023, 3, 31)
        )

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

        # add all objects to the session and commit changes
        db.session.add_all([owner2, facility2, address2, post_code2, 
                            amenity3, amenity4, amenity5, amenity6, amenity7, amenity8, promotion2])

        # SAMPLE 3
        # Create owners before facilities as owner id is needed in the facility model as an fkey
        owner3 = Owner(
            email="owner3@example.com",
            password=bcrypt.generate_password_hash("hello333").decode("utf-8"),
            mobile="0412345683"
        )

        facility3 = Facility(
            business_name="MindBody Boxing",
            independent=True,
            phone_num="0234567893",
            opening_time="5:00",
            closing_time="14:00",
            facility_type="Boxing Gym"
        )

        address3 = Address(
            street_num=4,
            street="Acacia Street",
            suburb="Byron Bay",
            state="NSW",
        )

        post_code3=PostCode(post_code="2481")

        amenity9 = Amenity.query.filter_by(boxing=True).first()
        amenity10 = Amenity.query.filter_by(lockers=True).first()

        # associate objects with each other
        facility3.owner = owner3
        facility3.address = address3
        facility3.post_code = post_code3
        facility3.amenities.append(amenity9)
        facility3.amenities.append(amenity10)

        # add all objects to the session and commit changes
        db.session.add_all([owner3, facility3, address3, post_code3, amenity9, amenity10])


        # SAMPLE 4
        # Create owners before facilities as owner id is needed in the facility model as an fkey
        owner4 = Owner(
            email="owner4@example.com",
            password=bcrypt.generate_password_hash("hello444").decode("utf-8"),
            mobile="0412345684"
        )

        facility4 = Facility(
            business_name="Space Yoga",
            independent=True,
            phone_num="0234567894",
            opening_time="9:30", 
            closing_time="19:30",
            facility_type="Yoga Studio"
        )

        address4 = Address(
            street_num=18,
            street="Cavannbah Road",
            suburb="Newcastle",
            state="NSW",
        )

        post_code4=PostCode(post_code="2267")

        amenity11 = Amenity.query.filter_by(yoga=True).first()
        amenity12 = Amenity.query.filter_by(private_training=True).first()


        # associate objects with each other
        facility4.owner = owner4
        facility4.address = address4
        facility4.post_code = post_code4
        facility4.amenities.append(amenity11)
        facility4.amenities.append(amenity12)

        # add all objects to the session and commit changes
        db.session.add_all([owner4, facility4, address4, post_code4, amenity11, amenity12])


        # SAMPLE 5
        # Create owners before facilities as owner id is needed in the facility model as an fkey
        owner5 = Owner(
            email="owner5@example.com",
            password=bcrypt.generate_password_hash("hello555").decode("utf-8"),
            mobile="0412345685"
        )

        facility5 = Facility(
            business_name="Pilates101",
            independent=True,
            phone_num="0234567895",
            opening_time="6:30", 
            closing_time="18:30",
            facility_type="Pilates Studio"
        )
    
        address5 = Address(
            street_num=73,
            street="Castlereagh Street",
            suburb="Newport",
            state="NSW",
        )

        post_code5=PostCode(post_code="2101")

        # associate objects with each other
        facility5.owner = owner5
        facility5.address = address5
        facility5.post_code = post_code5

        # add all objects to the session and commit changes
        db.session.add_all([owner5, facility5, address5, post_code5])


        db.session.commit()
        print("Database seeded!")
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.session.rollback()
        raise e

    


@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 