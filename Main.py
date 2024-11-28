import json
import os

# from MusicLibrary import MusicLibrary
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
        12: "Next Track",
        13: "Previous Track",
        14: "Turn on Shuffle",
        15: "Turn off Shuffle",
        16: "Turn on Repeat",
        17: "Turn off Repeat",
        18: "Clear Queue",
        19: "Exit"
    }
}

def showMenu(target: str, inline :int = None):
    i = 1 if inline != None else None
    for menu in MENUS[target]:
        out = "{} >>>".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1

def prompt(phrase: str) -> str:
    return input(phrase)

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

def musicTracks (data, page=1, pageSize=5):
    start = (page - 1) * pageSize
    end = min(start + pageSize, len(data["tracks"]))
    totalPages = (len(data["tracks"]) + pageSize - 1) // pageSize

    print("\nMusic Library")
    print("Total Duration: 12 min 17 sec")
    print("Tracks:")
    counter = 1
    
    for track_data in data["tracks"][start:end]:    
        track = Track.from_dict(track_data)  
        print (f"\t{counter} >> {track.getTitle()} — {track.getArtist()} ({track.getDuration()})")
        counter += 1

    if page < 1 or page > totalPages:
        return
    print(f"\n< Page {page} of {totalPages} >\n")

def playlistTracks ():
    pass




# PROGRAM MAIN
if __name__ == "__main__":
    data = load_data()
    while True:
        print("\n================================")
        print("\t MUSIC PLAYER")
        print("================================")
        showMenu ("main")
        opt = prompt("Enter option: ")
        if opt == '1':
            pageSize = 10  
            currPage = 1
            while True:
                musicTracks(data, currPage, pageSize)
                showMenu("menu")
                opt = prompt("Choose an option: ")

                if opt == '11':
                    pass
                elif opt == '12':
                    if currPage < (len(data["tracks"]) + pageSize - 1) // pageSize:
                        currPage += 1
                    print ("End of the list.")
                    
                elif opt == '13':
                    if currPage > 1:
                        currPage -= 1
                    print ("There's nothing to go back.")
                    
                elif opt == '14':
                    pass
                elif opt == '15':
                    pass
                elif opt == '16':
                    pass
                elif opt == '17':
                    pass
                elif opt == '18':
                    pass
                elif opt == '19':
                    break
                else:
                    print("Invalid option")
          
        elif opt == '2':
            pass
        if opt == '3':
            createTrack()
        elif opt == '4':
            pass


