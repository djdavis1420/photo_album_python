import json
from urllib.request import urlopen


def get_all_photos():
    path = 'https://jsonplaceholder.typicode.com/photos'
    list_of_photos = json.load(urlopen(path))
    return list_of_photos


def get_photos_by_album(album_id):
    query = '?albumId=' + str(album_id)
    path = 'https://jsonplaceholder.typicode.com/photos' + query
    list_of_photos = json.load(urlopen(path))
    return list_of_photos


def print_photos(album_id):
    photos = get_photos_by_album(album_id)
    print('\n\nphoto-album ' + str(album_id))
    for photo in photos:
        print('[' + str(photo['id']) + ']  ' + photo['title'])
    return photos
