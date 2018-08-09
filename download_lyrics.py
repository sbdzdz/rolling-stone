import configparser
import lyricsgenius as genius

config = configparser.ConfigParser()
config.read('config.ini')
token = config['GENIUS']['ACCESS_TOKEN']

api = genius.Genius(token)
artist = api.search_artist('Bob Dylan', max_songs=10)
for song in artist.songs:
    print(song.title, song.year)
