# Airtasker API - By Kenneth Hefford
## GitHub: https://github.com/KennethHefford/KennethHefford_T2A2-Airtasker-API.git

## Introduction

The Airtasker API web server developed in this project adeptly handles job postings, job requests, and user reviews. Leveraging core server concepts such as routing and data communication between users and a database, this API server is built using Flask and integrates seamlessly with a relational database via SQLAlchemy ORM. It offers a structured, efficient approach to managing CRUD operations for job-related data, ensuring secure and organised data management. This project showcases the ability to develop a robust web API server that centralises job-related data, streamlining the process for users to discover and manage job opportunities and reviews effortlessly.


### How to Start the Server

1.**Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```
2.**Install Dependencies**

```sh
pip install -r requirements.txt
```

3.**Set Up Environment Variables: Create a .env file in the root directory and add the following environment variables**

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///your_database.db
```

4.**Initialise the Database**

```sh
flask db create
```

5.**Seed the Database**

```sh
flask db seed
```

6.**Run the Server**

```sh
flask run
```

7.**Access the API with the URL http://127.0.0.1:5000.**
Insomnia was used. However, PostMan can be used.

### Database Management
```sh
flask db create
```
To Create the Database
```sh
flask db seed
```
To Seed the tables

```sh
flask db drop
```
To drop the Database

### R1: Problem Explanation

The gig economy is rapidly growing, with platforms like Airtasker connecting people who need tasks done with those looking to earn money by completing those tasks. Managing job postings, requests, and reviews efficiently is crucial for both task posters and taskers. Traditional methods of handling job-related data can be cumbersome, prone to errors, and lack centralised management, leading to inefficiencies and missed opportunities.

**Problem**:

- **Fragmented Data Management**: Job postings, requests, and reviews are often scattered across different platforms, making it difficult for users to find and manage relevant information.

- **Inefficient Job Matching**: Users struggle to find individuals with the right skills for specific tasks, slowing down the hiring process and reducing opportunities.

- **Lack of Security and Trust**: Many online platforms face issues with identity theft and trustworthiness, making it risky for freelancers and clients to engage with one another.

**Solution**:
This app solves the problem of managing job postings, job requests, and user reviews in a structured and efficient manner. It provides a web API that allows users to create, read, update, and delete job-related data, ensuring secure and organised data management. By centralising job-related data, it simplifies the process for users to find and manage job opportunities and reviews. Additionally, it allows customers to find people with particular skills, so they can be requested directly for specific tasks. When the task is completed, customers can add a review.

**How the App Addresses the Problem**:

- **Centralised Management**: By centralising job postings, requests, and reviews, the app makes it easier for users to access and manage all job-related data from a single platform, simplifying the process of finding and managing job opportunities.
- **Efficient Job Matching**: The app allows customers to find individuals with particular skills, so they can be requested directly for specific tasks. This makes the hiring process faster and more efficient.
- **Enhanced Security**: Using JWT authentication and Flask-Bcrypt for password hashing ensures that user data is securely managed and protected from unauthorised access, fostering trust and reliability.


**Objective References**:
- According to a survey by Upwork, 59 million Americans performed freelance work in 2020, contributing $1.2 trillion to the economy. By providing a streamlined and efficient API, this app aims to support the growing freelance economy by making it easier for freelancers to find and manage job opportunities.
- According to a report by the Federal Trade Commission (FTC), identity theft affected 1.4 million people in 2020, with many cases involving online platforms. By implementing robust security and identity verification measures, this app helps protect freelancers and clients from identity theft, thereby increasing trust and reliability on the platform.
- Airtasker reported that over 2 million people use their platform to outsource tasks and find work. Efficiently managing job-related data is crucial for maintaining user satisfaction and operational efficiency on such platforms, ensuring that both task posters and taskers have a seamless experience.

By addressing these key issues, the app not only enhances the user experience but also contributes to a more efficient and secure gig economy ecosystem.

### R2: Task Allocation and Tracking

Trello was used as a program management team. I utilised Trello to ensure that all tasks were organised and managed efficiently throughout the project's lifecycle. The Trello board was divided into three primary lists: **To Do**, **Doing**, and **Done**. This structure facilitated clear visibility of task progress and helped maintain focus on current priorities.

