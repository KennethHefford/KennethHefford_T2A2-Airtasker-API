from init import db, ma
from marshmallow import fields
from models.jobrequest import JobrequestSchema 
from marshmallow.validate import Length, Range, And, Regexp

class Review(db.Model):
    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)

    user_name = db.Column(db.String, db.ForeignKey("users.user_name", ondelete ='SET NULL'), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('jobrequests.request_id'), nullable=False)

    user = db.relationship("User", back_populates="reviews")
    jobrequest = db.relationship("Jobrequest", back_populates="reviews")


class ReviewSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["name"])
    jobrequest = fields.Nested(JobrequestSchema, only=["title"], dump_only=True)

    title = fields.String(required=True, validate=[
        And(
            Length(min=3, max=20, error="Title must be between 3 and 20 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 !]*$', error="Title must start with a capital letter and contain only alphanumeric characters, spaces, and exclamation marks.")
        )
    ])
    description = fields.String(required=True, validate=[Length(min=1, max=500, error="Description must be between 1 and 500 characters.")])
    rating = fields.Integer(required=True, validate=[Range(min=1, max=5, error="Rating must be between 1 and 5.")])

    class Meta:
        fields = ("review_id", "request_id", "title", "date", "description", "rating", "user", "jobrequest") 
        ordered = True

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)