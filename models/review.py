from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Range, And, Regexp

# Review model representing the 'reviews' table
class Review(db.Model):
    __tablename__ = "reviews"  # Define the table name

    # Table columns
    review_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)

    # Foreign keys
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('jobrequests.request_id'), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="reviews")
    jobrequest = db.relationship("Jobrequest", back_populates="reviews")


# Review Schema for serializing and deserializing Review data
class ReviewSchema(ma.Schema):
    # Nested schemas for related user and jobrequest data
    user = fields.Nested('UserSchema', only=["name"])
    jobrequest = fields.Nested('JobrequestSchema', only=["title", "request_id"])

    # Title validation (length and format)
    title = fields.String(required=True, validate=[
        And(
            Length(min=3, max=20, error="Title must be between 3 and 20 characters."),
            Regexp(r'^[A-Z][a-zA-Z0-9 !]*$', error="Title must start with a capital letter and contain only alphanumeric characters, spaces, and exclamation marks.")
        )
    ])

    # Description validation (length)
    description = fields.String(required=True, validate=[
        Length(min=1, max=500, error="Description must be between 1 and 500 characters.")
    ])

    # Rating validation (range)
    rating = fields.Integer(required=True, validate=[
        Range(min=1, max=5, error="Rating must be between 1 and 5.")
    ])

    # Meta class to define fields to include and enforce ordering
    class Meta:
        fields = ("review_id", "request_id", "title", "date", "description", "rating", "user", "jobrequest")
        ordered = True  # Ensures fields are returned in the specified order


# Schemas for handling single or multiple review objects
review_schema = ReviewSchema()  # Schema for a single review
reviews_schema = ReviewSchema(many=True)  # Schema for a list of reviews
