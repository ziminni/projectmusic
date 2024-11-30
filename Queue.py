from Track import Track
import random
import json

# wron implementation, follow to advice ni sir
class TrackQueue:
    def __init__(self):
        self.queue = []
        self.current_index = 0
        self.current_id = None  
        self.__repeat = False
        self.__shuffle = False

    def getShuffle (self):
        return "ON" if self.__shuffle else "OFF"
    
    def add_tracks(self):
        if not self.queue:
            with open("Store.json", "r") as file:
                data = json.load(file)
                self.queue.extend(data["Tracks"])
            if self.queue:
                self.current_index = 0
                self.current_id = self.queue[0]["id"]

    def next(self):
        if not self.queue:
            return None
        
        if self.current_index + 1 >= len(self.queue):
            self.current_index = 0 if self.repeat else len(self.queue) - 1
        else:
            self.current_index += 1
        self.current_id = self.queue[self.current_index]["id"]
        return self.current_track()

    def previous(self):
        if not self.queue:
            return None
        
        if self.current_index - 1 < 0:
            self.current_index = len(self.queue) - 1 if self.repeat else 0
        else:
            self.current_index -= 1
        self.current_id = self.queue[self.current_index]["id"]
        return self.current_track()

    def current_track(self):
        self.add_tracks()
        if not self.queue:
            return "No track is currently playing."
        

        current = self.queue[self.current_index]
        return f"{current['title']} by {current['artist']} ({current['duration']})"

    def shuffle(self):
        if not self.queue:
            return
        
        current_track = self.queue[self.current_index]
        random.shuffle(self.queue)
        self.current_index = self.queue.index(current_track)

        self.__shuffle = True 
        return self.__shuffle
        

    def unshuffle(self):
        if not self.queue:
            return
   
        with open("Store.json", "r") as file:
            data = json.load(file)
            original_tracks = data["Tracks"]  
        
        self.queue = original_tracks[:]
        
        current_track = self.queue[self.current_index]
        self.current_index = self.queue.index(current_track)

        self.__shuffle = False 
        return self.__shuffle
       

    def display_tracks(self, curpage=1, size=5):
        total_pages = (len(self.queue) + size - 1) // size
        if curpage < 1 or curpage > total_pages:
            print("Invalid page number.")
            return

        start = (curpage - 1) * size
        end = min(start + size, len(self.queue))

        print("\nTracks:")
        counter = start + 1
        for track in self.queue[start:end]:
            print(f"\t{counter}. {track['title']} by {track['artist']} ({track['duration']})")
            counter += 1

        print(f"\n< Page {curpage} of {total_pages} >\n")

