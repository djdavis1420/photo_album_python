from mock import patch

from src.web_app import *


def test_health__should_return_response_status_200():
    actual = health()
    assert actual.status_code == 200


@patch('src.web_app.print_photos')
@patch('src.web_app.request')
def test_display_photos_in_album__should_return_photos_in_requested_album(mock_request, mock_photos):
    mock_request.data = '{"album_id": "3"}'
    mock_photos.return_value = {101: 'incidunt alias vel enim'}
    actual = display_photos_in_album()
    assert actual.status_code == 200
    assert actual.data == b'{"101": "incidunt alias vel enim"}'


@patch('src.web_app.print_photos')
@patch('src.web_app.request')
def test_display_photos_in_album__should_return_album_number_is_invalid(mock_request, mock_photos):
    mock_request.data = '{"album_id": "a"}'
    mock_photos.side_effect = TypeError
    actual = display_photos_in_album()
    assert actual.status_code == 400
    assert actual.data == b'"Album Number is Invalid"'


@patch('src.web_app.print_photos')
@patch('src.web_app.request')
def test_display_photos_in_album__should_return_album_number_does_not_exist(mock_request, mock_photos):
    mock_request.data = '{"album_id": 155}'
    mock_photos.side_effect = IndexError
    actual = display_photos_in_album()
    assert actual.status_code == 404
    assert actual.data == b'"Album Number Does Not Exist"'
