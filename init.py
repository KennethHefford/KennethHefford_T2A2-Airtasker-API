from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Initialize Flask extensions
db = SQLAlchemy()      # For database management
ma = Marshmallow()     # For object serialization/deserialization
bcrypt = Bcrypt()      # For hashing passwords
jwt = JWTManager()     # For handling JWT authentication