[Airtasker API Trello Board](https://trello.com/b/sxCBTjo9)

#### Trello Board Structure:
- **To Do**: This list contained all tasks that were yet to be started. Each task card included descriptions and individual tasks relevant to the card were in the comments.
- **Doing**: Tasks that were actively being worked on were moved to this list. This helped in tracking the ongoing work and ensuring that focus was maintained on current tasks.
- **Done**: Completed tasks were moved to this list. The final comment will state that the task was fully checked and ready to move into this list.

#### Example of Task Tracking:
- **To Do**: Define API endpoints, Design database schema, Set up Flask environment
- **Doing**: Implement user authentication, Develop job post endpoints
- **Done**: Create user model, Set up JWT authentication, Implement CRUD operations for job posts

#### Usage:
Throughout the project, Trello was used to manage and track tasks. Below are some screenshots of some Trello Trello Cards at different stages of the project:

![Trello Board - Initial Setup](../docs/early%20trello.png)
*Initial setup of the Trello board with tasks categorised into To Do, Doing, and Done lists.*

![Trello Board - Mid Project](../docs/mid%20trello.png)
*Mid-project progress showing tasks being moved from To Do to Doing and Done lists.*

![Trello Board - Project Completion](../docs/late%20trello.png)
*Final state of the Trello board tasks in the Done list, indicating project completion.*

Regular reviews of the Trello board were conducted to ensure that tasks were on track and to address any blockers promptly. This systematic approach to task management ensured that the project stayed organised and on schedule, ultimately contributing to its successful completion.

By using Trello extensively and methodically throughout the project, I was able to maintain a high level of organisation and efficiency, ensuring that all tasks were completed in a timely manner.

### R3: Third-Party Services, Packages, and Dependencies

This project leverages several third-party services, packages, and dependencies to ensure robust functionality, security, and efficiency. Below is a detailed description of each:

- **Flask**: A micro web framework used to build the web server. Flask provides the essential tools and features needed to create a web application, including routing, request handling, and templating. Its simplicity and flexibility make it an ideal choice for developing RESTful APIs.

- **Flask-SQLAlchemy**: An ORM (Object-Relational Mapping) library for SQL databases. Flask-SQLAlchemy simplifies database interactions by allowing developers to work with Python objects instead of writing raw SQL queries. It supports various database backends and integrates seamlessly with Flask.

- **Flask-Marshmallow**: Used for object serialisation/deserialisation. Flask-Marshmallow works in conjunction with Marshmallow to convert complex data types, such as objects, into native Python data types that can be easily rendered into JSON. It also handles data validation and formatting.

- **Flask-Bcrypt**: For hashing passwords. Flask-Bcrypt provides bcrypt hashing utilities for Flask applications, ensuring that user passwords are stored securely. Bcrypt is a robust hashing algorithm that includes a salt to protect against rainbow table attacks.

- **Flask-JWT-Extended**: For handling JWT (JSON Web Token) authentication. Flask-JWT-Extended adds support for secure user authentication using JWTs. It provides various features, including token creation, token refreshing, and token revocation, to manage user sessions securely.

- **Marshmallow**: For data validation and serialisation. Marshmallow is a library that helps convert complex data types to and from Python data types. It is used extensively for input validation, ensuring that the data received by the API is correctly formatted and meets the required criteria.

- **SQLAlchemy**: The core SQL toolkit and ORM used by Flask-SQLAlchemy. SQLAlchemy provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access.

- **Psycopg2**: A PostgreSQL adapter for Python. Psycopg2 is used to connect to and interact with PostgreSQL databases. It provides a robust and efficient interface for executing SQL commands and managing database transactions.

- **PostgreSQL**: An open-source relational database management system. PostgreSQL is known for its robustness, extensibility, and standards compliance. It supports a wide range of data types and advanced features such as transactions, foreign keys, and subqueries, making it an ideal choice for complex applications.

- **Datetime**: A standard Python library used for manipulating dates and times. It is used in this project to handle date-related operations, such as setting the date for job posts and reviews.

- **Insomnia**: A  HTTP and GraphQL client used for testing and debugging APIs. Insomnia was used extensively throughout the development process to test API endpoints, ensuring they functioned correctly and returned the expected responses. It provides a user-friendly interface for making HTTP requests and viewing responses, which greatly aids in the development and debugging of APIs.

These dependencies collectively contribute to the functionality, security, and efficiency of the application. By leveraging these third-party packages, the project ensures a high standard of code quality and performance, while also simplifying development and maintenance tasks.


### R4: Database System Benefits and Drawbacks

#### Functions Provided by the API:

1. **User Management**:
   - **Register User**: Allows new users to register by providing their details.
   - **Login User**: Authenticates users and provides a JWT token for secure access.
   - **Edit User**: Enables users to update their profile information.
   - **Delete User**: Allows users to delete their accounts.

2. **Job Post Management**:
   - **Create Job Post**: Allows users to create new job posts.
   - **Get All Job Posts**: Fetches all job posts, providing a centralised view.
   - **Get Job Post by ID**: Retrieves a specific job post by its ID.
   - **Update Job Post**: Enables users to update existing job posts.
   - **Delete Job Post**: Allows users to delete job posts.

3. **Job Request Management**:
   - **Create Job Request**: Allows users to create job requests for specific job posts.
   - **Update Job Request**: Enables users to update existing job requests.
   - **Delete Job Request**: Allows users to delete job requests.

4. **Review Management**:
   - **Create Review**: Allows users to create reviews for completed job requests.
   - **Update Review**: Enables users to update existing reviews.
   - **Delete Review**: Allows admins to delete reviews for inappropriate content.

#### Benefits:

- **Centralised Management**: The API centralises job postings, job requests, and reviews, making it easier for users to access and manage all job-related data from a single platform.
- **Efficiency**: The API automates CRUD (Create, Read, Update, Delete) operations for job-related data, reducing manual effort and minimising errors.
- **Security**: The API uses JWT (JSON Web Token) authentication and Flask-Bcrypt for password hashing, ensuring that user data is securely managed and protected from unauthorised access.
- **Scalability**: The API is designed to handle a growing number of users and data, making it scalable for future expansion.
- **Flexibility**: The API supports various endpoints for different operations, providing flexibility for users to interact with the system in multiple ways.
- **Admin and User Privileges**: The API distinguishes between admin and user privileges. Admins have the ability to delete everything, including users, job posts, job requests, and reviews. Users can delete everything except reviews. Reviews can only be deleted by admins if the content of the review is deemed inappropriate.
- **Review Ratings**: Review ratings can only be posted as integers between 1 and 5, ensuring a standardised rating system.
- **Global Error Handling**: The API includes global error handling to catch and manage exceptions consistently across all endpoints. This helps in providing more informative error messages and maintaining the stability of the application.



#### Drawbacks:

- **Testing and Debugging**: Testing and debugging the API can be challenging, especially when dealing with complex interactions between different endpoints and data models.
- **History of Completed Job Requests and Reviews**: Implementing a feature to maintain the history of completed job requests and reviews proved challenging. Issues such as integrity errors, programming errors, interface errors, detached instance errors, and not null violations were encountered. Additionally, the lack of skillset to rectify these issues prevented the successful implementation of this feature.
- **User Deletion Handling**: Attempting to change the output of fields when deleting a user presented several challenges. The goal was to retain relevant fields in job requests and reviews while updating user information to indicate deletion. This included setting the user name to `[Deleted user]` with a unique integer suffix, changing the location to "not available," updating the description to "this job post has been deleted," and maintaining the job type for context. The email was also to be changed to `deleted@deleted.com` with the same integer suffix. However, implementing this feature led to various issues, including integrity errors, programming errors, interface errors, detached instance errors, and not null violations. The lack of relevant skillset to fix these issues prevented the successful implementation of this feature.
- **Job Post Deletion Handling**: Similar to user deletion, handling job post deletion involved updating related job requests and reviews to maintain context while indicating that the job post was deleted. The job title was to be set to `[Deleted job post]` with a unique integer suffix, and the description was to be updated to "this job post has been deleted." However, this process encountered similar issues, such as integrity errors, programming errors, interface errors, detached instance errors, and not null violations. The lack of relevant skillset to fix these issues prevented the successful implementation of this feature.

### R5: ORM Features, Purpose, and Functionalities

**SQLAlchemy** is a toolkit for working with databases in Python. 

#### Features

- **ORM (Object-Relational Mapping)**: Maps Python classes to database tables, allowing you to interact with the database using Python objects.
- **SQL Expression Language**: Provides a SQL abstraction layer, enabling you to construct complex SQL queries using Python constructs.
- **Schema Generation**: Automatically generates database schemas from your Python classes.
- **Session Management**: Manages transactions and session lifecycle, making database operations easier and safer.
- **Database Agnostic**: Works with multiple database backends (e.g., SQLite, PostgreSQL, MySQL, Oracle).
- **Relationship Handling**: Easily define and manage relationships between tables using foreign keys.
- **Advanced Query Constructs**: Support for common SQL patterns and database functions.

#### Purpose

SQLAlchemy serves as an essential intermediary between Python applications and relational databases. By simplifying the complexities of SQL, it streamlines database interactions, making them more accessible and intuitive for Python developers.

#### Functionality

- **Database Connection**: Connect to different databases using a unified interface.
- **Define Models**: Create Python classes representing database tables and their relationships.
- **CRUD Operations**: Simplify Create, Read, Update, and Delete operations using Python objects.
- **Querying**: Construct and execute complex queries using a fluent API.
- **Transactions**: Manage database transactions and ensure data consistency.
- **Schema Management**: Create and modify database schemas from Python code.
- **Relationships**: Define and handle relationships between different tables.
- **Migration**: Manage schema changes and migrations seamlessly.

### Examples from the Airtasker API Webserver

#### Object-Relational Mapping.
Define models using Python classes. This feature allows developers to define database tables and their relationships using Python classes, making the code more intuitive and easier to manage.

```python
# user.py

# User Model representing the 'users' table in the database
class User(db.Model):
    __tablename__ = "users"  # Define the table name

    # Table columns
    user_name = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships with other tables
    jobposts = db.relationship("Jobpost", back_populates="user", cascade="all, delete-orphan")
    jobrequests = db.relationship("Jobrequest", back_populates="user", cascade="all, delete-orphan")
    reviews = db.relationship('Review', back_populates='user', cascade="all, delete-orphan")
```


#### CRUD Operations

Performing Create, Read, Update, and Delete (CRUD) operations becomes straightforward and intuitive with SQLAlchemy. Developers can manipulate database records using Python objects, making the process feel more like working with regular Python data structures instead of complex SQL queries. This feature significantly eases database interactions, offering a more natural and efficient way to handle data.

```python
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Update user information
@auth_bp.route("/users/<string:user_name>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(user_name):
    # Load user data from the request body
    body_data = UserSchema().load(request.get_json(), partial=True)

    # Fetch the user by username
    stmt = db.select(User).filter_by(user_name=user_name)
    user = db.session.scalar(stmt)

    # If user exists, update their information
    if user:
        # Check if the requester is the account owner
        if user.user_name != get_jwt_identity():
            return {"error": "You are not authorised to edit this user. Only the owner can edit their information."}, 403

        # Update user fields if provided
        user.name = body_data.get("name") or user.name
        user.email = body_data.get("email") or user.email
        user.location = body_data.get("location") or user.location
        if body_data.get("password"):
            user.password = bcrypt.generate_password_hash(body_data.get("password")).decode("utf-8")

        # Commit changes to the database
        db.session.commit()

        # Return the updated user data
        return user_schema.dump(user), 200

    # Return error message if user not found
    return {"error": "User not found"}, 404
```


### R6: Entity Relationship Diagram (ERD)

![Airtasker Entity Relationship Diagram](../docs/Airtasker%20ERD.png)

**Overview**:
1. **User**: Represents users of the application.
2. **Jobpost**: Represents job postings created by users.
3. **Jobrequest**: Represents job requests made by users.
4. **Review**: Represents reviews given by users for job requests.

The relationships between these models ensure that data is logically organised, aiding in efficient database design and queries.

#### Normalisation Overview

Normalisation is the process of organising the fields and tables of a relational database to minimise redundancy and dependency. The provided ERD adheres to normalisation principles, specifically up to the Third Normal Form (3NF).

1. **First Normal Form (1NF)**:
   - Each table has a primary key.
   - Each column contains atomic (indivisible) values.
   - Each column contains values of a single type.

2. **Second Normal Form (2NF)**:
   - The database is in 1NF.
   - All non-key attributes are fully functional dependent on the primary key.

3. **Third Normal Form (3NF)**:
   - The database is in 2NF.
   - All attributes are functionally dependent only on the primary key.

### Comparison to Other Levels of Normalisation

#### **Denormalised Form**:
In a denormalised form, tables like `User` and `Jobpost` might be combined into one. This can lead to redundancy, as user information would be repeated for each job post they create.
- **Example**:
```plaintext
| user_name   | name     | email             | location | job_id | job_type    | job_location |
|-------------|----------|-------------------|----------|--------|-------------|--------------|
| ben_lane    | Ben      | ben@example.com   | Sydney   | 1      | Plumber     | Sydney       |
| jane_smith  | Jane     | jane@example.com  | Brisbane | 2      | Electrician | Brisbane     |

```

#### **First Normal Form (1NF)**:
In 1NF, each column contains atomic values, and each column contains values of a single type. However, redundancy may still occur.
- **Example**:
```plaintext
| user_name   | job_ids |
|-------------|---------|
| ben_lane    | 1       |
| jane_smith  | 2       |
```
#### **Second Normal Form (2NF)**:
In 2NF, partial dependencies are removed, ensuring that all non-key attributes are fully functional dependent on the primary key.
- **Example**:
```plaintext
| user_name   | name    | email            | location |
|-------------|---------|------------------|----------|
| ben_lane    | Ben     | ben@example.com  | Sydney   |
| jane_smith  | Jane    | jane@example.com | Brisbane |

| job_id | job_type    | job_location | user_name   |
|--------|-------------|--------------|-------------|
| 1      | Plumber     | Melbourne    | sally_lane  |
| 2      | Electrician | Perth        | jane_smith  |
```

#### **Third Normal Form (3NF)**:
In 3NF, transitive dependencies are removed, ensuring that all attributes are functionally dependent only on the primary key.
- **Example**:
```plaintext
| user_name   | name    | email             | location |
|-------------|---------|-------------------|----------|
| sally_lane  | Sally   | sally@example.com | Sydney   |
| jane_smith  | Jane    | jane@example.com  | Brisbane |

| job_id | job_type    | job_location | user_name   |
|--------|-------------|--------------|-------------|
| 1      | Plumber     | Melbourne    | sally_lane  |
| 2      | Electrician | Perth        | jane_smith  |
```

### R7: Implemented Models and Relationships

1. **User**:
   - **Relationships**: 
     - **Jobposts**: One-to-Many (A user can create multiple job posts)
     - **Jobrequests**: One-to-Many (A user can make multiple job requests)
     - **Reviews**: One-to-Many (A user can write multiple reviews)

```python
   # user.py

   class User(db.Model):
       __tablename__ = "users"  # Define the table name

       # Table columns
       user_name = db.Column(db.String, primary_key=True, nullable=False, unique=True)
       name = db.Column(db.String, nullable=False)
       email = db.Column(db.String, nullable=False, unique=True)
       location = db.Column(db.String, nullable=False)
       password = db.Column(db.String, nullable=False)
       is_admin = db.Column(db.Boolean, default=False)

       # Relationships with other tables
       jobposts = db.relationship("Jobpost", back_populates="user", cascade="all, delete-orphan")
       jobrequests = db.relationship("Jobrequest", back_populates="user", cascade="all, delete-orphan")
       reviews = db.relationship('Review', back_populates='user', cascade="all, delete-orphan")
```


2. **Jobpost**:
   - **Relationships**:
      - **User**: Many-to-One (A job post is created by a single user)
      - **Jobrequests**: One-to-Many (A job post can have multiple job requests)


```python
class Jobpost(db.Model):
    __tablename__ = "jobposts"  # Table name

    # Table columns
    availability = db.Column(db.String, nullable=False)
    job_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_type = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False)
    job_location = db.Column(db.String, nullable=False)

    # Foreign key to the 'users' table
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='jobposts')
    jobrequests = db.relationship('Jobrequest', back_populates="jobpost", cascade="all, delete-orphan")

```


3. **Jobrequest**:
   - **Relationships**:
      - **User**: Many-to-One (A job request is made by a single user)
      - **Jobpost**: Many-to-One (A job request is for a single job post)
      - **Review**: One-to-Many (A job request can have multiple reviews)

```python
# Jobrequest model representing the 'jobrequests' table
class Jobrequest(db.Model):
    __tablename__ = "jobrequests"  # Table name

    # Table columns
    request_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    job_time = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    # Foreign keys
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("jobposts.job_id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="jobrequests")
    jobpost = db.relationship("Jobpost", back_populates="jobrequests")
    reviews = db.relationship('Review', back_populates='jobrequest', cascade="all, delete-orphan")
```

4. **Review**:
   - **Relationships**:
      - **User**: Many-to-One (A review is written by a single user)
      - **Jobrequest**: Many-to-One (A review is for a single job request)
```python
# Review model representing the 'reviews' table
class Review(db.Model):
    __tablename__ = "reviews"  # Define the table name

    # Table columns
    review_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)

    # Foreign keys
    user_name = db.Column(db.String, db.ForeignKey("users.user_name"), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('jobrequests.request_id'), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="reviews")
    jobrequest = db.relationship("Jobrequest", back_populates="reviews")
```
#### Examples of Routes to Access Data Using the relationships from the model

1. **Get all Job Posts**

```python
# /jobposts - GET - Fetch all job posts
@jobposts_bp.route("/", methods=["GET"])
def get_all_jobposts():
    stmt = db.select(Jobpost).order_by(Jobpost.date.desc())  # Select all job posts ordered by date
    jobposts = db.session.scalars(stmt)  # Execute the query
    return jobposts_schema.dump(jobposts)  # Return serialized job posts
```

2. **Create a Job Request**

```python
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
        return {"error": f"Job Post with ID {job_id} not found"}, 404
```

### R8: API Endpoints


### API Endpoints Overview

This API provides comprehensive endpoints to manage users, job posts, job requests, and reviews. Each endpoint is designed to facilitate easy interaction with the database, ensuring efficient and secure handling of all job-related data. The key functionalities of each endpoint include creating, reading, updating, and deleting records. Additionally, some errors are handled globally to ensure consistent and user-friendly error reporting throughout the API.


#### User Endpoints

##### BluePrint: auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

1. **Register User**
   - **HTTP Verb**: POST
   - **Path**: /auth/register
   - **Body**: 
     ```json
     {
       "user_name": "sally123",
       "name": "Sally James",
       "email": "sally@example.com",
       "password": "password123",
       "location": "Sydney"
     }
     ```
   - **Response**:
     - **Success (201 Created)**:
       ```json
       {
         "user_name": "sally123",
         "name": "Sally James",
         "email": "sally@example.com",
         "location": "Sydney",
         "is_admin": false
       }
       ```
     - **Failure (400 Bad Request)**:
       ```json
       {
         "error": "Email address is already in use."
       }
       ```

2. **Login User**
   - **HTTP Verb**: POST
   - **Path**: /auth/login
   - **Body**: 
     ```json
     {
       "user_name": "sally123",
       "password": "password123"
     }
     ```
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "email": "sally@example.com",
         "is_admin": false,
         "token": "jwt_token"
       }
       ```
     - **Failure (400 Bad Request)**:
       ```json
       {
         "error": "Invalid email or password"
       }
       ```

3. **Delete User**
   - **HTTP Verb**: DELETE
   - **Path**: /auth/users/{user_name}
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "message": "User 'peter456' deleted successfully"
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "message": "User 'peter456' not found"
       }
       ```

