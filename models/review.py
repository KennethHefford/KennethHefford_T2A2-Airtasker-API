from init import db, ma
from marshmallow import fields
from sqlalchemy import CheckConstraint
from models.jobrequest import JobrequestSchema  # Ensure JobrequestSchema is imported

class Review(db.Model):
    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)

    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('jobrequests.request_id'), nullable=False)

    user = db.relationship("User", back_populates="reviews")
    jobrequest = db.relationship("Jobrequest", back_populates="reviews")

    # To make sure ratings are consistent 1-5
    __table_args__ = (
        CheckConstraint('rating >= 1', name='check_rating_gte_1'),
        CheckConstraint('rating <= 5', name='check_rating_lte_5'),
    )

class ReviewSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=["name"])
    jobrequest = fields.Nested('JobrequestSchema', only=["request_id"], exclude=["reviews"])

    class Meta:
        fields = ("review_id", "request_id", "title", "date", "description", "rating", "user")
        ordered = True

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)