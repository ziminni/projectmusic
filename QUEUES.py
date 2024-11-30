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
        self.repeatSong = None

    def addTrack(self, track: Track):
        self.queue.append(track)
        print(f"TRACK '{track.getTitle()}' ADDED TO THE QUEUE")

    def toggleRepeat(self, song=None):
        if song:
            if self.repeat and self.repeatSong  == song:
                self.repeat = False
                self.repeatSong = None
                print(f"REPEAT IS OFF FOR '{song.getTitle()}'")
            else:
                self.repeat = True
                self.repeatSong = song
                print(f"REPEAT IS ON FOR '{song.getTitle()}'")
        else:
            self.repeat = not self.repeat
            self.repeatSong = None
            print(f"REPEAT IS NOW {'ON' if self.repeat else 'OFF'}")

    def playNext(self):
        if not self.queue:
            print("QUEUE IS EMPTY")
            return None
        if self.repeat and self.repeatSong:
            print(f"REPEATING '{self.repeatSong.getTitle()}'")
            return self.repeatSong 
        if self.currentIndex < len(self.queue) - 1:
            self.currentIndex += 1
        else:
            if self.repeat:
                self.currentIndex = 0  
                print(f"REPEATING QUEUE FROM START")
            else:
                print("END OF QUEUE")
                return None
        return self.queue[self.currentIndex]
    
    def playPrevious(self):
        if not self.queue:
            print("QUEUE IS EMPTY.")
            return None
        if self.repeat and self.repeatSong:
            print(f"REPEATING '{self.repeatSong.getTitle()}'")
            return self.repeatSong
        if self.currentIndex > 0:
            self.currentIndex -= 1
        else:
            if self.repeat:
                self.currentIndex = len(self.queue) - 1  
                print(f"REPEATING QUEUE FROM END")
            else:
                print("START OF QUEUE")
                return None
        return self.queue[self.currentIndex]

    def toggleShuffle(self):
        if self.shuffle:
            self.queue = self.unshuffledQueue[:]
            self.shuffle = False
            print("SHUFFLE IS OFF")
        else:
            self.unshuffledQueue = self.queue[:]
            random.shuffle(self.queue)
            self.shuffle = True
            print("SHUFFLE IS ON")

    def currentTrack(self):
        if self.queue:
            return self.queue[self.currentIndex]
        return None

    def displayQueue(self):
        if not self.queue:
            print("QUEUE IS EMPTY")
            return
        print("CURRENT QUEUE:")
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

queue.addTrack(Track("Song A", "Artist 1", "Album A", "03:15"))
queue.addTrack(Track("Song B", "Artist 2", "Album B", "04:22"))
queue.addTrack(Track("Song C", "Artist 3", "Album C", "02:58"))

queue.toggleShuffle()
queue.displayQueue()
queue.toggleShuffle()
queue.displayQueue()

queue.toggleRepeat()
queue.playNext()
queue.playNext()
queue.playNext()