4. **Update User**
   - **HTTP Verb**: PUT, PATCH
   - **Path**: /auth/users/{user_name}
   - **Body**: 
     ```json
     {
       "name": "Peter Parker",
       "email": "peter_new@example.com",
       "password": "newpassword123",
       "location": "Melbourne"
     }
     ```
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "user_name": "peter456",
         "name": "Peter Parker",
         "email": "peter_new@example.com",
         "location": "Melbourne",
         "is_admin": false
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "User not found"
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "You are not authorised to edit this user. Only the owner can edit their information."
       }
       ```


#### Jobpost Endpoints

##### BluePrint: jobposts_bp = Blueprint("jobposts", __name__, url_prefix="/jobposts")

1. **Create Jobpost**
   - **HTTP Verb**: POST
   - **Path**: /jobposts
   - **Body**: 
     ```json
     {
       "availability": "Full-time",
       "job_type": "Software Developer",
       "description": "Develop and maintain web applications.",
       "job_location": "Brisbane"
     }
     ```
   - **Response**:
     - **Success (201 Created)**:
       ```json
       {
         "job_id": 1,
         "availability": "Full-time",
         "job_type": "Software Developer",
         "description": "Develop and maintain web applications.",
         "date": "2023-10-01",
         "job_location": "Brisbane",
         "user_name": "sally123"
       }
       ```
     - **Failure (400 Bad Request)**:
       ```json
       {
         "error": "Invalid input data"
       }
       ```

2. **Get All Jobposts**
   - **HTTP Verb**: GET
   - **Path**: /jobposts
   - **Response**:
     - **Success (200 OK)**:
       ```json
       [
         {
           "job_id": 1,
           "availability": "Full-time",
           "job_type": "Software Developer",
           "description": "Develop and maintain web applications.",
           "date": "2023-10-01",
           "job_location": "Brisbane",
           "user_name": "sally123"
         },
         {
           "job_id": 2,
           "availability": "Part-time",
           "job_type": "Graphic Designer",
           "description": "Create visual concepts.",
           "date": "2023-10-02",
           "job_location": "Sydney",
           "user_name": "peter456"
         }
       ]
       ```
     - **Failure (500 Internal Server Error)**:
       ```json
       {
         "error": "Internal server error"
       }
       ```

3. **Get Jobpost by ID**
   - **HTTP Verb**: GET
   - **Path**: /jobposts/{job_id}
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "job_id": 1,
         "availability": "Full-time",
         "job_type": "Software Developer",
         "description": "Develop and maintain web applications.",
         "date": "2023-10-01",
         "job_location": "Brisbane",
         "user_name": "sally123"
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Job post with ID 1 not found."
       }
       ```

