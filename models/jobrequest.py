from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# Jobrequest model representing the 'jobrequests' table
class Jobrequest(db.Model):
    __tablename__ = "jobrequests"  # Table name

    # Table columns
    request_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_time = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    # Foreign keys
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("jobposts.job_id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="jobrequests")
    jobpost = db.relationship("Jobpost", back_populates="jobrequests")
    reviews = db.relationship('Review', back_populates='jobrequest', cascade="all, delete-orphan")


# Schema for serializing/deserializing Jobrequest data
class JobrequestSchema(ma.Schema):
    # Nested schemas for related user, jobpost, and review data
    user = fields.Nested('UserSchema', only=["name"])
    jobpost = fields.Nested('JobpostSchema', only=["job_id", "job_type", "job_location"], exclude=["jobrequests"])
    reviews = fields.Nested('ReviewSchema', many=True, exclude=["jobrequest"])

    # Title validation (length and format)
    title = fields.String(required=True, validate=[
        And(
            Length(min=3, max=30, error="Title must be between 3 and 30 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ]*$', error="Title must start with a capital letter and contain only alphanumeric characters and spaces.")
        )
    ])

    # Description validation (length)
    description = fields.String(required=True, validate=[Length(min=1, max=500, error="Description must be between 1 and 500 characters.")])

    # Job time validation (length and format)
    job_time = fields.String(required=True, validate=[
        And(
            Length(min=1, max=50, error="Job Time must be between 1 and 50 characters."),
            Regexp(r'^[a-zA-Z0-9 ,\-]*$', error="Job Time must contain only alphanumeric characters, spaces, commas, and hyphens.")
        )
    ])

    # Meta class to define the fields to include and enforce ordering
    class Meta:
        fields = ("title", "request_id", "job_time", "date", "description", "completed", "user", "jobpost", "reviews")
        ordered = True  # Ensures fields are returned in the specified order


# Schemas for handling single or multiple job request objects
jobrequest_schema = JobrequestSchema()  # Single job request
jobrequests_schema = JobrequestSchema(many=True)  # List of job requests
