from flask import Flask, render_template
from flask import Blueprint
from flask_login import current_user
from repositories import get_frontend_data

views = simple_page = Blueprint('views', __name__)


@views.route('/', methods=["GET"])
@views.route('/find-job', methods=["GET"])
@views.route('/favorites', methods=["GET"])
@views.route('/settings', methods=["GET"])
@views.route('/positions', methods=["GET"])
@views.route('/positions/<id>', methods=["GET"])
@views.route('/requests', methods=["GET"])
@views.route('/edit-profile', methods=["GET"])
@views.route('/create', methods=["GET"])
@views.route('/candidates', methods=["GET"])
@views.route('/candidates/<id>', methods=["GET"])
def index(id=None):
    data = None
    if current_user.is_authenticated:
        data = get_frontend_data()
    return render_template("index.html", data=data)
