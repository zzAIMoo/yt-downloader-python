from youtube_dl import YoutubeDL
import hashlib
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/url', methods=['GET'])

def url():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    result = hashlib.md5(str.encode(id)) #I md5 the name of the file to avoid collision in names
    digested = result.hexdigest()
    ytdl_opts = {
        'format':'bestaudio',
        'outtmpl':'songs/'+digested+'.mp3'
    }
    audio_downloader = YoutubeDL(ytdl_opts)
    try:
        audio_downloader.extract_info("https://www.youtube.com/watch?v="+id)
    except Exception:
        print("Couldn\'t download the audio")
    results = "/"+digested+".mp3"
    return jsonify(results)

app.run()

