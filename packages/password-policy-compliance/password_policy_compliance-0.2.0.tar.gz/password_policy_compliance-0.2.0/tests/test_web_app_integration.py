import unittest
import json
from password_policy_compliance.examples.web_app_integration import app

class TestWebAppIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_valid(self):
        response = self.app.post('/register', 
                                 data=json.dumps({'username': 'alice', 'password': 'Str0ngP@ssw0rd!'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User registered successfully')

    def test_register_invalid(self):
        response = self.app.post('/register', 
                                 data=json.dumps({'username': 'bob', 'password': 'weak'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_login_success(self):
        self.app.post('/register', 
                      data=json.dumps({'username': 'charlie', 'password': 'Str0ngP@ssw0rd!'}),
                      content_type='application/json')
        response = self.app.post('/login', 
                                 data=json.dumps({'username': 'charlie', 'password': 'Str0ngP@ssw0rd!'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Login successful')

    def test_login_failure(self):
        response = self.app.post('/login', 
                                 data=json.dumps({'username': 'david', 'password': 'WrongPassword'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_password_strength(self):
        response = self.app.post('/password_strength', 
                                 data=json.dumps({'password': 'Str0ngP@ssw0rd!'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('strength_score', data)
        self.assertIn('feedback', data)
        self.assertIn('crack_times', data)

if __name__ == '__main__':
    unittest.main()
