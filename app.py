# import Flask and SQLAlchemy
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os
import logging

# set up the application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Use sqlite for simplicity
# postgres://isommie:MOVsapXN8lztQGgV97N4DnfkT03YKzLF@dpg-cjvn8195mpss73937sv0-a.oregon-postgres.render.com/simple_flask_rest_api_db
db = SQLAlchemy(app)

# set up logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Person {self.name}>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

# or in the shell
# Create the Database Before running the application
# Open a Python shell with >> python3
# Import the database and models >> from app import db, Person
# Create the tables >> db.create_all()
# Exit the Python shell >> exit()


# the API Endpoints
@app.route('/', methods=['GET'])
def home():
    return """
    <h1>Welcome to my Flask API resource!</h1>
    <p>
        This is a place where you can interact with the domain request header.<br>
        Just add <strong>/api</strong> to your request and explore the possibilities.<br>
        Thank you for visiting and have a great time exploring!
    </p>
    """

@app.route('/api', methods=['POST'])
def create_person():
    app.logger.info('Processing default request')
    name = request.json['name']
    if not isinstance(name, str):
        return jsonify({'error': 'Invalid input: name must be a string'}), 400
    new_person = Person(name=name)
    db.session.add(new_person)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'A person with that name already exists'}), 400
    return jsonify({'message': f'Person {new_person.name} created!'}), 201

@app.route('/api/<id>', methods=['GET'])
def read_person(id):
    app.logger.info('Processing default request')
    person = Person.query.get(id)
    if person is None:
        return jsonify({'error': 'Person not found!'}), 404
    return jsonify({'id': person.id, 'name': person.name}), 200

@app.route('/api/<id>', methods=['PUT'])
def update_person(id):
    app.logger.info('Processing default request')
    name = request.json['name']
    if not isinstance(name, str):
        return jsonify({'error': 'Invalid input: name must be a string'}), 400
    person = Person.query.get(id)
    if person is None:
        return jsonify({'error': 'Person not found!'}), 404
    person.name = name
    db.session.commit()
    return jsonify({'message': f'Person updated to {person.name}!'}), 200

@app.route('/api/<id>', methods=['DELETE'])
def delete_person(id):
    app.logger.info('Processing default request')
    person = Person.query.get(id)
    if person is None:
        return jsonify({'error': 'Person not found!'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': f'Person {person.name} deleted!'}), 200

@app.route('/api', methods=['GET'])
def get_all_persons():
    app.logger.info('Processing default request')
    persons = Person.query.all()
    return jsonify({'persons': [{'id': person.id, 'name': person.name} for person in persons]}), 200

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error
    app.logger.error(str(e))

    # Return a JSON response with the error message and status code
    return jsonify({'error': 'An unexpected error occurred'}), 500


# Running the Application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


# if __name__ == '__main__':
#     app.run(debug=True)