from init import db, ma 
from marshmallow import fields

class User(db.Model):
    #name of table
    __tablename__ = "users"
    #attributes of table
    user_name = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    jobposts = db.relationship('Jobpost', back_populates ='user')
    jobrequests = db.relationship('Jobrequest', back_populates='user')

class UserSchema(ma.Schema):
    jobposts = fields.List(fields.Nested('JobpostSchema', exclude=["user"]))
    jobrequests = fields.List(fields.Nested('JobrequestSchema', exclude=["user"]))
    class Meta:
        fields = ("user_name","name", "email", "location", "password", "is_admin", "jobpost", "jobrequests")

#to handle a single user object
user_schema = UserSchema(exclude=["password"])
#to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])
