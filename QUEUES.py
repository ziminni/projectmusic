import json
import os
from collections import deque

class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "duration": self.duration,
        }

    @staticmethod
    def from_dict(data):
        return Track(data["title"], data["artist"], data["duration"])

    def __str__(self):
        return f"{self.title} – {self.artist} ({self.duration})"

class MusicQueue:
    def __init__(self):
        self.queue = deque()
        self.current_index = 0
        self.repeat = False

    def add_track(self, track):
        self.queue.append(track)

    def play_next(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        if self.repeat and self.current_index == len(self.queue) - 1:
            self.current_index = 0  # Wrap to the start
        elif self.current_index < len(self.queue) - 1:
            self.current_index += 1
        else:
            print("End of queue.")
            return None
        return self.queue[self.current_index]

    def play_previous(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        if self.repeat and self.current_index == 0:
            self.current_index = len(self.queue) - 1  # Wrap to the end
        elif self.current_index > 0:
            self.current_index -= 1
        else:
            print("Start of queue.")
            return None
        return self.queue[self.current_index]

    def toggle_repeat(self):
        self.repeat = not self.repeat
        print(f"Repeat is now {'ON' if self.repeat else 'OFF'}.")

    def current_track(self):
        if self.queue:
            return self.queue[self.current_index]
        return None

    def save_queue(self):
        data = {
            "queue": [track.to_dict() for track in self.queue],
            "current_index": self.current_index,
            "repeat": self.repeat,
        }
        with open(QUEUE_FILE, "w") as f:
            json.dump(data, f)
        print("Queue saved.")

    def load_queue(self):
        try:
            with open(QUEUE_FILE, "r") as f:
                data = json.load(f)
            self.queue = deque(Track.from_dict(track) for track in data["queue"])
            self.current_index = data["current_index"]
            self.repeat = data["repeat"]
            print("Queue loaded.")
        except FileNotFoundError:
            print("No saved queue found.")

# Test code
if __name__ == "__main__":
    queue = MusicQueue()
    queue.load_queue()

    print("Adding sample tracks to the queue...")
    queue.add_track(Track("Song A", "Artist 1", "03:15"))
    queue.add_track(Track("Song B", "Artist 2", "04:22"))
    queue.add_track(Track("Song C", "Artist 3", "02:58"))

    print("\nInitial queue:")
    for track in queue.queue:
        print(track)

    print("\nTesting Repeat Off:")
    queue.toggle_repeat()  # Turn repeat ON
    queue.play_next()  # Move to next track
    print(f"Now playing: {queue.current_track()}")
    queue.play_next()  # Move to next track
    print(f"Now playing: {queue.current_track()}")
    queue.play_next()  # Should loop back to the start if repeat is ON
    print(f"Now playing: {queue.current_track()}")

    print("\nTesting Repeat On:")
    queue.toggle_repeat()  # Turn repeat OFF
    queue.play_next()  # Move to next track
    print(f"Now playing: {queue.current_track()}")
    queue.play_next()  # Try to move beyond the last track
    print(f"Now playing: {queue.current_track()}")

    queue.save_queue()

class MusicQueue:
    def __init__(self):
        self.queue = []
        self.current_index = 0
        self.repeat = False
        self.shuffle = False

    def add_to_queue(self, tracks):
        self.queue.extend(tracks)
        print(f"{len(tracks)} tracks added to the queue.")

    def play_next(self):
        if not self.queue:
            print("Queue is empty!")
            return

        self.current_index = (self.current_index + 1) % len(self.queue) if self.repeat else self.current_index + 1
        if self.current_index < len(self.queue):
            print(f"Now Playing: {self.queue[self.current_index]}")
        else:
            print("End of Queue.")

    def play_previous(self):
        if not self.queue:
            print("Queue is empty!")
            return

        self.current_index = (self.current_index - 1) % len(self.queue)
        print(f"Now Playing: {self.queue[self.current_index]}")

    def display_queue(self):
        print("Music Queue:")
        for i, track in enumerate(self.queue):
            marker = "->" if i == self.current_index else "  "
            print(f"{marker} {track}")

class Track:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

class MusicLibrary:
    def __init__(self, storage_file="MusicLibrary.json"):
        self.tracks = []
        self.storage_file = storage_file
        self.loadMusiclibrary()

    def add_track(self, title, artist, album, duration):
        track = Track(title, artist, album, duration)
        self.tracks.append(track)
        self.saveMusiclibrary()

    def loadMusiclibrary(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file) as file:
                data = json.load(file)
                for item in data:
                    self.add_track(item["title"], item["artist"], item["album"], item["duration"])

    def saveMusiclibrary(self):
        data = [
            {
                "title": # MAKE OG FORMAT ANI SA TRACK CLASS PARA COMPOSITION NALANG DAYON
                "artist": # MAKE OG FORMAT ANI SA TRACK CLASS PARA COMPOSITION NALANG DAYON
                "album": # MAKE OG FORMAT ANI SA TRACK CLASS PARA COMPOSITION NALANG DAYON
                "duration": # MAKE OG FORMAT ANI SA TRACK CLASS PARA COMPOSITION NALANG DAYON
            }
            # BUHATAN OG SMTH LIKE SELF.TRACKS TO PARA MA ACCESS OG MA SAVE
            for track in self.tracks # MURAG TRACK.SOMETHING2x
        ]
        with open(self.storage_file) as file:
            json.dump(data, file, indent=4)