from flask import Blueprint
from init import db, bcrypt
from models.user import User

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
        user_email = "admin@email.com",
        user_name = "admin",
        name = "admin",
        user_password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        user_location = "APAC",
        is_admin = True
    ),
    User(
        user_email = "usera@email.com", 
        name = "User A",
        user_name = "user_a",
        user_password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        user_location = "APAC"
    )]
    db.session.add_all(users)

    db.session.commit()

    print("Tables created!")


@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped!")