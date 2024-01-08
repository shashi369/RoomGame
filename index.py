######################################################################
# Name:Shashi Bhandari
# Date:1/5/24
# Description:Room assignment
######################################################################
######################################################################
# the blueprint for a room
class Room:
    # the constructor

    def __init__(self, name):
    # rooms have a name, exits (e.g., south), exit locations
    # (e.g., to the south is room n), items (e.g., table), item
    # descriptions (for each item), and grabbables (things that
    # can be taken into inventory)
        self._name = name
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []
        self._bucket = []
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
    
    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    def addExit(self, exit, room):
        self._exits.append(exit)
        self._exitLocations.append(room)

    def addItem(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)

    def addGrabbable(self, item):
        self._grabbables.append(item)

    def delGrabbable(self, item):
        self._grabbables.remove(item)
    
    #Default thing
    
    def __str__(self):
        a = "You are in {}.\n".format(self.name)

        a += "You see: "

        for item in self.items:
            a += item + " "
        
        a += "\n Exists: "

        for exit in self.exits:
            a += exit + " "
        
        return a


def play_game():
    #Defining Rooms
    room1 = Room("Room 1")
    room2 = Room("Room 2")
    room3 = Room("Room 3")
    room4 = Room("Room 4")

    #Keeping the rooms in order and exists
    room1.addExit("east",room2)
    room1.addExit("south",room3)
    room2.addExit("west",room1)
    room2.addExit("south",room4)
    room3.addExit("north", room1)
    room3.addExit("east", room4)
    room4.addExit("north", room2)
    room4.addExit("west", room3)


    #adding items to rooms
    room1.addItem("chair","A very comfortable looking chair.")
    room1.addItem("table", "An old wood table with a picture of a girl and some messed up papers and documents on it.")
    room1.addGrabbable("key")
    room1.addGrabbable("picture")

    room2.addItem("rug","A soft and vivid rug")
    room2.addItem("fireplace", "old looking fireplace with some ashes")

    room3.addItem("bookshelves","A bookshelve made up of wood and books related to astromony, physics and philosophy")
    room3.addItem("staute","Statue of Nikola Tesla")
    room3.addItem("desk","A desk with some laboratory reagents and materials.")
    room3.addGrabbable("book")

    room4.addItem("brew rig","A beer brewing rig which is very clean. And a prepared 6 pack next to it")
    room4.addGrabbable("6-pack")

    #Starting the game with room 1

    current_room = room1

    while True:
        print(current_room)

        user_input = input("What do you want to do? ")

        magic_variable = user_input.split()
        
        if len(magic_variable) >=2:
            if magic_variable[0]=="go" and magic_variable[1] in current_room.exits:
                exit_index = current_room.exits.index(magic_variable[1])
                current_room = current_room.exitLocations[exit_index]
            elif magic_variable[0] == "look" and magic_variable[1] in current_room.items:
                item_index = current_room.items.index(magic_variable[1])
                print(current_room.itemDescriptions[item_index])
            elif magic_variable[0]=="take" and magic_variable[1] in current_room.grabbables:
                if magic_variable[1] == "picture":
                    print("Move on from that girl now you.")
                    break
                
                bucket.append(magic_variable[1])
                current_room.delGrabbable(magic_variable[1])
                print("YOu took the ",magic_variable[1])
            
            elif magic_variable[0]=="my" and magic_variable[1]=="bucket":
                print("you've got ",bucket)
            else:
                print("Invalid action. Please use 'go','take' or 'look' for verb. ")
        else:
            print("Invalid input use the commands 'go','take' or 'look' and noun.")
        
    
bucket = []
play_game()