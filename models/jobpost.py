from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# Jobpost model representing the 'jobposts' table
class Jobpost(db.Model):
    __tablename__ = "jobposts"  # Table name

    # Table columns
    availability = db.Column(db.String, nullable=False)
    job_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_type = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False)
    job_location = db.Column(db.String, nullable=False)

    # Foreign key to the 'users' table
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='jobposts')
    jobrequests = db.relationship('Jobrequest', back_populates="jobpost", cascade="all, delete-orphan")


# Schema for serializing/deserializing Jobpost data
class JobpostSchema(ma.Schema):
    # Nested schemas for related user and job requests data
    user = fields.Nested('UserSchema', only=["name"])
    jobrequests = fields.List(fields.Nested('JobrequestSchema', exclude=["jobpost"]))
    reviews = fields.List(fields.Nested('ReviewSchema', exclude=["jobpost"]))

    # Job type validation (length and format)
    job_type = fields.String(required=True, validate=[
        And(
            Length(min=3, max=20, error="Job Type must be between 3 and 20 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ]*$', error="Job Type must start with a capital letter and contain only alphanumeric characters and spaces.")
        )
    ])

    # Job location validation (length and format)
    job_location = fields.String(required=True, validate=[
        And(
            Length(min=1, max=50, error="Job Location must be between 1 and 50 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ]*$', error="Job Location must start with a capital letter and contain only alphanumeric characters and spaces.")
        )
    ])

    # Availability validation (length and format)
    availability = fields.String(required=True, validate=[
        And(
            Length(min=1, max=50, error="Availability must be between 1 and 50 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ,\-]*$', error="Availability must start with a capital letter and contain only alphanumeric characters, commas, spaces, and hyphens.")
        )
    ])

    # Description validation (length)
    description = fields.String(required=True, validate=[Length(min=1, max=500, error="Description must be between 1 and 500 characters.")])

    # Meta class to define the fields to include and enforce ordering
    class Meta:
        fields = ("job_id", "job_type", "job_location", "availability", "description", "date", "user", "jobrequests")
        ordered = True  # Ensures fields are returned in the specified order


# Schemas for handling single or multiple job post objects
jobpost_schema = JobpostSchema()  # Single job post
jobposts_schema = JobpostSchema(many=True)  # List of job posts
