from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_caching import Cache
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.models import db, migrate
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields

# load_dotenv()
from flask_swagger_ui import get_swaggerui_blueprint

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields
from flask import Flask, abort, request, make_response, jsonify
from pprint import pprint
import json


# class DemoParameter(Schema):
#     gist_id = fields.Int()


# class AnimeSchema(Schema):
#     title = fields.Str()
#     description = fields.Str()

# spec = APISpec(
#     title="Anime API",
#     version="1.0.0",
#     openapi_version="3.0.2",
#     info=dict(
#         description="Anime API",
#         version="1.0.0-oas3",
#         contact=dict(
#             email="admin@donofden.com"
#             ),
#         license=dict(
#             name="Apache 2.0",
#             url='http://www.apache.org/licenses/LICENSE-2.0.html'
#             )
#         ),
#     # servers=[
#     #     dict(
#     #         description="Test server",
#     #         url="https://resources.donofden.com"
#     #         )
#     #     ],
#     tags=[
#         dict(
#             name="Anime",
#             description="Endpoints related to Anime"
#             )
#         ],
#     plugins=[FlaskPlugin(), MarshmallowPlugin()],
# )

# spec.components.schema("Anime", schema=AnimeSchema)


app = Flask(__name__)
cache = Cache(app)
api = Api(app)

# @app.route("/add_anime", methods=["POST"])
# def my_route():
#     """Gist detail view.
#     ---
#     get:
#       responses:
#         200:
#           description: Endpoints related to Demo
#           content:
#             application/json:
#               schema: AnimeSchema
#     """
#     # (...)
#     return jsonify('foo')


# # Since path inspects the view and its route,
# # we need to be in a Flask request context
# with app.test_request_context():
#     spec.path(view=my_route)
# # We're good to go! Save this to a file for now.
# with open('swagger.json', 'w') as f:
#     json.dump(spec.to_dict(), f)

# pprint(spec.to_dict())
# print(spec.to_yaml())


# spec = APISpec(
#     title='Anime app',
#     version='1.0.1',
#     openapi_version='3.0.2',
#     plugins=[FlaskPlugin(), MarshmallowPlugin()])


# @app.route('/swagger.json')
# def create_swagger_spec():
#     return jsonify(spec.to_dict)


# class TodoResponseScema(Schema):
#     id = fields.Int()
#     title = fields.Int()
#     status = fields.Boolean()


# class ToDoListResponseScema(Schema):
#     todo_list = fields.List(fields.Nested(TodoResponseScema))


# @app.route('/todo')
# def todo():
#     """Get ist of Todo
#        __

#        get:
#            description: Get List of Todo
#            response:
#                 200:
#                     description: Return a Todo List
#                     content:
#                         application/json:
#                             schema: ToDoListResponseScema

#     """
#     dummy_data = {}

#     return ToDoListResponseScema().dump({'todo_list': dummy_data})


# with app.test_request_context():
#     spec.path(view=todo)


# SWAGGER_URL = '/api/docs'
# API_URL = '/api/swagger'
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={'app_name': "Мое API"})
# app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


cache.init_app(app, config={"CACHE_TYPE": "SimpleCache"})

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://flask:slimdingo85@mysql:3306/flask"  #'mysql+pymysql://{}:{}@{}/{}'.format(
#     os.getenv('DB_USER', 'flask'),
#     os.getenv('DB_PASSWORD', ''),
#     os.getenv('DB_HOST', 'mysql'),
#     os.getenv('DB_NAME', 'flask')
# )
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


from app import app, db, cache, spec
from app.models import User, Anime


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Anime": Anime}


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
