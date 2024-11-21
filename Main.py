import json

from MusicLibrary import MusicLibrary
from Track import Track


MENUS = {
    "main" : {
        1: "View Playlist",
        2: "View Tracks",
        3: "Create new Track",
        4: "Create new Playlist"
    },
    "menu" : {
        11: "Play Queue",
        12: "Pause",
        13: "Shuffle",
        14: "Repeat"
    }
}

def showMenu(target: str, inline :int = None):
    print("\n<-----Menu----->")
    i = 1 if inline != None else None
    for menu in MENUS[target]:
        out = "[{}]".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1

def load_data():
    try:
        with open("Store.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tracks": [], "playlists": []}

def save_data(data):
    with open("Store.json", "w") as file:
        json.dump(data, file, indent=4)

def createTrack () -> Track:
    data = load_data()
    title = input("Enter title: ")
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    duration = input("Enter duration: ")
    single_track = Track(title, artist, album, duration)
    data["tracks"].append(single_track.to_dict())
    save_data(data)
    print(f"Track '{title}' by {artist} added successfully!")

if __name__ == "__main__":
    while True:
        showMenu ("main")
        opt = int(input("Enter option: "))
        if opt == 1:
            pass
        elif opt == 2:
            pass
        if opt ==3:
            pass
        elif opt == 4:
            createTrack()


# For accessing and manipulating the data sa JSON napud to apply some of the methods reqiired!! gdlck gaiss
