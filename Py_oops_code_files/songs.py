# Exercise 31: Playlist Class with Add, Remove & Shuffle

import random
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f'{song.title} added to Playlist.')
        else:
            print(f'{song.title} is already in Playlist.')

    def remove_song(self, title):
        songs_count = len(self.songs)
        # adding to all songs back self.songs except the song that must be removed.
        self.songs  = [song for song in self.songs if song.title != title]
        if songs_count == len(self.songs):
            print(f'Song {title} not found in Playlist.')
        else:
            print(f'{title} removed from Playlist.')

    def shuffle(self):
        shuffled = random.shuffle(self.songs)


    def all_songs(self):
        titles = [song.title for song in self.songs]
        print(f'Playlist:{' | '.join(titles)}')

playlist = Playlist('Divine Vibes')
playlist.add_song(Song("Om Mahaprana Deepam", "Shankar Mahadevan"))
playlist.add_song(Song("Bhagyada Lakshmi Baramma", "Rajeev & Sooryagayathri"))
playlist.add_song(Song("Lingashtakam", "SPB"))
playlist.add_song(Song("Ragvendra Raghavendra Yenniri", "Dr.Rajkumar"))


playlist.all_songs()
playlist.remove_song("Om Mahaprana Deepam")
playlist.shuffle()
print('After Shuffle:', end = ' ')
playlist.all_songs()