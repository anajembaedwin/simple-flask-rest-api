# API Documentation

This document provides information on the endpoints available in the Flask API.

## Standard Request and Response Formats

All requests should be made with the `Content-Type` header set to `application/json`. All responses will also be in JSON format.

## Endpoints

### POST /api

Creates a new person.

**Request format:**

```json
{
    "name": "string"
}
```

**Response format:**

```
{
    "message": "string"
}
```

### GET /api/<id>

Fetches details of a person.

**Response format:**

```
{
    "id": integer,
    "name": "string"
}
```

### PUT /api/<id>

Updates details of a person.

**Request format:**

```
{
    "name": "string"
}
```

**Response format:**

```
{
    "message": "string"
}
```

### DELETE /api/<id>

Deletes a person.

**Response format:**

```
{
    "message": "string"
}
```

### GET /api

Fetches all persons.

**Response format:**

```
{
    "persons": [
        {
            "id": integer,
            "name": "string"
        },
        ...
    ]
}
```

# Sample Usage
Here’s an example of how to use the API with curl:

## Create a new person

```
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe"}' http://localhost:5000/api
```

## Get a person's details

```
curl http://localhost:5000/api/1
```

## Update a person's details

```
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Jane Doe"}' http://localhost:5000/api/1
```

## Delete a person

```
curl -X DELETE http://localhost:5000/api/1
```

## Get all persons

```
curl http://localhost:5000/api
```

The standard formats for requests and responses for each endpoint of the Flask API, using different base URLs for local, Gunicorn, and live server environments:

1. **Create a Person**
    - Local: `POST http://localhost:5000/api`
    - Gunicorn: `POST http://127.0.0.1:8000/api/`
    - Live Server: `POST https://simple-flask-rest-api-y6zs.onrender.com/api`
    - Request Body: `{"name": "<name of the person>"}`
    - Response: `{"message": "Person <name of the person> created!"}` with HTTP status code 201

2. **Read a Person**
    - Local: `GET http://localhost:5000/api/<id>`
    - Gunicorn: `GET http://127.0.0.1:8000/api/<id>`
    - Live Server: `GET https://simple-flask-rest-api-y6zs.onrender.com/api/<id>`
    - Response: `{"id": <id of the person>, "name": "<name of the person>"}` with HTTP status code 200

3. **Update a Person**
    - Local: `PUT http://localhost:5000/api/<id>`
    - Gunicorn: `PUT http://127.0.0.1:8000/api/<id>`
    - Live Server: `PUT https://simple-flask-rest-api-y6zs.onrender.com/api/<id>`
    - Request Body: `{"name": "<new name of the person>"}`
    - Response: `{"message": "Person updated to <new name of the person>!"}` with HTTP status code 200

4. **Delete a Person**
    - Local: `DELETE http://localhost:5000/api/<id>`
    - Gunicorn: `DELETE http://127.0.0.1:8000/api/<id>`
    - Live Server: `DELETE https://simple-flask-rest-api-y6zs.onrender.com/api/<id>`
    - Response: `{"message": "Person <name of the person> deleted!"}` with HTTP status code 200

5. **Get All Persons**
    - Local: `GET http://localhost:5000/api`
    - Gunicorn: `GET http://127.0.0.1:8000/api/`
    - Live Server: `GET https://simple-flask-rest-api-y6zs.onrender.com/api`
    - Response: `{"persons": [{"id": <id of the person>, "name": "<name of the person>"}, ...]}` with HTTP status code 200

Please replace `<id>` with the actual ID of the person and `<name of the person>` with the actual name of the person. If there's an error, you'll get a response like `{"error": "<error message>"}` with an appropriate HTTP status code.


# Limitations and Assumptions
- The API does not support authentication or authorization. It’s assumed that it’s used in a trusted environment.
- The API does not support pagination. It’s assumed that the number of persons will be small enough to handle in a single request.
- The API does not validate the length of the name field. It’s assumed that names will be of reasonable length.


# Setup and Deployment Instructions

### Install the required Python packages with pip:

```
pip install flask flask_sqlalchemy
```

### Run the application:

```
python app.py
```

The application will be available at http://localhost:5000.

### Sample Deployment

To deploy the application on a server like Render, you would need to:

- Push your code to a Git repository: Render supports deployments from GitHub, GitLab, and Bitbucket.

- Create a new Web Service on Render: Go to the Render dashboard, click on “New”, and select “Web Service”.

- Connect your repository: Select your repository and branch.

- Configure the Web Service: Choose a name for your service and select the environment (Python). You also need to specify the build command (pip install -r requirements.txt if you have a requirements.txt file) and the start command (python app.py).

- Deploy: Click on “Create Web Service”. Render will fetch your code, install the dependencies, and start your application.

Please replace `"John Doe"`, `"Jane Doe"`, and `1` with actual names and ids you want to use for testing. Also, replace `localhost` and `5000` with your actual host and port if they are different.
