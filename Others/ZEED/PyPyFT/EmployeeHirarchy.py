# class Song:
#     def __init__(self, title, artist, year):
#         self.title = title
#         self.artist = artist
#         self.year = year

# class Album:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#         self.songs = []

#     def add_song(self, title, year):
#         song = Song(title, self.artist, year)
#         self.songs.append(song)

# class Artist:
#     def __init__(self, name):
#         self.name = name
#         self.albums = []
#         self.songs = []

#     def add_album(self, album):
#         self.albums.append(album)

#     def add_song(self, song):
#         self.songs.append(song)

# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)


# createArtist = input("Enter Name of Artist >> ")
# artist = Artist(createArtist)

# createAlbum = input("Enter Album Name >> ")
# album = Album(createAlbum, artist)
# artist.add_album(album)

# num_of_songs = int(input("Enter Number of Songs >> "))
# for x in range(num_of_songs):
#     song_title = input(f"Enter Song Name {x+1} >> ")
#     releaseYear = int(input(f"Enter Release Year for the Song {x+1}>> "))
#     album.add_song(song_title, releaseYear)

# song_title = input("Enter Song Title >> ")
# release_year = int(input("Release Year >> "))
# artist_song = Song(song_title, artist ,release_year)
# artist.add_song(artist_song)

# playlist_name = input("Enter Playlist Name >> ")
# playlist = Playlist(playlist_name)
# playlist.songs.extend(album.songs)
# playlist.songs.append(artist_song)

# print("\nSongs in the playlist:")
# for song in playlist.songs:
#     print(f"{song.title} by {song.artist.name} ({song.year})")

# print("\nArtist's songs:")
# for song in artist.songs:
#     print(f"{song.title} ({song.year})")


class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

class Album:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist, year):
        song = Song(title, artist, year)
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
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

# Create an artist
artist_name = input("Enter the artist's name: ")
artist = Artist(artist_name)

# Create an album
album = Album()

# Use add_song from the Album class to create a song for the artist
song_title = input("Enter the song title: ")
song_year = int(input("Enter the song's release year: "))
album.add_song(song_title, artist, song_year)

# Add all songs from the album to the playlist
playlist = Playlist()
for song in album.songs:
    playlist.add_song(song)

# Print all the songs in the playlist
print("Songs in the playlist:")
for song in playlist.songs:
    print(song.title)

# Print all the artist's songs
print(f"Songs by {artist.name}:")
for song in artist.songs:
    print(song.title)