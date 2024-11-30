import json
from Track import Track
from Queue import TrackQueue

# messy, add more class rearrange
class MusicLibrary:
    # def load_Track (self):
    #     data = json.load(file)
    #     try:
    #         with open("Store.json", "r") as file:
    #             return data["tracks"].append(self.addTrack.to_dict())
    #             # return json.load(file)
    #     except FileNotFoundError:
    #         self.addTrack = []

    def load_data(self):
        try:
            with open("Store.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"tracks": []}
    
    def save_library(self, data):
        with open("Store.json", "w") as file:
            # data = {"Tracks": [track.to_dict() for track in self.addTrack]}
            json.dump(data, file, indent=4)
        
    def store_Track (self, track):
        data = self.load_data()
        data["Tracks"].append(track.to_dict())
        
        self.save_library(data)

    def total_duration(self, data):
        data = self.load_data()
        counter = 0

        for data_duration in data["Tracks"]:
            parts = data_duration["duration"].split(":")
            minutes = int(parts[0])
            seconds = int(parts[1])

            total_sec = (minutes * 60) + seconds
            counter += total_sec

        hours = counter // 3600
        remaining_sec = counter % 3600
        minutes = remaining_sec // 60
        seconds = remaining_sec % 60

        if hours > 0:
            return f"{hours} hr/s {minutes} mins and {seconds}s"
        elif minutes > 0:
            return f"{minutes} mins and {seconds}s"
        else:
            return f"{seconds}s"
        
    def display_tracks (self, data, curpage=1, size=5):
        start = (curpage - 1) * size
        end = min(start + size, len(data["Tracks"]))
        totalPages = (len(data["Tracks"]) + size - 1) // size
        counter = start + 1

        for track in data["Tracks"][start:end]:
        # Access title, artist, and duration directly from the dictionary
             print (f"\t{counter}. {track['title']} by {track['artist']} ({track['duration']})")
             counter += 1

        if curpage < 1 or curpage > totalPages:
            return
        print(f"\n< Page {curpage} of {totalPages} >\n")

    def __str__ (self):
        data = self.load_data()
        queue = TrackQueue()
        s = "\n===============================================\n"
        s += "\t Music Library"
        s += "\n==============================================\n"
        total_duration = self.total_duration([track["duration"] for track in data.get("Tracks", [])])
        s += f"Total Duration: {total_duration}"
        s += f"\nShuffle: {queue.getShuffle()}"
        s += f"\nRepeat: \n"
        s += f"\nCurrently Playing (Paused): "

        return s
            
        
        
        
        
