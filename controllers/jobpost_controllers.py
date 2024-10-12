from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.jobpost import Jobpost, jobpost_schema, jobposts_schema
from models.jobrequest import Jobrequest
from models.review import Review
from controllers.jobrequest_controllers import jobrequests_bp

from utils import authorise_as_admin

jobposts_bp = Blueprint("jobposts", __name__, url_prefix="/jobposts")
# Register the jobrequests_bp blueprint - make all routes in jobrequest_controllers.py have the prefix /jobposts
jobposts_bp.register_blueprint(jobrequests_bp)



#/jobposts - GET - fetch all jobposts
@jobposts_bp.route("/")
def get_all_jobposts():
    stmt = db.select(Jobpost).order_by(Jobpost.date.desc())
    jobposts = db.session.scalars(stmt)
    return jobposts_schema.dump(jobposts)


#/jobposts/<id> - GET - fetch a specific jobpost
@jobposts_bp.route("/<int:job_id>", methods=["GET"])
def get_a_jobpost(job_id):
    stmt = db.select(Jobpost).filter_by(job_id=job_id)
    jobpost = db.session.scalar(stmt)
    if jobpost:
        return jobpost_schema.dump(jobpost)
    else:
        return {"error": f"Job post with ID {job_id} not found."}
    


#/jobposts - POST - create a new jobpost
@jobposts_bp.route("/", methods=["POST"])
@jwt_required()
def create_jobpost():
    body_data = jobpost_schema.load(request.get_json())
    jobpost = Jobpost(
        job_type=body_data.get("job_type"),
        availability=body_data.get("availability"),
        description=body_data.get("description"),
        date = date.today(),
        job_location = body_data.get("job_location"),
        user_name = get_jwt_identity()
    )
    
    db.session.add(jobpost)
    db.session.commit()
    
    return jobpost_schema.dump(jobpost), 201

#/jobposts/<id> - DELETE - delete a jobpost
@jobposts_bp.route("/<int:job_id>", methods=["DELETE"])
@jwt_required()
def delete_jobpost(job_id):
    # Get the current user's user_name from the JWT
    current_user_name = get_jwt_identity()
    
    # Check if user is admin
    is_admin = authorise_as_admin()
    
    # Fetch the job post from the database
    stmt = db.select(Jobpost).filter_by(job_id=job_id)
    jobpost = db.session.scalar(stmt)
    
    # If job post exists
    if jobpost:
        # If not admin or job post owner
        if not (is_admin or jobpost.user_name == current_user_name):
        # Return error message
            return {"error": "You are not authorised to delete job posts."}, 403
        
        # Set job_id to NULL for all completed job requests
        stmt = db.update(Jobrequest).where(Jobrequest.job_id == job_id, Jobrequest.completed == True).values(job_id=None)
        db.session.execute(stmt)

        # Delete job requests where completed is False
        stmt = db.delete(Jobrequest).where(Jobrequest.job_id == job_id, Jobrequest.completed == False)
        db.session.execute(stmt)

        # Delete the job post
        db.session.delete(jobpost)
        db.session.commit()
        # Return success message
        return {"message": f"Job {jobpost.job_type} deleted successfully!"}, 200
    else:
        # Return error message if job post not found
        return {"error": f"Job Post with job ID:{job_id} not found"}, 404
    


#/jobposts/<id> -PUT,PATCH -edit a jobpost
@jobposts_bp.route("/<int:job_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_jobpost(job_id):
    body_data = jobpost_schema.load(request.get_json(), partial=True)
    stmt = db.select(Jobpost).filter_by(job_id=job_id)
    jobpost = db.session.scalar(stmt)
    if jobpost:
        #if the user is not the owner of the jobpost
        if jobpost.user_name != get_jwt_identity():
            #return error message
            return {"error": "You are not authorised to edit this job post. Only owner can edit posts."}, 403

        #update the fields as required
        jobpost.job_type = body_data.get("job_type") or jobpost.job_type
        jobpost.availability = body_data.get("availability") or jobpost.availability
        jobpost.description = body_data.get("description") or jobpost.description
        jobpost.job_location = body_data.get("job_location") or jobpost.job_location
        db.session.commit()
        return jobpost_schema.dump(jobpost)
    else:
        return {"error": f"Job Post with ID {job_id}not found."}, 404
    
