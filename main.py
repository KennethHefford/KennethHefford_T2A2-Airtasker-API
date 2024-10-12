import os
from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt
from controllers.cli_controllers import db_commands
from controllers.auth_controllers import auth_bp
from controllers.jobpost_controllers import jobposts_bp
from controllers.review_controllers import review_bp
from controllers.jobrequest_controllers import jobrequests_bp


def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False  # Keep JSON key order as defined
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    # Initialize app with necessary extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Global handler for validation errors
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    # Register blueprints for CLI, authentication, and other functionalities
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(jobposts_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(jobrequests_bp)

    return app
