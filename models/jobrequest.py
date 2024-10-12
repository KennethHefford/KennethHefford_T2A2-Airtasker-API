from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Jobrequest(db.Model):
    __tablename__ = "jobrequests"

    request_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_time = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("jobposts.job_id"), nullable=False)

    user = db.relationship("User", back_populates="jobrequests")
    jobpost = db.relationship("Jobpost", back_populates="jobrequests", foreign_keys=[job_id])
    reviews = db.relationship('Review', back_populates='jobrequest')

class JobrequestSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["name"])
    jobpost = fields.Nested('JobpostSchema', only=["job_id", "job_type", "job_location"], exclude=["jobrequests"])
    reviews = fields.Nested('ReviewSchema', many=True, exclude=["jobrequest"])

    title = fields.String(required=True, validate=[
        And(
            Length(min=3, max=30, error="Title must be between 3 and 30 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 ]*$', error="Title must start with a capital letter and contain only alphanumeric characters and spaces.")
        )
    ])
    description = fields.String(required=True, validate=[Length(min=1, max=500, error="Description must be between 1 and 500 characters.")])
    job_time = fields.String(required=True, validate=[
    And(
        Length(min=1, max=50, error="Job Time must be between 1 and 50 characters."),
        Regexp(r'^[a-zA-Z0-9 ,\-]*$', error="Job Time must contain only alphanumeric characters, spaces, commas, and hyphens.")
    )])
    completed = fields.Boolean(required=True)

    class Meta:
        fields = ("title","request_id", "job_time", "date", "description", "completed", "user", "jobpost", "reviews")
        ordered = True

jobrequest_schema = JobrequestSchema()
jobrequests_schema = JobrequestSchema(many=True)