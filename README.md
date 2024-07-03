This project demonstrates a CRUD (Create, Read, Update, Delete) application using FastAPI 

<h3>File Structure</h3>

CRUD_APP <br>
├── app/ <br>
│   ├── __init__.py<br>
│   ├── main.py<br>
│   ├── database.py<br>
│   ├── models.py<br>
│   ├── schemas.py<br>
│   └── crud.py<br>
├── requirements.txt<br>
└── .env<br>

<h2>Description</h2>
app/: This directory contains the main application code.

init.py: Initializes the app as a Python package.
main.py: Entry point of the FastAPI application where routes are defined.
database.py: Manages database connections and sessions.
models.py: Defines database models using SQLAlchemy.
schemas.py: Defines Pydantic models (schemas) for request and response validation.
crud.py: Contains CRUD (Create, Read, Update, Delete) operations logic.
requirements.txt: Lists Python dependencies required for the project.

.env: Configuration file containing environment variables, such as database connection strings.
