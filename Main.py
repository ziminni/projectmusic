from Track import Track
from MusicLibrary import MusicLibrary
from Queue import TrackQueue

# Remember:
# Very messy OOP
# Inefficient calcduration/totalduration
# Queues wrong approach
# Sugda na ang playlist!!!

MENUS = {
    "main" : {
        1 : "Create new Track",
        2 : "View All Tracks",
        3 : "Create Playlist",
        4 : "View All Playlist",
        5 : "Exit Program"
    },
    "menu" : {
        1 : "Next Page",
        2 : "Previous Page",
        3 : "Turn on Shuffle",
        4 : "Turn off Shuffle",
        5 : "Turn on Repeat",
        6 : "Turn off Repeat",
        7 : "Add Track to Playlist",
        8 : "Exit to main menu"
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
    return input(phrase).lower()



if __name__ == "__main__":
    data = MusicLibrary()
    load = data.load_data()
    queue = TrackQueue()
    while True:
        print ("\n===== Music Player =====\n")
        showMenu("main")
        opt = prompt("\nChoose an option: ")
        if opt == '1':
            id = load["counter"]
            title = input("Enter Track Title: ")
            artist = input("Enter Track Artist: ")
            album = input("Enter Track Album: ")
            duration = input("Enter Track Duration (mm:ss): ")
   
            try:
                track = Track(id, title, artist, album, duration)
                data.store_Track(track)

                load = data.load_data()
            
            except ValueError as e:
                print(f"Error adding track: {e}")

        elif opt == '2':
            psize = 10  
            currpage = 1
            totpage = (len(load["Tracks"]) + psize - 1) // psize
            
            while True:
            
                print (data)
                print("\t",queue.current_track())
                queue.display_tracks(currpage, psize)

                print ("============= menu ===============")
                print (" [P] Prev << [Q] Play >> [N] Next ")
                print ("==================================")
                showMenu("menu")
                opt = prompt("Choose an option: ")
                if opt == 'q':  
                    pass
        
                elif opt == 'p': 
                    track = queue.previous()
            
                elif opt == 'n':  
                    queue.next()

                elif opt == '1': 
                    if currpage < totpage:
                        currpage += 1
                    else:
                        print("You are already on the last page.")

                elif opt == '2':  
                    if currpage > 1:
                        currpage -= 1
                    else:
                        print("You are already on the first page.")
                
                elif opt == '3':
                    queue.shuffle()
             
                        
                elif opt == '4': 
                    queue.unshuffle()
               

                elif opt == '5':
                    pass

                else:
                    print("Invalid option. Please try again.")

