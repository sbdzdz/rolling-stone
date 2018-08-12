import configparser
import lyricsgenius as genius

def get_name(writer):
    return writer[0]

def written_by(author, song):
    writers = [get_name(writer) for writer in song.writer_artists]
    return author in writers

config = configparser.ConfigParser()
config.read('config.ini')
token = config['GENIUS']['ACCESS_TOKEN']

api = genius.Genius(token)
artist = api.search_artist('Bob Dylan', max_songs=20)
artist._songs = [song for song in artist.songs if written_by(artist.name, song)]

for song in artist.songs:
    print(song.title, song.year)