4. **Update Jobpost**
   - **HTTP Verb**: PUT, PATCH
   - **Path**: /jobposts/{job_id}
   - **Body**: 
     ```json
     {
       "availability": "Part-time",
       "job_type": "Software Developer",
       "description": "Develop and maintain mobile applications.",
       "job_location": "Perth"
     }
     ```
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "job_id": 1,
         "availability": "Part-time",
         "job_type": "Software Developer",
         "description": "Develop and maintain mobile applications.",
         "date": "2023-10-01",
         "job_location": "Perth",
         "user_name": "sally123"
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "You are not authorized to edit this job post. Only the owner can edit posts."
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Job post with ID 1 not found."
       }
       ```

5. **Delete Jobpost**
   - **HTTP Verb**: DELETE
   - **Path**: /jobposts/{job_id}
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "message": "Job post with ID 1 deleted successfully"
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "message": "Job post with ID 1 not found"
       }
       ```


#### Jobrequest Endpoints

##### BluePrint: jobrequests_bp = Blueprint("jobrequests", __name__, url_prefix="/<int:job_id>/jobrequests")

1. **Create Jobrequest**
   - **HTTP Verb**: POST
   - **Path**: /jobposts/{job_id}/jobrequests
   - **Body**: 
     ```json
     {
       "job_time": "Morning",
       "description": "Fix the plumbing",
       "title": "Plumbing Job",
       "completed": false
     }
     ```
   - **Response**:
     - **Success (201 Created)**:
       ```json
       {
         "request_id": 1,
         "job_time": "Morning",
         "description": "Fix the plumbing",
         "title": "Plumbing Job",
         "completed": false,
         "date": "2023-10-01",
         "user_name": "sally123",
         "job_id": 1
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Job Post with ID 1 not found"
       }
       ```

