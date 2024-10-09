from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Jobpost(db.Model):
    __tablename__ = "jobposts"


    availability = db.Column(db.String, nullable=False)
    job_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_type = db.Column(db.String, nullable = False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False )
    job_location = db.Column(db.String, nullable=False )
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)


    user = db.relationship('User', back_populates ='jobposts')
    jobrequests = db.relationship('Jobrequest', back_populates="jobpost")

class JobpostSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["name"])
    jobrequests = fields.List(fields.Nested('JobrequestSchema', exclude=["jobpost"]))
    reviews = fields.List(fields.Nested('ReviewSchema', exclude=["jobpost"]))

    job_type = fields.String(required=True, validate=[
        And(
            Length(min=3, max=20, error="Job Type must be between 3 and 20 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ]*$', error="Job Type must start with a capital letter and contain only alphanumeric characters and spaces.")
        )
    ])
    job_location = fields.String(required=True, validate=[
        And(
            Length(min=1, max=50, error="Job Location must be between 1 and 50 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ]*$', error="Job Location must start with a capital letter and contain only alphanumeric characters and spaces.")
        )
    ])
    availability = fields.String(required=True, validate=[
    And(
        Length(min=1, max=50, error="Availability must be between 1 and 50 characters."),
        Regexp(r'^[A-Z][a-zA-Z0-9 ,\-]*$', error="Availability must start with a capital letter and contain only alphanumeric characters, commas, spaces, and hyphens.")
    )
])
    description = fields.String(required=True, validate=[Length(min=1, max=500, error="Description must be between 1 and 500 characters.")])
    class Meta:
        fields = ("job_id", "job_type", "job_location", "availability", "description", "date", "user", "jobrequests")
        ordered = True



jobpost_schema = JobpostSchema()
jobposts_schema = JobpostSchema(many=True)


