from flask import render_template, Blueprint
from db import db

index = Blueprint("index", __name__, template_folder="templates")

@index.route("/")
def _index():
    pass
