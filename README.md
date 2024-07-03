# FastAPI CRUD Project

This project implements a CRUD (Create, Read, Update, Delete) application using FastAPI.

## API Documentation

### Retrieve all users

- **URL**: `/users/`
- **Method**: `GET`
- **Description**: Retrieves a list of all users.

### Create a new user

- **URL**: `/users/`
- **Method**: `POST`
- **Description**: Creates a new user.

### Retrieve a specific user

- **URL**: `/users/{user_id}`
- **Method**: `GET`
- **Description**: Retrieves details of a specific user identified by `user_id`.

### Update a user

- **URL**: `/users/{user_id}`
- **Method**: `PUT`
- **Description**: Updates information of a specific user identified by `user_id`.

### Delete a user

- **URL**: `/users/{user_id}`
- **Method**: `DELETE`
- **Description**: Deletes a specific user identified by `user_id`.

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
    git clone [https://github.com/YOUR-GITHUB-USERNAME/fastapi_crud.git](https://github.com/mdsayem01k/CRUD_APP.git)
    cd CRUD_APP
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

