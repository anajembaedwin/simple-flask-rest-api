import unittest
from app import app, db, Person

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        with app.app_context():
            self.db.create_all()

    def tearDown(self):
        with app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_create_person(self):
        with app.app_context():
            response = self.app.post('/api', json={'name': 'Test'})
            self.assertEqual(response.status_code, 201)
            person = Person.query.first()
            self.assertEqual(person.name, 'Test')

    def test_read_person(self):
        with app.app_context():
            # Create a test person
            self.app.post('/api', json={'name': 'Test'})
            person = Person.query.first()

            # Test the read_person route
            response = self.app.get(f'/api/{person.id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'id': person.id, 'name': 'Test'})

    def test_update_person(self):
        with app.app_context():
            # Create a test person
            self.app.post('/api', json={'name': 'Test'})
            person = Person.query.first()

            # Test the update_person route
            response = self.app.put(f'/api/{person.id}', json={'name': 'Updated'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(Person.query.get(person.id).name, 'Updated')

    def test_delete_person(self):
        with app.app_context():
            # Create a test person
            self.app.post('/api', json={'name': 'Test'})
            person = Person.query.first()

            # Test the delete_person route
            response = self.app.delete(f'/api/{person.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIsNone(Person.query.get(person.id))

    def test_get_all_persons(self):
        with app.app_context():
            # Create some test persons
            self.app.post('/api', json={'name': 'Test1'})
            self.app.post('/api', json={'name': 'Test2'})

            # Test the get_all_persons route
            response = self.app.get('/api')
            self.assertEqual(response.status_code, 200)
            persons = response.get_json()['persons']
            self.assertEqual(len(persons), 2)

if __name__ == '__main__':
    unittest.main()
