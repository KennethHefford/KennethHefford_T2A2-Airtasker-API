from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

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
        return {"error": f"Job request with ID {job_id} does not found"}, 404
    


# Delete jobrequest only available if completed is == false
@jobrequests_bp.route("/<int:request_id>", methods=["DELETE"])
@jwt_required()
def delete_jobrequest(job_id, request_id):
    stmt = db.select(Jobrequest).filter_by(request_id=request_id)
    jobrequest = db.session.scalar(stmt)
    if jobrequest:
        if jobrequest.completed:
            return {"error": "Cannot delete a job request that has been completed."}, 403
        db.session.delete(jobrequest)
        db.session.commit()
        return {"message": f"Job Request with ID {request_id} has been withdrawn"}
    else:
        return {"error": f"Job Request with ID {request_id} does not exist"}, 404

# edit a job request
@jobrequests_bp.route("/<int:request_id>", methods=["PUT","PATCH"])
@jwt_required()
def edit_jobrequest(job_id, request_id):
    body_data = jobrequest_schema.load(request.get_json(), partial=True)

    stmt = db.select(Jobrequest).filter_by(request_id=request_id)
    jobrequest = db.session.scalar(stmt)

    if jobrequest:
        if jobrequest.completed:
            return {"error": "Cannot update a job request that has been completed."}, 403
        
        jobrequest.job_time = body_data.get("job_time", jobrequest.job_time)
        jobrequest.description = body_data.get("description", jobrequest.description)
        jobrequest.title = body_data.get("title", jobrequest.title)
        jobrequest.completed = body_data.get("completed", jobrequest.completed)
        jobrequest.date = date.today()
        db.session.commit()
        return jobrequest_schema.dump(jobrequest)
    else:
        return {"error": f"Job Request with ID {request_id} not found."}, 404