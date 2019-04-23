import json
from urllib.request import urlopen


def get_photos_by_album(album_id):
    query = '?albumId=' + str(album_id)
    path = 'https://jsonplaceholder.typicode.com/photos' + query
    return json.load(urlopen(path))


def print_photos(album_id):
    if type(album_id) is str:
        raise TypeError
    if (album_id > 100) or (album_id <= 0):
        raise IndexError

    photos = get_photos_by_album(album_id)
    album = {}
    print('\n\nphoto-album ' + str(album_id))
    for photo in photos:
        photo_details = {photo['id']: photo['title']}
        album.update(photo_details)
        print('[' + str(photo['id']) + ']  ' + photo['title'])

    return album
