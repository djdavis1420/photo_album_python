#!C/Users/djdav/Development/Python/photo_album/venv/Scripts/python

import json
from flask import Flask
from flask import Response
from flask import request

from src.services.photos import print_photos

app = Flask(__name__)


@app.route('/photo_album/health', methods=['GET'])
def health():
    return Response(status=200)


@app.route('/photo_album/display_album', methods=['GET'])
def display_photos_in_album():
    request_data = json.loads(request.data)
    album_id = request_data['album_id']
    result = print_photos(album_id)
    return Response(json.dumps(result), status=200)


if __name__ == '__main__':
    app.run(debug=True)
