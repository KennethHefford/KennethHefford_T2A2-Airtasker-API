from flask import Blueprint, request
from models.user import User, user_schema, UserSchema
from models.jobrequest import Jobrequest
from models.jobpost import Jobpost
from models.review import Review
from init import bcrypt, db
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from utils import authorise_as_admin
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # get the data from the body of the request
        body_data = UserSchema().load(request.get_json())
        # create an instance of the user model
        user = User(
            user_name = body_data.get("user_name"),
            name = body_data.get("name"),
            email = body_data.get("email"),
            location = body_data.get("location")
        )
        # hash the password
        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        # add and commit to db
        db.session.add(user)
        db.session.commit()
        # return acknowledgement
        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"{err.orig.diag.column_name} is required."}, 400
            #not null violation
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            #unique violation
            return {"error": "Email address is already in use."}, 400


@auth_bp.route("/login", methods=["POST"])
def login_user():
    #get the data from the body from the body of the request
    body_data = request.get_json()
    #find the user in DB with that email address
    stmt = db.select(User).filter_by(user_name=body_data["user_name"])
    user = db.session.scalar(stmt)
    #if user exists and pw is correct 
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        #create jwt
        token = create_access_token(identity=str(user.user_name), expires_delta=timedelta(days=1))
        #respond
        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    #else
    else:
        #respond back with an error message
        return {"error": "Invalid email or password"}, 400


@auth_bp.route("/users", methods=["PATCH", "PUT"])
@jwt_required()
def update_user():
    # Ensure the user from the JWT matches the user being updated
    body_data = UserSchema().load(request.get_json(), partial=True)
    password = body_data.get("password")
    #get the user from the db
    stmt = db.select(User).filter_by(user_name=get_jwt_identity())
    user = db.session.scalar(stmt)
    #if user exists
    if user:
            user.user_name = body_data.get("user_name") or user.user_name
            if password:
                user.password = bcrypt.generate_password_hash(password).decode("utf-8")
            user.name = body_data.get("name") or user.name
            user.email = body_data.get("email") or user.email
            user.location = body_data.get("location") or user.location
            password = body_data.get("password")
            #commit the session
            db.session.commit()
            #return acknowledgement
            return user_schema.dump(user)
    else:
            # return error message if user not existing
            return {"error": "User not found"}, 404
    
#delete user
@auth_bp.route("/users/<string:user_name>", methods=["DELETE"])
@jwt_required()
@authorise_as_admin
def delete_user(user_name):
    # Get user from db
    stmt = db.select(User).filter_by(user_name=user_name)
    user = db.session.scalar(stmt)
    
    # If user exists
    if user:
        # Generate a unique user_name
        stmt = db.select(User).filter(User.user_name.like('[deleted user%]')).order_by(User.user_name.desc())
        last_deleted_user = db.session.scalar(stmt)
        
        if last_deleted_user:
            last_number = int(last_deleted_user.user_name.split()[-1])
            new_deleted_user_name = f"[deleted user {last_number + 1}]"
        else:
            new_deleted_user_name = "[deleted user 1]"
        
        # Generate a unique placeholder email
        new_deleted_user_email = f"deleted{last_number + 1}@example.com" if last_deleted_user else "deleted1@example.com"

        # Check if the placeholder user exists, if not, create it
        stmt = db.select(User).filter_by(user_name=new_deleted_user_name)
        deleted_user = db.session.scalar(stmt)
        if not deleted_user:
            deleted_user = User(
                user_name=new_deleted_user_name,
                name="Deleted User",
                email=new_deleted_user_email,
                location="Unknown",
                password="",
                is_admin=False
            )
            db.session.add(deleted_user)
            db.session.commit()
            
        # Set user_name to placeholder in jobrequest table by user for completed job requests
        stmt = db.update(Jobrequest).where(Jobrequest.user_name == user_name, Jobrequest.completed == True).values(user_name=new_deleted_user_name)
        db.session.execute(stmt)

        # Delete job requests where completed is False
        stmt = db.delete(Jobrequest).where(Jobrequest.user_name == user_name, Jobrequest.completed == False)
        db.session.execute(stmt)

        # Set user_name to placeholder for all reviews by user
        stmt = db.update(Review).where(Review.user_name == user_name).values(user_name=new_deleted_user_name)
        db.session.execute(stmt)

        # Delete job posts by user
        stmt = db.delete(Jobpost).where(Jobpost.user_name == user_name)
        db.session.execute(stmt)

        # Delete the user
        db.session.delete(user)
        db.session.commit()
        
        # Return success message
        return {"message": f"User Name: {user_name} deleted successfully!"}
    else:
        # Return error message if user not found
        return {"error": f"User {user_name} not found"}, 404