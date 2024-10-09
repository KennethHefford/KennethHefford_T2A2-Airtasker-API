from flask_jwt_extended import get_jwt_identity

from init import db
from models.user import User


def authorise_as_admin():
    # get users user_name from get jwt identity
    user_name = get_jwt_identity()
    #fetch user from db
    stmt = db.select(User).filter_by(user_name=user_name)
    user = db.session.scalar(stmt)
    #check if user is admin or not
    return user.is_admin
