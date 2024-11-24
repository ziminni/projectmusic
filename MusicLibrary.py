import json
from Track import Track

class MusicLibrary:
    def __init__(self):
        self.tracks = []
        self.playlists = []
        self.load_data()

    def load_data(self):
        try:
            with open("Store.json", "r") as file:
                data = json.load(file)
                self.tracks = [Track.from_dict(track) for track in data["tracks"]]
                self.playlists = data.get("playlists", [])
        except FileNotFoundError:
            print("Store.json not found. Starting with an empty library.")

    def save_data(self):
        data = {
            "tracks": [track.to_dict() for track in self.tracks],
            "playlists": self.playlists
        }
        with open("Store.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_track(self, track: Track):
        self.tracks.append(track)
        self.save_data()

    def view_tracks(self):
        if not self.tracks:
            print("No tracks available.")
        else:
            for i, track in enumerate(self.tracks, start=1):
                print(f"{i}. {track.getTitle()} - {track.getArtist()} ({track.getDuration()})")

    def create_playlist(self, name):
        if name not in [playlist['name'] for playlist in self.playlists]:
            self.playlists.append({"name": name, "tracks": []})
            self.save_data()
            print(f"Playlist '{name}' created successfully!")
        else:
            print(f"Playlist '{name}' already exists.")

    def view_playlists(self):
        if not self.playlists:
            print("No playlists available.")
        else:
            for i, playlist in enumerate(self.playlists, start=1):
                print(f"{i}. {playlist['name']} - {len(playlist['tracks'])} tracks")
                

if __name__ == "__main__":
    library = MusicLibrary()