from io import StringIO

import pytest
from mock import patch

from src.services.photos import *


@patch('src.services.photos.urlopen')
def test_get_photos_by_album__should_serialize_response_data(mock_urlopen):
    album_id = 3
    mock_urlopen.return_value = StringIO('{"test_key": "test_value"}')
    actual = get_photos_by_album(album_id)
    assert actual == {"test_key": "test_value"}


def test_print_photos__should_raise_type_error():
    album_id = 'a'
    with pytest.raises(TypeError):
        print_photos(album_id)


def test_print_photos__should_raise_index_error():
    album_id = 155
    with pytest.raises(IndexError):
        print_photos(album_id)


def test_print_photos__should_return_and_print_in_console_details_for_album_2():
    album_id = 2
    actual = print_photos(album_id)
    assert actual[53] == 'soluta et harum aliquid officiis ab omnis consequatur'


def test_print_photos__should_return_and_print_in_console_details_for_album_3():
    album_id = 3
    actual = print_photos(album_id)
    assert actual[101] == 'incidunt alias vel enim'