2. **Delete Jobrequest**
   - **HTTP Verb**: DELETE
   - **Path**: /jobposts/{job_id}/jobrequests/{request_id}
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "message": "Job Request with ID 1 has been withdrawn"
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Job Request with ID 1 does not exist"
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "Cannot delete a job request that has been completed."
       }
       ```

3. **Update Jobrequest**
   - **HTTP Verb**: PUT, PATCH
   - **Path**: /jobposts/{job_id}/jobrequests/{request_id}
   - **Body**: 
     ```json
     {
       "job_time": "Afternoon",
       "description": "Fix the plumbing and the sink",
       "title": "Plumbing and Sink Job",
       "completed": true
     }
     ```
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "request_id": 1,
         "job_time": "Afternoon",
         "description": "Fix the plumbing and the sink",
         "title": "Plumbing and Sink Job",
         "completed": true,
         "date": "2023-10-05",
         "user_name": "sally123",
         "job_id": 1
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "You are not authorised to edit this job request. Only the owner can edit it."
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "Cannot update a job request that has been completed."
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Job Request with ID 1 not found."
       }
       ```

#### Review Endpoints

##### BluePrint: review_bp = Blueprint("reviews", __name__, url_prefix="/jobrequests/<int:request_id>/reviews")

1. **Create Review**
   - **HTTP Verb**: POST
   - **Path**: /jobrequests/{request_id}/reviews
   - **Body**: 
     ```json
     {
       "title": "Great Job",
       "rating": 5,
       "description": "The job was completed excellently."
     }
     ```
   - **Response**:
     - **Success (201 Created)**:
       ```json
       {
         "review_id": 1,
         "date": "2023-10-01",
         "title": "Great Job",
         "rating": 5,
         "description": "The job was completed excellently.",
         "request_id": 1,
         "user_name": "sally123"
       }
       ```
     - **Failure (400 Bad Request)**:
       ```json
       {
         "error": "Rating is required."
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "Cannot create a review if the job has not been completed."
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Job request with ID 1 does not exist."
       }
       ```

