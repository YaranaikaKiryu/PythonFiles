class Playlist:
    def __init__(self):
        self.songs = []

    def addsong(self, song):
        self.songs.append(song)
        print(f"{song} has been added to the playlist.")

    def displayplaylist(self):
        if self.songs:
            print("Your Playlist:")
            for i, song in enumerate(self.songs, start=1):
                print(f"{i}. {song}")
        else:
            print("Your playlist is empty.")

def main():
    playlist = Playlist()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a song to the playlist")
        print("2. Display the playlist")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_songs = int(input("How many songs would you like to add? "))
            for _ in range(num_songs):
                song = input("Enter the name of the song: ")
                playlist.addsong(song)
                
        elif choice == "2":
            playlist.displayplaylist()
            
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()