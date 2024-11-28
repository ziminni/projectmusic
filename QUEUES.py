import json
import random
from Track import Track

QUEUE_FILE = "Queue.json"

class MusicQueue:
    def __init__(self):
        self.queue = []
        self.unshuffledQueue = []
        self.currentIndex = 0
        self.repeat = False
        self.shuffle = False

    def addTrack(self, track: Track):
        self.queue.append(track)
        print(f"TRACK '{track.getTitle()}' ADDED TO THE QUEUE")

    def playNext(self):
        if not self.queue:
            print("QUEUE IS EMPTY")
            return None
        if self.repeat and self.currentIndex == len(self.queue) - 1:
            self.currentIndex = 0
        elif self.currentIndex < len(self.queue) - 1:
            self.currentIndex += 1
        else:
            print("END OF QUEUE")
            return None
        return self.queue[self.currentIndex]

    def playPrevious(self):
        if not self.queue:
            print("QUEUE IS EMPTY.")
            return None
        if self.repeat and self.currentIndex == 0:
            self.currentIndex = len(self.queue) - 1
        elif self.currentIndex > 0:
            self.currentIndex -= 1
        else:
            print("START OF QUEUE")
            return None
        return self.queue[self.currentIndex]

    def toggleRepeat(self):
        self.repeat = not self.repeat
        print(f"REPEAT IS NOW {'ON' if self.repeat else 'OFF'}")

    def toggleShuffle(self):
        if self.shuffle:
            self.queue = self.unshuffledQueue[:]
            self.shuffle = False
            print("SHUFFLE IS OFF")
        else:
            self.unshuffledQueue = self.queue[:]
            random.shuffle(self.queue)
            self.shuffle = True
            print("SHUFLE IS ON")

    def currentTrack(self):
        if self.queue:
            return self.queue[self.currentIndex]
        return None

    def displayQueue(self):
        for i, track in enumerate(self.queue):
            marker = "->" if i == self.currentIndex else "  "
            print(f"{marker} {track.getTitle()} - {track.getArtist()} ({track.getDuration()})")

    def saveQueue(self):
        data = {
            "queue": [track.to_dict() for track in self.queue],
            "currentIndex": self.currentIndex,
            "repeat": self.repeat,
            "shuffle": self.shuffle
        }
        with open(QUEUE_FILE, "w") as f:
            json.dump(data, f)

    def loadQueue(self):
        try:
            with open(QUEUE_FILE, "r") as f:
                data = json.load(f)
            self.queue = [Track.from_dict(track) for track in data["queue"]]
            self.unshuffledQueue = self.queue[:]
            self.currentIndex = data["currentIndex"]
            self.repeat = data["repeat"]
            self.shuffle = data["shuffle"]
        except FileNotFoundError:
            print("NO QUEUE FOUND")
    

# TEST SIGURO
queue = MusicQueue()

queue.add_track(Track("Song A", "Artist 1", "03:15"))
queue.add_track(Track("Song B", "Artist 2", "04:22"))
queue.add_track(Track("Song C", "Artist 3", "02:58"))

queue.toggle_shuffle()
queue.display_queue()
queue.toggle_shuffle()
queue.display_queue()

queue.toggle_repeat()
queue.play_next()
queue.play_next()
queue.play_next()