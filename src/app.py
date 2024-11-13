from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from controller.youtuber import Youtuber
import os
from ffmpy import FFmpeg
from controller.rekordboxer import RekordBoxer

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
load_dotenv()

youtuber = Youtuber()
rekordboxer = RekordBoxer()

@app.route('/search', methods=['POST'])
@cross_origin()
def search_song():
    # Get the search query from the JSON body of the POST request
    data = request.get_json()

    # Retrieve the 'query' from the JSON data, defaulting to empty string if not provided
    query = data.get('query', '')

    videos = youtuber.search(query)
    return jsonify(videos)

@app.route('/download', methods=['POST'])
@cross_origin()
def download_song():
    data = request.get_json()
    url = data.get('url', '')
    playlist = data.get('playlist', '')
    name = youtuber._download_mp3(url)
    response = rekordboxer.add_song(name, playlist)
    return jsonify(response)

@app.route('/playlists', methods=['GET'])
@cross_origin()
def get_playlists():
    return jsonify(rekordboxer.get_playlists())

@app.route('/autocomplete', methods=['POST'])
@cross_origin()
def autocomplete():
    data = request.get_json()
    query = data.get('query', '')
    suggestions = youtuber.autocomplete(query)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
