# Photo Album

This basic application displays photo IDs and titles for an album. Photos are available at https://jsonplaceholder.typicode.com/photos. The format https://jsonplaceholder.typicode.com/photos?albumId=3 is used to select a specific album number and associated photos.

## Prerequisites

```
IntelliJ IDEA with Python Plugin (or PyCharm)
Postman
```

## Installing

- Clone the repository at "https://github.com/djdavis1420/photo_album.git".
- In your terminal/shell, navigate to the project's root directory.
- Activate a virtual environment (ie, "source ./venv/Scripts/activate") .
    - pip install -Ur src_reqs.txt
    - pip install -Ur test_reqs.txt
- Pytest, Mock, and Flask will be installed in the virtual environment.

## Running the Console Application
 - To view basic photo output in the console, right-click on photo_album/src/console_app.py and select "Run 'console_app'"
 - You will be prompted to type the number of an album between 1 and 100 (inclusive) into the console.
 - Upon pressing ENTER, you will see the details for the relevant photos in the console in the format provided by the instructions for the exercise. The output format begins with a line indicating the album, followed by fifty lines representing one photo id and photo title.

## Running the Web Application
 - To launch the web app, right-click on photo_album/src/web_app.py and select "Run 'web_app'".
 - Take note of the URL that is printed in the IntelliJ IDEA (or PyCharm) console. By default, this should be http://127.0.0.1:5000/.
 - In Postman, send a GET request with a body (raw) of '{"album_id": 3}' to "http://127.0.0.1:5000/photo_album/display_album".
 - The response body in Postman will provide the data for each photo in the requested album in JSON format.
 - Simultaneously, details for the requested album will be printed to the console in IntelliJ IDEA (or PyCharm) in the format required by the exercise.

## Error Handling
 - "Album Number is Invalid" if the album number is not an integer.
 - "Album Number Does Not Exist" if the album number is not between 1-100 (inclusive).

## Built With

- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - Integrated Development Environment
- [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework for Python
- [mock](https://docs.python.org/dev/library/unittest.mock.html) - Testing Library for Python
- [Flask](http://flask.pocoo.org/) - API Framework for Python

## Exercise Details

Create a console application that displays photo ids and titles in an album. The photos are available in this online web service (https://jsonplaceholder.typicode.com/photos).

Hint: Photos are filtered with a query string. This will return photos within albumId=3
(https://jsonplaceholder.typicode.com/photos?albumId=3)

- You can use any language
- Any open source libraries
- Unit tests are encouraged
- Post your solution on any of the free code repositories and send us a link:
    - https://github.com/
    - https://gitlab.com
    - https://bitbucket.org/

Provide a README that contains instructions on how to build and run your application
Spend as much (or little) time as you'd like on this. Feel free to use any resources available.

Example:

- photo-album 2
    - [53] soluta et harum aliquid officiis ab omnis consequatur
    - [54] ut ex quibusdam dolore mollitia
- photo-album 3
    - [101] incidunt alias vel enim
    - [102] eaque iste corporis tempora vero distinctio consequuntur nisi nesciunt