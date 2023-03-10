from flask import jsonify, request, redirect, url_for, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app import db, bcrypt
from marshmallow import fields
from utilities import *
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from models.owners import Owner
from models.facilities import Facility
from schemas.owners_schema import owner_schema, owners_schema


auth = Blueprint('auth', __name__, url_prefix="/login")
owners = Blueprint('owners', __name__, url_prefix='/owners')


# authenticate an existing owner 
@auth.route("/login/secure", methods=["POST"])
def auth_login():
    # Define the owner schema fields
    # name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    owner_schema.load(request.json)

    # Find the owner in the database by email
    owner = Owner.query.filter_by(email=email).first()

    # If the owner is not found, redirect to the register route
    if not owner:
        return redirect(url_for('owners.register'))

    # If the owner is not found or the password is incorrect, return an error
    if not bcrypt.check_password_hash(owner.password, password):
        return jsonify({"error": "Invalid password, please try again."}), 401

    # Generate an access token with the owner's ID as the identity
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=owner.email, expires_delta=expiry)

    # Return the access token to the owner
    return jsonify({"access_token": access_token}), 200


# Register a new owner
@owners.route('/register/secure', methods=['POST'])
def register():
    # Load and validate the request data using OwnerSchema
    owner_fields = owner_schema.load(request.json)

    # Extract the validated data from the fields dictionary
    name = owner_fields['name']
    email = owner_fields['email']
    password = owner_fields['password']
    mobile = owner_fields['mobile']

    # Check if owner already exists in the database
    existing_owner = Owner.query.filter_by(email=email).first()

    if existing_owner is not None:
        # if the owner is found, check the password
        if existing_owner.check_password(password):
            # generate an access token and return it
            access_token = create_access_token(identity=email)
            return jsonify({'access_token': access_token}), 200
        else:
            # if the password is incorrect, return an error message
            return jsonify({'error': 'Invalid password. Please try again'}), 401
    else:
        # if the owner is not found, ask if they want to register as a new owner
        register = owner_fields.get('register')

        if register:
            # create a new owner with the provided name, email, password, and mobile
            owner = Owner(name=name, email=email, mobile=mobile, password=password)
            # Hash the owner's password before saving to the database
            hashed_password = generate_password_hash(password, method='sha256')
            owner.set_password(hashed_password)

            # add and commit new owner to db
            db.session.add(owner)
            db.session.commit()
            # generate an access token and return it
            access_token = create_access_token(identity=email)
            return jsonify({'access_token': access_token}), 200
        else:
            # if the owner doesn't want to register, return an error message
            return jsonify({'error': 'Invalid email'}), 401

        


# retrieve details of a logged-in owner
@owners.route('/<int:owner_id>/secure', methods=['GET'])
@jwt_required()
def get_owner(owner_id):
    # Verify access
    access_check = verify_owner_access(owner_id)
    if access_check:
        return access_check

    owner = Owner.query.get(owner_id)
    # return owner details that match
    return jsonify({'owner':owner_schema.dump(owner)}), 200




# update details of a logged-in owner
@owners.route('/<int:owner_id>/secure', methods=['PUT'])
@jwt_required()
def update_owner(owner_id):
    # Verify access
    access_check = verify_owner_access(owner_id)
    if access_check:
        return access_check
    
    # retrieve the owner from the database
    owner = Owner.query.get(owner_id)

    # load the owner schema fields from the request data
    owner_fields = owner_schema.load(request.json)

    # update the owner details with the loaded data
    owner.name = owner_fields.get('name', owner.name)
    owner.email = owner_fields.get('email', owner.email)
    owner.mobile = owner_fields.get('mobile', owner.mobile)
    owner.password = owner_fields.get('password', owner.password)

    # Hash the owner's password before saving to the database
    hashed_password = generate_password_hash(owner.password, method='sha256')
    owner.set_password(hashed_password)
    # commit changes to database
    db.session.commit()
    return jsonify({'message': 'Owner information updated successfully'}), 200



# delete account of a logged-in owner
@owners.route('/account/secure', methods=['DELETE'])
@jwt_required()
def delete_account():
    owner_id = get_jwt_identity()

    # Verify if owner has access
    access_check = verify_owner_access(owner_id)
    if access_check:
        return access_check

    # retrieve the owner from the database
    owner = Owner.query.get(owner_id)

    # Verify if owner's details match the account they are trying to delete
    owner_fields = request.json
    if owner.name != owner_fields.get('name') or owner.email != owner_fields.get('email') or owner.mobile != owner_fields.get('mobile'):
        return jsonify({'error': 'Unauthorized access'}), 401

    # Delete all facilities associated with the owner's account
    Facility.query.filter_by(owner_id=owner_id).delete()

    # Delete the owner's account
    db.session.delete(owner)
    db.session.commit()

    return jsonify({'message': 'Account deleted successfully'})
