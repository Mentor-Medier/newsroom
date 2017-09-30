import unittest

from app import app, db
from app.models import User, News
import urllib

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.baseURL = "http://localhost:5000"

    def tearDown(self):
        pass

    def test_index(self):
        response = urllib.request.urlopen(self.baseURL)
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
