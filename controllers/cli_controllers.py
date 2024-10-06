from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.jobpost import Jobpost
from models.jobrequest import Jobrequest

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("seed")
def seed_tables():
    #create a list of user instances
    users = [
        User(
        email = "admin@email.com",
        user_name = "admin",
        name = "admin",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        location = "APAC",
        is_admin = True
    ),
    User(
        email = "test@email.com", 
        name = "Test",
        user_name = "test",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        location = "APAC"
    )]
    db.session.add_all(users)
    
    jobposts = [
        Jobpost(
        job_type = "sample_plumming",
        availability = "Monday-Friday 8am-5pm",
        description = "I am available to do all jobs relating to plumming",
        date = date.today(),
        job_location = "Sydney",

        user = users [0]
    ), Jobpost(
        job_type = "sample_movers",
        availability = "Weekends 8am-5pm",
        description = "Moving house? Let me help. I have a large truck and an assistant to help",
        date = date.today(),
        job_location = "Melbourne",

        user = users [1]
    )]


    db.session.add_all(jobposts)

    db.session.commit()

    print("Tables seeded!")


@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped!")