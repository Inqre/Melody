from flask import render_template, Blueprint, request
from db import db
import uuid
from id3reader import Reader

upload = Blueprint("upload", __name__, template_folder="templates")

@upload.route("/upload/")
def _upload():
    if request.method == "POST":
        song = request.files['song']
        name = song.filename
        if not name.endswith(".mp3"):
            return "Only MP3 files are supported."
        name = uuid.uuid4().hex+".mp3"
        with open("static/songs/"+name, 'wb') as file:
            file.write(file)
        obj = Reader("static/songs/"+name)
        title = obj.getValue("title")
        artist = obj.getValue("performer")
        year = obj.getValue("year")
        url = "/static/songs/"+name
        db.insert("songs", {"name":name, "title":title, "artist":artist, "year":year, "url":url})
    return render_template("upload.html")
