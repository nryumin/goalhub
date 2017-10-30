from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from repositories import UserRepository
app = Flask(__name__)

app.config['MONGO_HOST'] = 'database'
app.config['MONGO_DBNAME'] = 'pitchme'
app.config['MONGO_USERNAME'] = 'writer'
app.config['MONGO_PASSWORD'] = 'writer'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return UserRepository.get_by_id(user_id)

from api import api
from views import views

app.register_blueprint(api,url_prefix='/api')
app.register_blueprint(views)
