import json

class Track:
    def __init__(self, title, artist, album, duration):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__duration = duration

    def getTitle (self):
        return self.__title
    def getArtist (self):
        return self.__artist
    def getAlbum (self):
        return self.__album
    def getDuration (self):
        return self.__duration

    def to_dict(self):
        return {
            "title": self.__title,
            "artist": self.__artist,
            "album": self.__album,
            "duration": self.__duration
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["artist"], data["album"], data["duration"])