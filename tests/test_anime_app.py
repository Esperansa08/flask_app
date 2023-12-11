import unittest

import flask_unittest
import pytest

from app import app


@pytest.fixture
def client():
    # Set Flask application to test mode
    app.config["TESTING"] = True

    # Generate Flask test client
    with app.test_client() as client:
        yield client

    # Reset Flask application mode
    app.config["TESTING"] = False


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        with self.app as client:
            # Perform a POST request to the login endpoint with valid credentials
            response = client.get(
                "/login", data=dict(username="test", password="testpassword")
            )
            self.assertEqual(
                response.status_code, 200
            )  # expect a redirect response

    def test_register(self):
        with self.app as client:
            # Perform a POST request to the registration endpoint with valid form data

            response = client.post(
                "/register",
                data=dict(
                    username="newuser",
                    email="test@example.com",
                    password="newpassword",
                    password2="newpassword",
                ),
            )
            self.assertEqual(
                response.status_code, 302
            )  # expect a redirect response

            # Ensure account was successfully registered
            # You can check the database or perform a login request to verify the registration

    def test_home(self):
        with self.app as client:
            # Perform a GET request to the home endpoint without logging in
            response = client.get("/")
            self.assertEqual(
                response.status_code, 302
            )  # expect a redirect response
            response = client.get("/index")
            self.assertEqual(response.status_code, 302)
            # Log in the user
            response = client.post(
                "/login", data=dict(username="test", password="testpassword")
            )

            # Perform a GET request to the home endpoint after logging in
            response = client.get("/")
            self.assertEqual(
                response.status_code, 200
            )  # expect a successful response

    def test_anime_list(self):
        with self.app as client:
            # Perform a GET request to the profile endpoint without logging in
            response = client.get("/anime_list")
            self.assertEqual(
                response.status_code, 302
            )  # expect a redirect response

            # Log in the user
            response = client.post(
                "/login", data=dict(username="test", password="testpassword")
            )
            self.assertEqual(response.status_code, 302)
            # Perform a GET request to the profile endpoint after logging in
            response = client.get("/anime_list")
            self.assertEqual(
                response.status_code, 200
            )  # expect a successful response


if __name__ == "__main__":
    unittest.main()
