from flask import Flask, render_template
from flask import Blueprint
from flask_login import current_user
from repositories import get_frontend_data

views = simple_page = Blueprint('views', __name__)


@views.route('/', methods=["GET"])
def index(id=None):
    return render_template("index.html")
