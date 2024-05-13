class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.songs = []

    def add_song(self, title, year):
        song = Song(title, self.artist, year)
        self.songs.append(song)

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

# Create an artist
artist_name = input("Enter artist's name: ")
artist = Artist(artist_name)


album_title = input("Enter album title: ")
album = Album(album_title, artist)


num_songs = int(input("How many songs do you want to add to the album? "))
for i in range(num_songs):
    song_title = input(f"Enter title for song {i+1}: ")
    release_year = int(input(f"Enter release year for song {i+1}: "))
    album.add_song(song_title, release_year)


song_title = input("Enter song title: ")
release_year = int(input("Enter release year: "))
artist_song = Song(song_title, artist, release_year)
artist.add_song(artist_song)


playlist_name = input("Enter playlist name: ")
playlist = Playlist(playlist_name)
playlist.songs.extend(album.songs)
playlist.songs.append(artist_song)  


print("\nSongs in the playlist:")
for song in playlist.songs:
    print(f"{song.title} by {song.artist.name} ({song.year})")


print("\nArtist's songs:")
for song in artist.songs:
    print(f"{song.title} ({song.year})")
