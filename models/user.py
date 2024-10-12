from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

# User Model representing the 'users' table in the database
class User(db.Model):
    __tablename__ = "users"  # Define the table name

    # Table columns
    user_name = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships with other tables
    jobposts = db.relationship("Jobpost", back_populates="user", cascade="all, delete-orphan")
    jobrequests = db.relationship("Jobrequest", back_populates="user", cascade="all, delete-orphan")
    reviews = db.relationship('Review', back_populates='user', cascade="all, delete-orphan")


# User Schema for serializing and deserializing User data
class UserSchema(ma.Schema):
    # Nested schemas for related data
    jobposts = fields.List(fields.Nested('JobpostSchema', exclude=["user"]))
    jobrequests = fields.List(fields.Nested('JobrequestSchema', exclude=["user"]))
    reviews = fields.List(fields.Nested('ReviewSchema', exclude=["user"]))

    # Email validation (length and format)
    email = fields.String(required=True, validate=[
        And(
            Length(min=1, max=50, error="Email must be between 1 and 50 characters."),
            Regexp(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', error="Invalid email address.")
        )
    ])

    # User name validation (length and format)
    user_name = fields.String(required=True, validate=[
        And(
            Length(min=1, max=50, error="User name must be between 1 and 50 characters."),
            Regexp(r'^[a-zA-Z0-9_]+$', error="User name must contain only alphanumeric characters and underscores.")
        )
    ])

    # Meta class to define the fields to include
    class Meta:
        fields = (
            "user_name",
            "name",
            "email",
            "location",
            "password",
            "is_admin",
            "jobposts",
            "jobrequests",
            "reviews"
        )


# User Schemas for handling serialization
user_schema = UserSchema(exclude=["password"])  # Schema for a single user
users_schema = UserSchema(many=True, exclude=["password"])  # Schema for a list of users
