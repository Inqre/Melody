from flask import render_template, Blueprint, request, redirect
from db import db
import uuid
from id3reader import Reader
import os

index = Blueprint("index", __name__, template_folder="templates")

@index.route("/", methods=['GET', 'POST'])
def _index():
    if not request.values.get("song"):
        return redirect("/?song=0")
    page = int(request.values.get("song"))
    if request.method == "POST":
        song = request.files.getlist('song[]')
        for song in song:
            name = song.filename
            if not name.endswith(".mp3"):
                return "Only MP3 files are supported."
            name = uuid.uuid4().hex+".mp3"
            with open("static/songs/"+name, 'wb') as file:
                file.write(song.read())
            obj = Reader("static/songs/"+name)
            title = obj.getValue("title")
            if not title:
                title = song.filename.split(".mp3")[0]
            artist = obj.getValue("performer")
            if not artist:
                artist = "Unknown"
            year = obj.getValue("year")
            url = "../static/songs/"+name
            if not db.find("songs", {"title":title}):            
                db.insert("songs", {"title":title, "artist":artist, "year":year, "url":url})
            else:
                os.remove("static/songs/"+name)

    songs = db.find("songs", "all")
    playlists = db.find("playlists", "all")
    if songs:
        try:
            first = songs[page]
        except IndexError:
            return redirect("/")
    else:
        first = []
    if not playlists:
        playlists = []
    if not songs:
        songs = []
    
    if page > 0:
        autoplay = {"autoplay":"autoplay", "play":"pause"}
    else:
        autoplay = {"autoplay":"", "play":"play"}
    return render_template("index.html", autoplay=autoplay, page=page, first=first, songs=songs, playlists=playlists)

