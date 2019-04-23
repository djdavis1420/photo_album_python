from urllib.request import urlopen


def test_check_external_service_status():
    path = 'https://jsonplaceholder.typicode.com/photos'
    response = urlopen(path, timeout=3)
    assert response.code == 200
