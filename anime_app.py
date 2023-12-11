import os

from flask import Flask
from flask_caching import Cache
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.models import db

app = Flask(__name__)
cache = Cache(app)
api = Api(app)

cache.init_app(app, config={"CACHE_TYPE": "SimpleCache"})

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI"
)
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


from app import app, cache, db, spec
from app.models import Anime, User


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Anime": Anime}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
