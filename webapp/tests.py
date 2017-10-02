import unittest
import hashlib
from app import app, db
from app.models import User, News

def get_hashed_password(user_password):
    salt = "cefalologin"
    salted_password = user_password + salt
    hashed_value = hashlib.md5(salted_password.encode())
    return hashed_value.hexdigest()

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.tester = app.test_client(self)
        self.email_address = "test@example.com"
        self.password = "pass"
        self.full_name = "Test User"

    def tearDown(self):
        self.delete_user()
        with app.app_context():
            db.session.remove()

    def create_user(self):
        existing_user = User.query.filter_by(email_address=self.email_address).first()
        if existing_user == None:
            new_user = User(
                email_address=self.email_address,
                password=get_hashed_password(self.password),
                full_name=self.full_name)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        return existing_user

    def delete_user(self):
        existing_user = User.query.filter_by(email_address=self.email_address).first()
        if existing_user != None:
            db.session.delete(existing_user)
            db.session.commit()

    def recreate_user(self):
        existing_user = User.query.filter_by(email_address=self.email_address).first()
        if existing_user != None:
            self.delete_user()
        return self.create_user()

    def test_index_without_login(self):
        error_message = "test_index_without_login is failed."
        expected_response = b'Sign in to start your session'
        response = self.tester.get('/',
                               follow_redirects=True)
        self.assertEqual(response.status, '200 OK')
        self.assertIn(expected_response,response.data,error_message)

    def test_signup_with_valid_user(self):
        error_message = "test_signup_with_valid_user is failed."
        expected_response = b'Dashboard'
        response = self.tester.post('/signup',
                                    data=dict(
                                        email_address=self.email_address,
                                        password=self.password,
                                        full_name=self.full_name
                                    ),
                                    follow_redirects=True)
        self.assertEqual(response.status, '200 OK')
        self.assertIn(expected_response, response.data, error_message)

    def test_login_with_valid_user(self):
        error_message = 'test_login_with_valid_user is failed.'
        expected_response = b'Dashboard'
        user = self.recreate_user()
        response = self.tester.post('/login',
                                    data=dict(
                                        email_address=self.email_address,
                                        password=self.password
                                    ),
                                    follow_redirects=True)
        self.assertEqual(response.status, '200 OK')
        self.assertIn(expected_response, response.data, error_message)

    def test_login_with_invalid_user(self):
        error_message = "test_login_with_invalid_user is failed."
        expected_response = b'Sign in to start your session'
        response = self.tester.post('/login',
                                    data=dict(
                                        email_address=self.email_address,
                                        password=''),
                                    follow_redirects=True)
        self.assertEqual(response.status, '200 OK', "Error in response status")
        self.assertIn(expected_response, response.data, error_message)

    def test_show_news_without_login(self):
        response = self.tester.post('/news/12321312/html',
                                    follow_redirects=True)
        self.assertEqual(response.status, '405 METHOD NOT ALLOWED', "Error in response status")

    def test_logout_without_login(self):
        response = self.tester.post('/logout',
                                    follow_redirects=True)
        self.assertEqual(response.status, '405 METHOD NOT ALLOWED', "Error in response status")

if __name__ == '__main__':
    unittest.main()
