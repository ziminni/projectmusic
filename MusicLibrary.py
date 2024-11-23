from Track import Track

class playlist:
    def __init__(self, name):
        self.name = name
        self.track = []
        
    def new_track(self, track):
        self.track.append(track)
        
    def total_duration(self):
        return sum(track.duration for track in self.track)
    
    def __str__(self):
        total_minutes, total_seconds = divmod(self.total_duration(), 60)
        return f'{self.name} - {total_minutes}:{total_seconds}'
    
    def view_track(self, start=0, end=5):
        if not self.track:
            print("There is no tracks available")
        else:
            for i, track in enumerate(self.track[start:end], start=start + 1): #try daw ni if mu work ba hehe
                print(f'{i}. {track.name} - {track.duration}')
            
            
    def view_playlist(self):
        for index, playlist in enumerate(self.playlist, start=1):
            print(f"{index}. {playlist}")
            
    def new_playlist(self, )
