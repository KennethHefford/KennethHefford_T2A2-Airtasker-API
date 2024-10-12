from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db

from models.review import Review, review_schema
from models.jobrequest import Jobrequest
from utils import authorise_as_admin

review_bp = Blueprint("reviews", __name__, url_prefix="/jobrequests/<int:request_id>/reviews")

# Only create review if job request is completed
@review_bp.route("/", methods=["POST"])
@jwt_required()
def create_review(request_id):
    body_data = review_schema.load(request.get_json())

    # Fetch the job request by its ID
    jobrequest = db.session.scalar(db.select(Jobrequest).filter_by(request_id=request_id))

    if jobrequest:
        # Check if the job request is completed
        if jobrequest.completed:  # Proceed only if the job is completed
            rating = body_data.get("rating")
            if rating is None:
                return {"error": "Rating is required."}, 400

            review = Review(
                date=date.today(),
                title=body_data.get("title"),
                rating=rating,
                description=body_data.get("description"),
                request_id=jobrequest.request_id,
                user_name=get_jwt_identity()
            )

            # Add and commit the session
            db.session.add(review)
            db.session.commit()

            # Return acknowledgement
            return review_schema.dump(review), 201
        else:
            return {"error": "Cannot create a review if the job has not been completed."}, 403
    else:
        return {"error": f"Job request with ID {request_id} does not exist."}, 404
    
# edit a review
@review_bp.route("/<int:review_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_review(request_id, review_id):
    # Load the data from the request body
    body_data = review_schema.load(request.get_json(), partial=True)

    # Fetch the review by its ID and request_id
    stmt = db.select(Review).filter_by(review_id=review_id, request_id=request_id)
    review = db.session.scalar(stmt)

    # If review exists
    if review:
        # Check if the current user is the owner of the review
        if review.user_name != get_jwt_identity():
            return {"error": "You are not authorised to edit this review. Only the owner can edit it."}, 403

        # Update the review fields
        review.title = body_data.get("title") or review.title
        review.rating = body_data.get("rating") or review.rating
        review.description = body_data.get("description") or review.description

        # Commit the changes to the database
        db.session.commit()
        return review_schema.dump(review), 200
    else:
        # Return error message if review not found
        return {"error": f"Review with ID {review_id} does not exist."}, 404

# Only admin can delete a review for inappropriate content
@review_bp.route("/<int:review_id>", methods=["DELETE"])
@jwt_required()
@authorise_as_admin
def delete_review(request_id, review_id):
    # Fetch the review by its ID and request_id
    stmt = db.select(Review).filter_by(review_id=review_id, request_id=request_id)
    review = db.session.scalar(stmt)
    
    # If review exists
    if review:
        # Delete the review
        db.session.delete(review)
        db.session.commit()
        return {"message": f"Review with ID {review_id} has been deleted successfully."}, 200
    else:
        # Return error message if review not found
        return {"error": f"Review with ID {review_id} does not exist."}, 404