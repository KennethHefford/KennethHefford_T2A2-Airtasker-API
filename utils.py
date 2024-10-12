import functools
from flask_jwt_extended import get_jwt_identity

from init import db
from models.user import User
from models.jobrequest import Jobrequest
from models.jobpost import Jobpost


# Decorator to authorize admins only
def authorise_as_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current user's identity from the JWT token
        user_name = get_jwt_identity()
        
        # Fetch the user from the database using their user_name
        stmt = db.select(User).filter_by(user_name=user_name)
        user = db.session.scalar(stmt)

        # Allow function to run if the user is an admin
        if user and user.is_admin:
            return func(*args, **kwargs)

        # Return error if user is not authorized
        return {"error": "You are not authorized to perform this action."}, 403

    return wrapper


# Decorator to authorize admins or resource owners
def authorise_as_admin_or_user(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current user's user_name from the JWT token
        current_user_name = get_jwt_identity()
        
        # Fetch the current user from the database
        stmt = db.select(User).filter_by(user_name=current_user_name)
        current_user = db.session.scalar(stmt)

        # Allow function to run if the user is an admin
        if current_user and current_user.is_admin:
            return func(*args, **kwargs)

        # Initialize variable for the relevant table entry
        table_entry = None

        # Check which model is being accessed based on route parameters
        if 'request_id' in kwargs:
            stmt = db.select(Jobrequest).filter_by(request_id=kwargs['request_id'])
            table_entry = db.session.scalar(stmt)
        elif 'job_id' in kwargs:
            stmt = db.select(Jobpost).filter_by(job_id=kwargs['job_id'])
            table_entry = db.session.scalar(stmt)
        elif 'user_name' in kwargs:
            stmt = db.select(User).filter_by(user_name=kwargs['user_name'])
            table_entry = db.session.scalar(stmt)

        # Allow if the current user owns the table entry
        if table_entry and table_entry.user_name == current_user_name:
            return func(*args, **kwargs)

        # Return error if user is not authorized
        return {"error": "You are not authorized to perform this action."}, 403

    return wrapper
