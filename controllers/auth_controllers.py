from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta

from init import bcrypt, db
from models.user import User, user_schema, UserSchema
from utils import authorise_as_admin_or_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Register a new user
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # Get and validate user data from request body
        body_data = UserSchema().load(request.get_json())
        
        # Create a new user instance
        user = User(
            user_name=body_data.get("user_name"),
            name=body_data.get("name"),
            email=body_data.get("email"),
            location=body_data.get("location"),
        )

        # Hash the user's password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Save the user to the database
        db.session.add(user)
        db.session.commit()

        # Return the newly created user data
        return user_schema.dump(user), 201

    except IntegrityError as err:
        # Handle database integrity errors
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"{err.orig.diag.column_name} is required."}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address is already in use."}, 400

# Log in an existing user
@auth_bp.route("/login", methods=["POST"])
def login_user():
    # Get user credentials from request body
    body_data = request.get_json()
    
    # Find the user by username
    stmt = db.select(User).filter_by(user_name=body_data["user_name"])
    user = db.session.scalar(stmt)

    # Validate user credentials
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # Create JWT token for the user
        token = create_access_token(identity=str(user.user_name), expires_delta=timedelta(days=1))
        
        # Return user info and token
        return {"email": user.email, "is_admin": user.is_admin, "token": token}

    return {"error": "Invalid email or password"}, 400

# Delete a user account
@auth_bp.route("/users/<string:user_name>", methods=["DELETE"])
@jwt_required()
@authorise_as_admin_or_user
def delete_user(user_name):
    # Find the user by username
    stmt = db.select(User).filter_by(user_name=user_name)
    user = db.session.scalar(stmt)

    # If user exists, delete them from the database
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User '{user_name}' deleted successfully"}, 200

    return {"message": f"User '{user_name}' not found"}, 404

# Update user information
@auth_bp.route("/users/<string:user_name>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(user_name):
    # Load user data from the request body
    body_data = UserSchema().load(request.get_json(), partial=True)

    # Fetch the user by username
    stmt = db.select(User).filter_by(user_name=user_name)
    user = db.session.scalar(stmt)

    # If user exists, update their information
    if user:
        # Check if the requester is the account owner
        if user.user_name != get_jwt_identity():
            return {"error": "You are not authorised to edit this user. Only the owner can edit their information."}, 403

        # Update user fields if provided
        user.name = body_data.get("name") or user.name
        user.email = body_data.get("email") or user.email
        user.location = body_data.get("location") or user.location
        if body_data.get("password"):
            user.password = bcrypt.generate_password_hash(body_data.get("password")).decode("utf-8")

        # Commit changes to the database
        db.session.commit()

        # Return the updated user data
        return user_schema.dump(user), 200

    return {"error": "User not found"}, 404
