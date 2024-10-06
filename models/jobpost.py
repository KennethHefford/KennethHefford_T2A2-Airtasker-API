from init import db, ma
from marshmallow import fields

class Jobpost(db.Model):
    __tablename__ = "jobposts"


    availability = db.Column(db.String, nullable=False)
    job_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_type = db.Column(db.String, primary_key=True, nullable = False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False )
    job_location = db.Column(db.String, nullable=False )
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    # name = db.Column(db.String, db.ForeignKey("users.name"), nullable=False)
    # location = db.Column(db.String, db.ForeignKey("users.location"), nullable=False)


    user = db.relationship('User', back_populates ='jobposts')
    jobrequests = db.relationship("Jobrequest", back_populates="jobpost")

class JobpostSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["name"])
    jobrequests = fields.List(fields.Nested('JobrequestSchema', exclude =['jobrequest']))
    class Meta:
        fields = ("user", "job_id", "job_type", "job_location", "availability", "description", "date", "jobrequests")
        ordered = True

#  fields = ("user_name", "name", "location", "availability", "job_id", "job_type", "date")

jobpost_schema = JobpostSchema()
jobposts_schema = JobpostSchema(many=True)