2. **Edit Review**
   - **HTTP Verb**: PUT, PATCH
   - **Path**: /jobrequests/{request_id}/reviews/{review_id}
   - **Body**: 
     ```json
     {
       "title": "Updated Review",
       "rating": 4,
       "description": "The job was good, but there were some delays."
     }
     ```
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "review_id": 1,
         "date": "2023-10-01",
         "title": "Updated Review",
         "rating": 4,
         "description": "The job was good, but there were some delays.",
         "request_id": 1,
         "user_name": "sally123"
       }
       ```
     - **Failure (403 Forbidden)**:
       ```json
       {
         "error": "You are not authorised to edit this review. Only the owner can edit it."
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Review with ID 1 does not exist."
       }
       ```

3. **Delete Review**
   - **HTTP Verb**: DELETE
   - **Path**: /jobrequests/{request_id}/reviews/{review_id}
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "message": "Review with ID 1 has been deleted successfully."
       }
       ```
     - **Failure (404 Not Found)**:
       ```json
       {
         "error": "Review with ID 1 does not exist or you are not authorized to delete it. Only admins can delete reviews."
       }
       ```

# Bibliography

1. Airtasker. (2023, December 13). *Airtasker Year in Review 2023 - Airtasker Blog*. Airtasker Blog. [https://www.airtasker.com/blog/year-in-review-2023/?form=MG0AV3](https://www.airtasker.com/blog/year-in-review-2023/?form=MG0AV3)
2. Consumer Sentinel Network Data Book 2020. (2021, February 2). *Federal Trade Commission*. [https://www.ftc.gov/reports/consumer-sentinel-network-data-book-2020?form=MG0AV3](https://www.ftc.gov/reports/consumer-sentinel-network-data-book-2020?form=MG0AV3)
3. contributors, M. C. and. (n.d.). *Basic Syntax | Markdown Guide*. Www.markdownguide.org. [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/)
4. *Flowchart Maker & Online Diagram Software*. (n.d.). App.diagrams.net. [https://draw.io/](https://draw.io/)
5. *Freelance Forward Economics Report | Upwork*. (2020). Upwork.com. [https://www.upwork.com/press/releases/freelance-forward-economics-report?form=MG0AV3](https://www.upwork.com/press/releases/freelance-forward-economics-report?form=MG0AV3)
6. *How it works*. (n.d.). Airtasker. [https://www.airtasker.com/au/how-it-works/](https://www.airtasker.com/au/how-it-works/)
7. *Introduction to Markdown*. (2024). Write the Docs. [https://www.writethedocs.org/guide/writing/markdown/](https://www.writethedocs.org/guide/writing/markdown/)
8. Melanie. (2023, November 27). *SQLAlchemy: What is it? What’s it for?* Data Science Courses | DataScientest. [https://datascientest.com/en/sqlalchemy-what-is-it-whats-it-for](https://datascientest.com/en/sqlalchemy-what-is-it-whats-it-for)
9. Microsoft. (2024, June 6). *Database normalization description*. Learn.microsoft.com. [https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description](https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)
10. *SQLAlchemy Documentation — SQLAlchemy 2.0 Documentation*. (n.d.). Docs.sqlalchemy.org. [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)
11. *Trello*. (2023). Trello. Trello. [https://trello.com/](https://trello.com/)