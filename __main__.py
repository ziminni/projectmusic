from Track import Track
from MusicLibrary import MusicLibrary
from Playlist import Playlist
from json_utilz import load, save
from Duration import total_duration
from queue_ import Queue
from sort import merge_sort
from pagination import Pagination

class main:
    def __init__(self):
        self.library = MusicLibrary()
        self.playlist = Playlist()
        self.data = load()

    @staticmethod
    def prompt(args: str) -> str:
        return input(args).lower()

    def main(self):
        while True:
            print("\n========= WELCOME =========")
            print("   [P] Open Music Player")
            print("===========================")
            print("MENU:\n    1 >> Create new Track\n    2 >> View All Tracks\n    3 >> Create Playlist\n    4 >> View All Playlist\n    0 >> Exit Program")
            choice = main.prompt("\nEnter choice: ")

            if choice == "p":
                while True:
                    print("\n========= MUSIC PLAYER =========")
                    print("1 >> Play from Library\n2 >> Play from Playlist\n0 >> Exit main menu")
                    choice = main.prompt("\nEnter choice: ")

                    # Music Library - music player
                    if choice == '1':  
                        while True:
                            try:
                                # Load data and initialize the queue
                                self.data = load()
                                tracks = merge_sort(self.data["Tracks"][:], "title")
                                queue = Queue()

                                print("=" * 45)
                                print("\t       Music Library")
                                print("=" * 45)

                                print(f"Total duration: {total_duration(self.data, 'Tracks')}")

                                for track in tracks:
                                    queue.enqueue(track)

                                current = queue.current_play()  
                                print(f"\nCurrently Playing (Playing): \n\t{current}")

                                # Main loop for music player
                                while True: 
                                        
                                    print(f"\nShuffle: {queue.shuffle_status()}")
                                    print(f"Repeat: {queue.repeat_status()}\n")

                                    print(queue)

                                    print("\nOption: [N] Next [P] Previous")
                                    print("=" * 45)
                                    print("[1] Playback Option\n[2] Exit Music Player")
                                    choice = main.prompt("\nEnter your choice: ")

                                    if choice == '2':
                                        break  # Exit the music player

                                    if choice == 'n':  # Next track
                                        queue.next()
                                        current = queue.current_play()  
                                        print(f"\nCurrently Playing (Playing): \n\t{current}")

                                    elif choice == 'p':  # Previous track
                                        queue.prev()
                                        current = queue.current_play()  
                                        print(f"\nCurrently Playing (Playing): \n\t{current}")

                                    elif choice == '1':  # Playback options
                                        print("\n[1] Toggle Shuffle\n[2] Toggle Repeat")
                                        option = main.prompt("Enter your choice: ")

                                        if option == '1':
                                            queue.toggle_shuffle()
                                        elif option == '2':
                                            queue.toggle_repeat()

                            except Exception as e:
                                print(f"An error occurred: {e}")
                                restart = main.prompt("Would you like to try again? (y/n): ")
                                if restart.lower() != 'y':
                                    break
                            break


                 
                    elif choice == '2':  # Play from Playlist
                        queue = Queue()
                        print("=" * 45)
                        print("\t       Music Player - Playlist")
                        print("=" * 45)
                        print("Select a Playlist to Play:")

                        self.playlist.displayPlaylists()
                        print ("\n    [0] Go back")

                        try:
                            playlist_choice = int(main.prompt("\nEnter playlist number: "))
                            self.playlist.updatePlaylistList()


                            if playlist_choice == 0:
                                break

                            elif playlist_choice <= 0 or playlist_choice > len(self.playlist.list):
                                print("\nInvalid input. Please enter a valid playlist number.")
                                continue

                            playlist_name = self.playlist.list[playlist_choice - 1]
                            playlist_tracks = []
                            for playlist in self.playlist.data["Playlists"]:
                                if playlist_name in playlist:
                                    playlist_tracks = playlist[playlist_name]
                                    break

                            if not playlist_tracks:
                                print("\nNo tracks found in this playlist.")
                                continue
                            
                            sorted_tracks = merge_sort(playlist_tracks, key="title")
                            queue.enqueue_playlist(sorted_tracks)

                            print(f"\nNow Playing from Playlist: {playlist_name}")

                            current = queue.current_play()  
                            print(f"\nCurrently Playing (Paused): \n\t{current}") 

                            while True:
                                print(f"\nShuffle: {queue.shuffle_status()}")
                                print(f"Repeat: {queue.toggle_repeat()}\n")

                                print(queue.display())
                                
                                print("\nOption: [N] Next [P] Previous [Q] Play Queue")
                                print("=" * 45)
                                print("[1] Playback option\n[2] Exit Music Player")
                                choice = main.prompt("\nEnter your choice: ")

                                # Next Track
                                if choice == 'n':
                                    queue.next() 
                                    current = queue.current_play()  
                                    print(f"\nCurrently Playing: {current}")  
                                
                                # Previous Track
                                elif choice == 'p':
                                    queue.prev()
                                    current = queue.current_play()  
                                    print(f"\nCurrently Playing: {current}")

                                elif choice == 'q':
                                    pass

                                # Toggle Shuffle or Repeat
                                elif choice == '1':
                                    print("[1] Toggle shuffle\n[2] Toggle repeat")
                                    opt = main.prompt("Enter your choice: ")

                                    if opt == '1':
                                        print(queue.toggle_shuffle())

                                    elif opt == '2':
                                        print(queue.toggle_repeat())

                                # Exit music player
                                elif choice == '2':
                                    break
                        except (ValueError, IndexError):
                            print("\nInvalid input. Please enter a valid number.")

                    # Exit to main menu
                    elif choice == '0':
                        break

            elif choice == '1':
                self.library.createTrack()
                self.data = load ()
            
            elif choice == '2':
                print("=" * 45)
                print("\t       Music Library")
                print("=" * 45)
                print(f"\nTotal duration: {total_duration(self.data, "Tracks")}")
                self.library.displayTracks()
                input("\nPress [Enter] to exit...")

            elif choice == '3':
                self.playlist.createPlaylist()

            elif choice == '4':
                while True:
                    print("=" * 45)
                    print("\t          Playlists")
                    print("=" * 45)

                    print("Available Playlist: ")
                    self.playlist.displayPlaylists()
                    print("\n    [A] Add tracks to playlist")
                    print("    [E] Exit main menu")
                    choice = main.prompt("\nEnter number of the Playlist: ")
              
                    if choice == 'a':
                        while True:
                            try:
                                print("\nAvailable Playlists: ")
                                self.playlist.displayPlaylists()

                                playlist_index = int(input("\nSelect a playlist to add tracks to (Enter number): ")) - 1

                                if 0 <= playlist_index < len(self.playlist.list):
                                    playlist_name = self.playlist.list[playlist_index]
                                    break  
                                else:
                                    print("\nInvalid playlist selection. Please try again.")

                            except ValueError:
                                print("\nInvalid input. Please enter a valid number.")


                        while True:
                            try:
                                print("\nOptions:")
                                print("    [1] Select from all tracks")
                                print("    [2] Search for tracks")
                                option = int(input("\nChoose an option (1 or 2): "))

                                if option == 1:
                                    print("\nAvailable Tracks in Music Library:")
                                    counter = 1
                                    for track in self.data["Tracks"]:
                                        print(f"    [{counter}] {track['title']} by {track['artist']} ({track['duration']})")
                                        counter += 1

                                    self.playlist.addTrack(playlist_name)
                                    break  

                                elif option == 2:
                                    query = input("\nEnter search query (title, artist, or album): ")
                                    matching_tracks = self.playlist.searchTrack(query)

                                    if not matching_tracks:
                                        print("\nNo matching tracks found. Returning to main menu.")
                                        break  

                                    while True:
                                        try:
                                            print("\nOptions:")
                                            print("    [1] Add a specific track")
                                            print("    [2] Add all matching tracks")
                                            choice = int(input("\nChoose an option (1 or 2): "))

                                            if choice == 1:
                                                self.playlist.searchedTracks(1, playlist_name, matching_tracks)
                                                break  
                                            elif choice == 2:
                                                self.playlist.searchedTracks(2, playlist_name, matching_tracks)
                                                break 
                                            else:
                                                print("\nInvalid choice. Please select 1 or 2.")
                                        except ValueError:
                                            print("\nInvalid input. Please enter a number (1 or 2).")

                                else:
                                    print("\nInvalid option. Please choose 1 or 2.")
                            except ValueError:
                                print("\nInvalid input. Please enter a valid number.")



                    elif choice == 'e':
                        print("Going back!")
                        break

                    elif int(choice) == 0 or int(choice) < 0:
                        print("\nInvalid input. Please enter a valid playlist number.")
                        continue

                    elif int(choice) > 0 or int(choice) <= len(self.playlist.list):
                        self.playlist.displayTracks(choice)
                        input("\nPress [Enter] to exit...")

            elif choice == '0':
                print("Terminating Application...")
                break

if __name__ == "__main__":
    run = main()
    run.main()
