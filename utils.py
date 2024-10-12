import functools

from flask_jwt_extended import get_jwt_identity

from init import db
from models.user import User
from models.jobrequest import Jobrequest
from models.jobpost import Jobpost


#creating a decorator for authorise_as_admin

def authorise_as_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #get the user's identify from get_jwt_identity
        user_name = get_jwt_identity()
        #fetch the user from the db
        stmt = db.select(User).filter_by(user_name=user_name)
        user = db.session.scalar(stmt)
        # if user is admin
        if user.is_admin:
            #allow decorator func to run
            return func(*args, **kwargs)
        #else
        else:
            #return error message
            return {"error": "You are not authorised to perform this action."}, 403
    return wrapper



def authorise_as_admin_or_user(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current user's user_name from the JWT
        current_user_name = get_jwt_identity()
        
        # Fetch the current user from the db
        stmt = db.select(User).filter_by(user_name=current_user_name)
        current_user = db.session.scalar(stmt)
        
        # Check if the current user is admin
        if current_user.is_admin:
            return func(*args, **kwargs)

        # Determine the model type based on the route parameters
        table_entry = None
        if 'request_id' in kwargs:
            stmt = db.select(Jobrequest).filter_by(request_id=kwargs['request_id'])
            table_entry = db.session.scalar(stmt)
        elif 'job_id' in kwargs:
            stmt = db.select(Jobpost).filter_by(job_id=kwargs['job_id'])
            table_entry = db.session.scalar(stmt)
        elif 'user_name' in kwargs:
            stmt = db.select(User).filter_by(user_name=kwargs['user_name'])
            table_entry = db.session.scalar(stmt)

        # Check if the entry exists and if the user is the owner
        if table_entry and table_entry.user_name == current_user_name:
            return func(*args, **kwargs)

        # Return error message if not authorized
        return {"error": "You are not authorised to perform this action."}, 403

    return wrapper