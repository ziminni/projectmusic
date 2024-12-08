from Track import Track, Playlist_
from json_utilz import load, save
from Duration import total_duration, sec_to_min
from sort import merge_sort
from pagination import Pagination

class Playlist:
    def __init__(self):
        self.data = load()
        self.list = []

    def updatePlaylistList(self):
        self.list = []
        if "Playlists" in self.data:
            for playlist in self.data["Playlists"]:
                for name in playlist:
                    self.list.append(name)

    def createPlaylist(self):
        while True:
            playlistName = input("Enter Playlist Name: ")
            try:
                if "Playlists" not in self.data:
                    self.data["Playlists"] = []

                for playlist in self.data["Playlists"]:
                    if playlistName in playlist:
                        print("\nName already taken. Please choose another name.\n")
                        break

                else:  
                    self.data["Playlists"].append({playlistName: []})
                    save(self.data) 
                    print("\nPlaylist added successfully!\n")
                    
                    self.updatePlaylistList() 
                    break  

            except Exception as e:
                print(f"Error adding playlist: {e}")

    def displayTracks(self, playlist_index):
        self.updatePlaylistList()
        try:
            playlist_index = int(playlist_index) - 1

            playlist_name = self.list[playlist_index]

            for playlist in self.data["Playlists"]:
                if playlist_name in playlist:
                    tracks = playlist[playlist_name]
                    if not tracks:
                        print("\nNo tracks found in this playlist.")
                        return

                    print ("=" * 45)
                    print(f"Tracks in '{playlist_name}':")
                    print (f"Total duration: {total_duration(playlist, playlist_name)}")
                    sorted_tracks = merge_sort(tracks, key="title")
                    
                    pagination = Pagination(sorted_tracks, items_per_page=10)

                    while True:
                        print("\nTracks:")
                        start_index = (pagination.current_page - 1) * pagination.items_per_page
                        end_index = start_index + pagination.items_per_page
                        track_counter = start_index + 1


                        for track in sorted_tracks[start_index:end_index]:
                            print(f"\t[{track_counter}]   {track['title']} by {track['artist']} ({sec_to_min(track['duration'])})")
                            track_counter += 1
                        print(f"\n---------------- Page {pagination.current_page} of {pagination.total_pages()} ----------------")

                        choice = input("\nOptions: [1] Next Page | [2] Previous Page | [E] Exit out of page: ").lower()
                        if choice == "1":
                            pagination.next_page()
                        elif choice == "2":
                            pagination.previous_page()
                        elif choice == "e":
                            break
                        else:
                            print("\nInvalid choice. Please try again.")
                            input("\nPress [Enter] to exit...")
                    return

        except (ValueError, IndexError):
            print("\nInvalid input. Please enter a valid playlist number.")
    
    def displayPlaylists(self):
        self.updatePlaylistList()
        if not self.list:
            print("There are no Playlists made!")
            return
        
        pagination = Pagination(self.list, items_per_page=10)
        while True:
            print("\nTracks:")
            start_index = (pagination.current_page - 1) * pagination.items_per_page
            end_index = start_index + pagination.items_per_page
            counter = start_index + 1


            for playlist_name in self.list[start_index:end_index]:
                print(f"\t[{counter}]   {playlist_name}")
                counter += 1
            print(f"\n---------------- Page {pagination.current_page} of {pagination.total_pages()} ----------------")

            choice = input("\nOptions: [N] Next Page | [P] Previous Page | [E] Exit out of page: ").lower()
            if choice == "n":
                pagination.next_page()
            elif choice == "p":
                pagination.previous_page()
            elif choice == "e":
                break
            else:
                print("\nInvalid choice. Please try again.")
                input("\nPress [Enter] to exit...")


    def searchTrack(self, track):
        self.data = load()

        tracks = self.data.get("Tracks", [])
        if not tracks:
            print("\nNo tracks available in the music library.")
            return []

        track_lower = track.lower()
        results = [
            track for track in tracks
            if track_lower in track["title"].lower()
            or track_lower in track["artist"].lower()
            or track_lower in track["album"].lower()
        ]

        print(f"\nTracks matching '{track}':")
        
        counter = 1
        for track in results:
            print(f"    [{counter}] {track['title']} by {track['artist']} ({track['duration']})")
            counter += 1

        return [track for track in results]


    def searchedTracks(self, option, playlist_name, matching_tracks):
        
        if option == 1:
            track_index = int(input("\nSelect a track to add (Enter number): ")) - 1
            if track_index < 0 or track_index >= len(matching_tracks):
                return "\nInvalid track selection."
            
            selected_track = matching_tracks[track_index]

            for playlist in self.data["Playlists"]:
                if playlist_name in playlist:
                    if selected_track in playlist[playlist_name]: 
                        return "\nTrack is already in the playlist."
                        
                    playlist[playlist_name].append(selected_track)
                    save(self.data)
                    return f"\nTrack '{selected_track['title']}' added to playlist '{playlist_name}'."
                    
        elif option == 2:
            for selected_track in matching_tracks:
                for playlist in self.data["Playlists"]:
                    if playlist_name in playlist:
                        if selected_track in playlist[playlist_name]:
                            print ("\n Tracks is already in the playlist.")
                        playlist[playlist_name].append(selected_track)
            save(self.data)
            print (f"\nAll matching tracks added to playlist '{playlist_name}'.")
            return
            

        else:
            print("\nInvalid option selected.")
            return

            

    def addTrack (self, playlist_name):
        index = int(input("\nSelect a track to add (Enter number): ")) - 1

        if index < 0 or index >= len(self.data["Tracks"]):
            print("\nInvalid track selection.")
    
        selected_track = self.data["Tracks"][index]

        for playlist in self.data["Playlists"]:
            if playlist_name in playlist:
                if selected_track in playlist[playlist_name]:
                    print("\nTrack is already in the playlist.")
                    
                playlist[playlist_name].append(selected_track)
                save(self.data)
                print(f"\nTrack '{selected_track['title']}' added to playlist '{playlist_name}'.")
 