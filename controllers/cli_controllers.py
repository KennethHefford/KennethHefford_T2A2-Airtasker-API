from datetime import date
from flask import Blueprint
from init import db, bcrypt

from models.user import User
from models.jobpost import Jobpost
from models.jobrequest import Jobrequest
from models.review import Review

# Create a Blueprint for database commands
db_commands = Blueprint("db", __name__)

# Command to create all tables
@db_commands.cli.command("create")
def create_tables():
    db.create_all()  # Create all tables in the database
    print("Tables created!")

# Command to seed the database with initial data
@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of user instances
    users = [
        User(
            email="admin@email.com",
            user_name="admin",
            name="admin",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            location="APAC",
            is_admin=True
        ),
        User(
            email="test@email.com",
            name="Test",
            user_name="test",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            location="APAC"
        )
    ]
    
    db.session.add_all(users)  # Add users to the session

    # Create job post instances
    jobposts = [
        Jobpost(
            job_type="sample_plumbing",
            availability="Monday-Friday 8am-5pm",
            description="I am available to do all jobs relating to plumbing",
            date=date.today(),
            job_location="Sydney",
            user=users[0]  # Associate the first user (admin) with this job post
        ),
        Jobpost(
            job_type="sample_movers",
            availability="Weekends 8am-5pm",
            description="Moving house? Let me help. I have a large truck and an assistant to help",
            date=date.today(),
            job_location="Melbourne",
            user=users[1]  # Associate the second user (test) with this job post
        )
    ]

    db.session.add_all(jobposts)  # Add job posts to the session

    # Create job request instances
    jobrequests = [
        Jobrequest(
            job_time="Friday 9am",
            description="I need help with my tap; it won't stop leaking.",
            title="Leaky tap",
            completed=False,
            date=date.today(),
            user=users[0],  # User requesting help
            jobpost=jobposts[0]  # Link to the plumbing job post
        ),
        Jobrequest(
            job_time="Saturday 9am",
            description="I am moving house",
            title="Moving House",
            completed=True,
            date=date.today(),
            user=users[1],  # User requesting help
            jobpost=jobposts[1]  # Link to the moving job post
        )
    ]
    
    db.session.add_all(jobrequests)  # Add job requests to the session

    # Create review instances
    reviews = [
        Review(
            user=users[1],  # User who wrote the review
            jobrequest=jobrequests[1],  # Link to the corresponding job request
            title="Best Service",
            description="The movers were very efficient, and none of my furniture was damaged.",
            rating=5,
            date=date.today(),
        )
    ]
    
    db.session.add_all(reviews)  # Add reviews to the session
    db.session.commit()  # Commit the session to save changes

    print("Tables seeded!")  # Confirmation message


# Command to drop all tables
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()  # Drop all tables in the database
    print("Tables dropped!")  # Confirmation message
