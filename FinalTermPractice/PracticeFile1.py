class Playlist:
    def __init__(self):
        self.songs = []
       
    def add_song(self, song_name, song_artist):
        song = {"name": song_name, "artist": song_artist}
        self.songs.append(song)
        print(f"{song_name} has been added to the playlist.")
    
    def remove_song(self, song_name):
        for song in self.songs:
            if song["name"] == song_name:
                self.songs.remove(song)
                print(f"{song_name} has been removed from the playlist.")
                return
        print(f"{song_name} not found in the playlist.")
    
    def display_info(self):
        for song in self.songs:
            print(f"{song['name']} by {song['artist']}")

def main():
    playlist = Playlist()
    
    while True:
        print("====ALBUM PLAYLIST====")
        print("1. Add a song to the playlist")
        print("2. Remove a song from the playlist")
        print("3. Display the playlist")
        print("4. Exit")
        print("======================")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            song_name = input("Enter the name of the song: ")
            song_artist = input("Enter the name of the artist: ")
            playlist.add_song(song_name, song_artist)
        
        elif choice == 2:
            song_name = input("Enter the name of the song: ")
            playlist.remove_song(song_name)
        
        elif choice == 3:
            playlist.display_info()
            
        elif choice == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")
            
main()