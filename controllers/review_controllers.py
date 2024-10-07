from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.review import Review, review_schema, reviews_schema
from models.jobrequest import Jobrequest

review_bp = Blueprint("reviews", __name__, url_prefix="/jobrequests/<int:request_id>/reviews/")

# Only create review if job request is completed
@review_bp.route("/", methods=["POST"])
@jwt_required()
def create_review(request_id):
    body_data = request.get_json()

    # Fetch the job request by its ID
    jobrequest = db.session.scalar(db.select(Jobrequest).filter_by(request_id=request_id))

    if jobrequest:
        # Check if the job request is completed
        if jobrequest.completed:  # Proceed only if the job is completed
            rating = body_data.get("rating")
            if rating is None:
                return {"error": "Rating is required."}, 400
            
            if not (1 <= rating <= 5):
                return {"error": "Rating must be between 1 and 5."}, 400
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
    body_data = request.get_json()

    # Fetch the review by its ID
    stmt = db.select(Review).filter_by(review_id=review_id)
    review = db.session.scalar(stmt)

    if review:
        # Check if the review belongs to the job request
        if review.request_id != request_id:
            return {"error": "Review does not belong to this job request."}, 403

        # Update the review fields
        review.title = body_data.get("title", review.title)
        review.rating = body_data.get("rating", review.rating)
        review.description = body_data.get("description", review.description)

        # Commit the changes to the database
        db.session.commit()
        return review_schema.dump(review)
    else:
        return {"error": f"Review with ID {review_id} does not exist."}, 404
    
# Reviews are permanent and cannot be deleted