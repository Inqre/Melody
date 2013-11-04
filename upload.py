from flask import render_template, Blueprint, request
from db import db

upload = Blueprint("upload", __name__, template_folder="templates")

@upload.route("/")
def _upload():
    pass
