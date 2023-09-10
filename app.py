# import Flask and SQLAlchemy
from flask import Flask, request
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