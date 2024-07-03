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
<b>init.py:</b> Initializes the app as a Python package.<br>
<b>main.py:</b> Entry point of the FastAPI application where routes are defined.<br>
<b>database.py:</b> Manages database connections and sessions.<br>
<b>models.py:</b> Defines database models using SQLAlchemy.<br>
<b>schemas.py:</b> Defines Pydantic models (schemas) for request and response validation.<br>
<b>crud.py:</b> Contains CRUD (Create, Read, Update, Delete) operations logic.<br>
<b>requirements.txt:</b> Lists Python dependencies required for the project.<br>
<b><br>
<b>.env:</b> Configuration file containing environment variables, such as database connection strings.<br>
