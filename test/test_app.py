from mock import patch
from src.app import *


def test_health__should_return_response_status_200():
    actual = health()
    assert actual.status_code == 200


@patch('src.app.print_photos')
@patch('src.app.request')
def test_display_photos_in_album__should_call_print_photos(mock_request, mock_photos):
    mock_request.data = '{"album_id": 3}'
    mock_photos.return_value = ['test_response']
    actual = display_photos_in_album()
    assert actual.status_code == 200
    assert actual.data == b'["test_response"]'
