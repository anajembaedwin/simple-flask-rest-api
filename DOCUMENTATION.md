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
