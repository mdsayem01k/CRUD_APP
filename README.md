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



- **app/**: Contains the main application code.
  - **__init__.py**: Initializes the app as a Python package.
  - **main.py**: Entry point of the FastAPI application where routes are defined.
  - **database.py**: Manages database connections and sessions.
  - **models.py**: Defines database models using SQLAlchemy.
  - **schemas.py**: Defines Pydantic models (schemas) for request and response validation.
  - **crud.py**: Contains CRUD operations logic.

- **requirements.txt**: Lists Python dependencies required for the project.
- **.env**: Configuration file containing environment variables, such as database connection strings.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/YOUR-GITHUB-USERNAME/fastapi_crud.git
    cd fastapi_crud
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set up the environment variables in `.env`.
2. Start the FastAPI application:

    ```sh
    uvicorn app.main:app --reload
    ```

3. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

