from Track import Track

class playlist:
    def __init__(self, name):
        self.name = name
        self.playlist = []
        
    def new_track(self, track):
        self.track.append(track)
        
    def view_playlist(self):
        for index, playlist in enumerate(self.playlist, start=1):
            print(f"{index}. {playlist}")
            
    def new_playlist(self, )
