from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db

from models.jobpost import Jobpost, jobpost_schema, jobposts_schema
from controllers.jobrequest_controllers import jobrequests_bp
from utils import authorise_as_admin_or_user

# Create a Blueprint for job posts
jobposts_bp = Blueprint("jobposts", __name__, url_prefix="/jobposts")

# Register the job requests blueprint with the job posts blueprint
jobposts_bp.register_blueprint(jobrequests_bp)

# /jobposts - GET - Fetch all job posts
@jobposts_bp.route("/")
def get_all_jobposts():
    stmt = db.select(Jobpost).order_by(Jobpost.date.desc())  # Select all job posts ordered by date
    jobposts = db.session.scalars(stmt)  # Execute the query
    return jobposts_schema.dump(jobposts)  # Return serialized job posts

# /jobposts/<id> - GET - Fetch a specific job post by ID
@jobposts_bp.route("/<int:job_id>", methods=["GET"])
def get_a_jobpost(job_id):
    stmt = db.select(Jobpost).filter_by(job_id=job_id)  # Query for the specific job post
    jobpost = db.session.scalar(stmt)  # Get the job post
    if jobpost:
        return jobpost_schema.dump(jobpost)  # Return serialized job post
    else:
        return {"error": f"Job post with ID {job_id} not found."}, 404  # Return error if not found

# /jobposts - POST - Create a new job post
@jobposts_bp.route("/", methods=["POST"])
@jwt_required()  # Require JWT authentication
def create_jobpost():
    body_data = jobpost_schema.load(request.get_json())  # Load and validate the incoming data
    jobpost = Jobpost(
        job_type=body_data.get("job_type"),
        availability=body_data.get("availability"),
        description=body_data.get("description"),
        date=date.today(),  # Set the current date
        job_location=body_data.get("job_location"),
        user_name=get_jwt_identity()  # Get the current user's identity from the JWT
    )
    
    db.session.add(jobpost)  # Add the job post to the session
    db.session.commit()  # Commit the transaction
    
    return jobpost_schema.dump(jobpost), 201  # Return serialized job post with 201 status

# /jobposts/<id> - DELETE - Delete a job post by ID
@jobposts_bp.route('/<int:job_id>', methods=['DELETE'])
@jwt_required()  # Require JWT authentication
@authorise_as_admin_or_user  # Allow access to admins or resource owners
def delete_jobpost(job_id):
    stmt = db.select(Jobpost).filter_by(job_id=job_id)  # Find the job post in the database
    jobpost = db.session.scalar(stmt)  # Get the job post
    if jobpost:
        db.session.delete(jobpost)  # Delete the job post
        db.session.commit()  # Commit the transaction
        return {"message": f"Job post with ID {job_id} deleted successfully"}, 200  # Return success message
    else:
        return {"message": f"Job post with ID {job_id} not found"}, 404  # Return error if not found

# /jobposts/<id> - PUT, PATCH - Edit a job post
@jobposts_bp.route("/<int:job_id>", methods=["PUT", "PATCH"])
@jwt_required()  # Require JWT authentication
def update_jobpost(job_id):
    body_data = jobpost_schema.load(request.get_json(), partial=True)  # Load incoming data (partial update)
    stmt = db.select(Jobpost).filter_by(job_id=job_id)  # Query for the job post
    jobpost = db.session.scalar(stmt)  # Get the job post
    if jobpost:
        # Check if the current user is the owner of the job post
        if jobpost.user_name != get_jwt_identity():
            return {"error": "You are not authorized to edit this job post. Only the owner can edit posts."}, 403  # Return error if not authorized

        # Update fields as required
        jobpost.job_type = body_data.get("job_type") or jobpost.job_type
        jobpost.availability = body_data.get("availability") or jobpost.availability
        jobpost.description = body_data.get("description") or jobpost.description
        jobpost.job_location = body_data.get("job_location") or jobpost.job_location
        db.session.commit()  # Commit the transaction
        return jobpost_schema.dump(jobpost)  # Return the updated job post
    else:
        return {"error": f"Job post with ID {job_id} not found."}, 404  # Return error if not found
