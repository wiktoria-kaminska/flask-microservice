import unittest
from api.app import create_app


class TestConfig():
    SERVER_NAME = 'localhost:5000'
    TESTING = True


class BaseTestCase(unittest.TestCase):
    config = TestConfig

    def setUp(self):
        '''Set up an instance of the app for testing'''
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()



    def tearDown(self):
        self.app_context.pop()
