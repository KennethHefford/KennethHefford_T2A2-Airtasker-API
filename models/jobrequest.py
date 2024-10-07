from init import db, ma
from marshmallow import fields


class Jobrequest(db.Model):
    __tablename__ = "jobrequests"


    request_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_time = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False )
    title = db.Column(db.String, nullable=False )
    completed = db.Column(db.Boolean, default=False, nullable=False)
    

    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("jobposts.job_id"), nullable = False)


    user = db.relationship("User", back_populates="jobrequests")
    jobpost = db.relationship("Jobpost", back_populates = "jobrequests", foreign_keys=[job_id])

class JobrequestSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["name"])
    jobpost = fields.Nested('JobpostSchema', only=["job_id", "job_type", "job_location"], exclude=["jobrequests"])
    class Meta:
        fields = ("request_id", "job_time", "date", "description", "title", "completed", "user", "jobpost")

jobrequest_schema = JobrequestSchema()
jobrequests_schema = JobrequestSchema(many=True)