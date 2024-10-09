from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils import authorise_as_admin
from init import db
from models.jobrequest import Jobrequest, jobrequest_schema, jobrequests_schema
from models.jobpost import Jobpost
jobrequests_bp = Blueprint("jobrequests", __name__, url_prefix="/<int:job_id>/jobrequests")


#create job request route
@jobrequests_bp.route("/", methods = ["POST"])
@jwt_required()
def create_jobrequest(job_id):
    #get the jobrequest info from the body
    body_data = jobrequest_schema.load(request.get_json())
    #fetch the jobpost with id=job_id
    stmt = db.select(Jobpost).filter_by(job_id=job_id)
    jobpost = db.session.scalar(stmt)
    #if jobpost exist 
    if jobpost:
        #create an instance of the jobrequest model
        jobrequest = Jobrequest (
        job_time=body_data.get("job_time"),
        description=body_data.get("description"),
        date = date.today(),
        title = body_data.get("title"),
        completed = body_data.get("completed", False),
        job_id = jobpost.job_id,
        user_name = get_jwt_identity()
        )
        #add and commit the session
        db.session.add(jobrequest)
        db.session.commit()
        #return acknowledgement
        return jobrequest_schema.dump(jobrequest), 201
    else:
        return {"error": f"Job request with ID {job_id} not found"}, 404
    


# Delete jobrequest only available if completed is == false
@jobrequests_bp.route("/<int:request_id>", methods=["DELETE"])
@jwt_required()
def delete_jobrequest(request_id):
    # Get the current user's user_name from the JWT
    current_user_name = get_jwt_identity()
    
    # Check if user is admin
    is_admin = authorise_as_admin()
    
    # Fetch the job request from the database
    stmt = db.select(Jobrequest).filter_by(request_id=request_id)
    jobrequest = db.session.scalar(stmt)
    
    # If job request exists
    if jobrequest:
        # If the job request is completed, it cannot be deleted
        if jobrequest.completed:
            return {"error": "Cannot delete a job request that has been completed."}, 403
        
        # If not admin or job request owner
        if not (is_admin or jobrequest.user_name == current_user_name):
            # Return error message
            return {"error": "You are not authorised to delete this job request."}, 403
        
        # Delete the job request
        db.session.delete(jobrequest)
        db.session.commit()
        # Return success message
        return {"message": f"Job Request with ID {request_id} has been withdrawn"}, 200
    else:
        # Return error message if job request not found
        return {"error": f"Job Request with ID {request_id} does not exist"}, 404

@jobrequests_bp.route("/<int:request_id>", methods=["PUT", "PATCH"])
@jwt_required()
<<<<<<< HEAD
def edit_jobrequest(job_id, request_id):
    body_data = jobrequest_schema.load(request.get_json(), partial=True)

=======
def edit_jobrequest(request_id):
    # Load the data from the request body
    body_data = jobrequest_schema.load(request.get_json(), partial=True)
    
    # Fetch the job request from the database
>>>>>>> feature/validation
    stmt = db.select(Jobrequest).filter_by(request_id=request_id)
    jobrequest = db.session.scalar(stmt)
    
    # If job request exists
    if jobrequest:
        # Check if the current user is the owner of the job request
        if jobrequest.user_name != get_jwt_identity():
            return {"error": "You are not authorised to edit this job request. Only the owner can edit it."}, 403
        
        # Check if the job request is completed
        if jobrequest.completed:
            return {"error": "Cannot update a job request that has been completed."}, 403
        
        # Update the job request fields
        jobrequest.job_time = body_data.get("job_time") or jobrequest.job_time
        jobrequest.description = body_data.get("description") or jobrequest.description
        jobrequest.title = body_data.get("title") or jobrequest.title
        jobrequest.completed = body_data.get("completed") or jobrequest.completed
        jobrequest.date = date.today()
        
        # Commit the changes to the database
        db.session.commit()
        
        # Return the updated job request
        return jobrequest_schema.dump(jobrequest), 200
    else:
        # Return error message if job request not found
        return {"error": f"Job Request with ID {request_id} not found."}, 404