from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.models import db, migrate
from app.routes import api

#load_dotenv()

app = Flask(__name__)

api = Api(app)


# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db.init_app(app)
# migrate.init_app(app, db)
# api.init_app(app,
#              version=VERSION, title='Аниматика',
#              description='Anime base')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:slimdingo85@mysql:3306/flask' #'mysql+pymysql://{}:{}@{}/{}'.format(
#     os.getenv('DB_USER', 'flask'),
#     os.getenv('DB_PASSWORD', ''),
#     os.getenv('DB_HOST', 'mysql'),
#     os.getenv('DB_NAME', 'flask')
#)
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()


from app import app, db
from app.models import User, Anime


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Anime': Anime}


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
