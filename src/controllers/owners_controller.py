from flask import jsonify, request, redirect, url_for, Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app import db, bcrypt
from marshmallow import fields
from utilities import *
from datetime import timedelta
from models.owners import Owner
from schemas.owners_schema import owner_schema


auth = Blueprint('auth', __name__, url_prefix="/login")
owners = Blueprint('owners', __name__, url_prefix='/owners')

# 1
# authenticate an existing owner 
@auth.route("/secure", methods=["POST"])
def auth_login():
        # define the owner schema fields
        email = fields.Email(required=True)
        password = fields.String(required=True)
        
        # load and validate the request data using OwnerSchema
        owner_fields = owner_schema.load(request.json)

        # find the owner in the database by email
        owner = Owner.query.filter_by(email=owner_fields["email"]).first()

        # if the owner is not found, redirect to the register route
        if not owner:
            return jsonify({"error": "Owner email does not exist."}), 405
            return redirect(url_for('owners.register'))


        # if the owner is not found or the password is incorrect, return an error
        if owner and not bcrypt.check_password_hash(owner.password, owner_fields["password"]):
            return jsonify({"error": "Invalid password, please try again."}), 401

        # generate an access token with the owner's ID as the identity
        expiry = timedelta(days=1)
        access_token = create_access_token(identity=owner.id, expires_delta=expiry)

        # return the access token to the owner
        return jsonify({"access_token": access_token}), 200
    




# 2
# Register a new owner
@owners.route('/register/secure', methods=['POST'])
def register():
    # Load and validate the request data using OwnerSchema
    owner_fields = owner_schema.load(request.json, partial=False)

    # Extract the validated data from the fields dictionary
    name = owner_fields['name']
    email = owner_fields['email']
    password = owner_fields['password']
    mobile = owner_fields['mobile']

    # Check if owner already exists in the database
    existing_owner = Owner.query.filter_by(email=email).first()

    if existing_owner:
       return jsonify({"error": "You already have an account. Please login."}), 400

    owner = Owner(name=name,
              email=email,
              mobile=mobile,
              # Hash the owner's password before saving to the database
              password=bcrypt.generate_password_hash(password).decode('utf-8'))
            

    # add and commit new owner to db
    db.session.add(owner)
    db.session.commit()

    # generate an access token and return it
    access_token = create_access_token(identity=owner.id)
    return jsonify({'access_token': access_token}), 200



        

# 3
# retrieve details of a logged-in owner
@owners.route('/<int:owner_id>/secure', methods=['GET'])
@jwt_required()
def get_owner(owner_id):
    try:
        # verify access
        access_check = verify_ownerdetails_access(owner_id)
        if access_check:
            return access_check

        owner = Owner.query.get(owner_id)

        # return owner details that match
        return jsonify({'owner':owner_schema.dump(owner)}), 200
    except:
        return jsonify({'error': 'Invalid owner ID'}), 404





# 4
# update details of a logged-in owner
@owners.route('/<int:owner_id>/secure', methods=['PUT'])
@jwt_required()
def update_owner(owner_id):
    # Verify access
    access_check = verify_ownerdetails_access(owner_id)
    if access_check:
        return access_check

    # retrieve the owner from the database
    owner = Owner.query.get(owner_id)

    # load the owner schema fields from the request data
    owner_fields = owner_schema.load(request.json, partial=True)

    # update the owner details with the loaded data
    owner.name = owner_fields.get('name', owner.name)
    owner.email = owner_fields.get('email', owner.email)
    owner.mobile = owner_fields.get('mobile', owner.mobile)
    owner.password = owner_fields.get('password', owner.password)

    # hash the owner's password before saving to the database
    hashed_password = bcrypt.generate_password_hash(owner.password).decode('utf-8')
    owner.password = hashed_password

    # commit changes to database
    db.session.commit()
    return jsonify({'message': 'Owner information updated successfully'}), 200





# 5
# delete account of a logged-in owner
@owners.route('/account/secure', methods=['DELETE'])
@jwt_required()
def delete_account():
    owner_id = get_jwt_identity()

    # verify if owner has access
    access_check = verify_ownerdetails_access(owner_id)
    if access_check:
        return access_check

    # retrieve the owner from the database
    owner = Owner.query.get(owner_id)
    
    # delete all facilities associated with the owner
    for facility in owner.facilities:
        db.session.delete(facility)

    # delete the owner's account
    db.session.delete(owner)
    db.session.commit()

    return jsonify({'message': 'Account deleted successfully'})
