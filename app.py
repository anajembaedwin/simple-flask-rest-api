# import Flask and SQLAlchemy
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# set up the application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Use sqlite for simplicity
db = SQLAlchemy(app)

# define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Person {self.name}>'

# Create the Database Before running the application
# Open a Python shell with >> python3
# Import the database and models >> from app import db, Person
# Create the tables >> db.create_all()
# Exit the Python shell >> exit()


# the API Endpoints
@app.route('/api', methods=['POST'])
def create_person():
    name = request.json['name']
    if not isinstance(name, str):
        return jsonify({'error': 'Invalid input: name must be a string'}), 400
    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': f'Person {new_person.name} created!'}), 201

@app.route('/api/<id>', methods=['GET'])
def read_person(id):
    person = Person.query.get(id)
    if person is None:
        return jsonify({'error': 'Person not found!'}), 404
    return jsonify({'id': person.id, 'name': person.name}), 200

@app.route('/api/<id>', methods=['PUT'])
def update_person(id):
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
    person = Person.query.get(id)
    if person is None:
        return jsonify({'error': 'Person not found!'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': f'Person {person.name} deleted!'}), 200

@app.route('/api', methods=['GET'])
def get_all_persons():
    persons = Person.query.all()
    return jsonify({'persons': [{'id': person.id, 'name': person.name} for person in persons]}), 200


# Running the Application
if __name__ == '__main__':
    app.run(debug=True)
