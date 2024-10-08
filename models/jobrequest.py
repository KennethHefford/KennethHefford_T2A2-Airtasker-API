from init import db, ma
from marshmallow import fields

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

    class Meta:
        fields = ("title","request_id", "job_time", "date", "description", "completed", "user", "jobpost", "reviews")
        ordered = True

jobrequest_schema = JobrequestSchema()
jobrequests_schema = JobrequestSchema(many=True)