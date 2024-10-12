from flask_jwt_extended import get_jwt_identity
import functools
from init import db
from models.user import User


# def authorise_as_admin():
#     # get users user_name from get jwt identity
#     user_name = get_jwt_identity()
#     #fetch user from db
#     stmt = db.select(User).filter_by(user_name=user_name)
#     user = db.session.scalar(stmt)
#     #check if user is admin or not
#     return user.is_admin


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