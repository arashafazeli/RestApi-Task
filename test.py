import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import app, db, Beer
from os import environ

db = SQLAlchemy(app)
class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        environ["DB_URL"] = "sqlite:///:memory:"
        app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URL')
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
        self.app = app.test_client()
        db.create_all()

        # Insert dummy data for testing
        beer1 = Beer(id=1, beer_id='73513513', name='Stockholm Beer', price=12.95, alcohol_percentage=5)
        beer2 = Beer(id=2, beer_id='12345678', name='eriksberg', price=9.99, alcohol_percentage=4.5)
        db.session.add(beer1)
        db.session.add(beer2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_test_route(self):
        response = self.app.get('/test')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'test route')

    def test_get_beer(self):
        response = self.app.get('/beer/73513513')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['beer_id'], '73513513')
        self.assertEqual(data['name'], 'Stockholm Beer')

    def test_get_beer_not_found(self):
        response = self.app.get('/beer/99999999')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['error'], 'Beer not found')

    def test_search_beer(self):
        data = {
            'name': 'Beer',
            'priceFrom': 0,
            'priceTo': 10,
            'alcoholPercentageFrom': 0,
            'alcoholPercentageTo': 5
        }
        response = self.app.post('/beer', json=data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)  # Assuming two beers match the search criteria

    def test_check_health(self):
        response = self.app.get('/health')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'Database connection is healthy')

if __name__ == '__main__':
    unittest.main()
