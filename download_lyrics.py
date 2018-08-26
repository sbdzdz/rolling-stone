import configparser
import lyricsgenius as genius

def written_by(author, song):
    writers = [w[0] for w in song.writer_artists]
    return not writers or author in writers

config = configparser.ConfigParser()
config.read('config.ini')
token = config['GENIUS']['ACCESS_TOKEN']

api = genius.Genius(token)
bob = api.search_artist('Bob Dylan')
bob._songs = [s for s in bob.songs if written_by(bob.name, s)]
bob.save_lyrics(filename='data/dylan')
