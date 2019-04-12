from src.services.photos import *


def test_get_all_photos__should_return_list_of_all_photos():
    actual = get_all_photos()
    assert actual is not None
    assert type(actual) == list
    assert type(actual[0]) == dict


def test_get_photos_by_album__should_return_list_of_photos_in_specific_album():
    album_id = 3
    actual = get_photos_by_album(album_id)
    assert actual is not None
    assert type(actual) == list
    assert type(actual[0]) == dict


def test_print_photos__should_print_details_for_fifty_photos_in_console():
    album_id = 3
    print_photos(album_id)
