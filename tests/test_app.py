#from .. import anime_app
from app.routes import internal_error
import unittest
import flask_unittest
import flask.globals


# class TestBase(flask_unittest.AppClientTestCase):
#     def create_app(self):
#         """Create and configure a new app instance for each test."""
#         # create a temporary file to isolate the database for each test
#         db_fd, db_path = tempfile.mkstemp()
#         # create the app with common test config
#         app = create_app({"TESTING": True, "DATABASE": db_path})

#         # create the database and load test data
#         with app.app_context():
#             init_db()
#             get_db().executescript(_data_sql)

#             # Yield the app
#             '''
#             This can be outside the `with` block too, but we need to
#             call `close_db` before exiting current context
#             Otherwise windows will have trouble removing the temp file
#             that doesn't happen on unices though, which is nice
#             '''
#             yield app

#             ## Close the db
#             close_db()

#         ## Cleanup temp file
#         os.close(db_fd)
#         os.remove(db_path)


# class MyTestCase(flask_unittest.AppClientTestCase):
#     # def setUp(self):
#     #     anime_app.app.testing = True
#     #     self.app = anime_app.app.test_client()

#     def test_home(self, client):
#         # result = self.app.get('/')
#         # Make your assertions
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)


# class TestAuth(TestBase):
#     def test_login(self, _, client):
#         # test that viewing the page renders without template errors
#         self.assertStatus(client.get("/auth/login"), 200)

#         # test that successful login redirects to the index page
#         auth = AuthActions(client)
#         response = auth.login()
#         self.assertLocationHeader(response, "http://localhost/")

#         # login request set the user_id in the session
#         # check that the user is loaded from the session
#         client.get("/")
#         self.assertEqual(session["user_id"], 1)
#         self.assertEqual(g.user["username"], "test")

class TestSum(unittest.TestCase):

    def test_intrnal(self):
        self.assertEqual(internal_error(500), 500, "Should be 500")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()