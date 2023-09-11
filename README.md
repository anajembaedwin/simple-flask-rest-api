# Simple Flask REST Api

A simple Flask REST API, built with Flask and SQLAlchemy, capable of CRUD operations on a "person" resource, interfacing with a database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- You need to have Python 3 and pip installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).
- The project was built using Windows Subsystem for Linux (WSL), Ubuntu, virtualenv, and Visual Studio Code with a remote connection, so most instructions are for a Linux environment but can also work on Windows.

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/anajembaedwin/simple-flask-rest-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd simple-flask-rest-api
   ```

3. Install the required packages:

   ```bash
   pip install flask flask_sqlalchemy
   ```

4. Run the application:

   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000` or a preconfigured port.

## API Endpoints

The API has the following endpoints:

- `POST /api`: Creates a new person.
- `GET /api/<id>`: Fetches details of a person.
- `PUT /api/<id>`: Updates details of a person.
- `DELETE /api/<id>`: Deletes a person.
- `GET /api`: Fetches all persons.

# Database Modelling Diagram

UML (Unified Modeling Language) diagram that represents the structure and relationships of the API classes and models.

# Components of the Project

## Person Class

This is the main class in the application. It has two attributes: `id` and `name`.

## Flask App

This is the main application object. It doesn’t have any attributes in the current design, but it has methods corresponding to each of the API endpoints: `create_person`, `read_person`, `update_person`, `delete_person`, and `get_all_persons`.

## Database (db)

This is the SQLAlchemy database instance. It doesn’t have any attributes or methods in the current design, but it’s used to interact with the Person class.

# Text Representation of UML Diagram

## Person

- `id`: Integer
- `name`: String

## Flask App

- `create_person()`: POST /api
- `read_person(id)`: GET /api/<id>
- `update_person(id)`: PUT /api/<id>
- `delete_person(id)`: DELETE /api/<id>
- `get_all_persons()`: GET /api

## Database (db)

## E-R diagram Sketch

```
      +---------------+            +---------------+
      |   Flask App   |<>--------->|    Person     |
      +---------------+            +---------------+
                                    | - id: Integer |
                                    | - name: String|
                                    +---------------+
                                                |
                                                |
                                                |
                                    +---------------+
                                    |  Database (db)|
                                    +---------------+
```

## UML diagram

![UML Diagram](flask-api-uml-diagramm.drawio.png)


