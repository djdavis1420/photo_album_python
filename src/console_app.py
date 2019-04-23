from src.services.photos import print_photos

try:
    album_number = int(input("Type the number of the album (1-100 inclusive) for which you'd like details and press ENTER: "))
    print_photos(album_number)
except TypeError:
    print('Album Number is Invalid')
except ValueError:
    print('Album Number is Invalid')
except IndexError:
    print('Album Number Does Not Exist')
