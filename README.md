# RoomGame
<b>It's an assignment to create a room game using OOP.</b>

The game
The first step to designing any kind of computer program is to establish the goal or purpose and to
identify all of the necessary details. This is very similar to first understanding a problem before setting
about to solve it. Although we will build a very simple game, it can still have (very simple) goals.
The setting of the game is a small “mansion” consisting of four rooms. Here's the layout:
1
Each room has various exits that lead to other rooms in the mansion. In addition, each room has items,
some of which can simply be observed, and others that can be picked up and added to the player's
inventory. For this activity, there is no actual goal for the player other than to move about the mansion,
observe various items throughout the rooms in the mansion, and add various items found in the rooms to
inventory. There is an end state that results in death, however! Of course, this doesn't prevent extending
the game with a better story and more variety (some ideas will be discussed later).
The four rooms are laid out in a simple square pattern. Room 1 is at the top-left of the mansion, room 2
is at the top-right, room 3 is at the bottom-left, and room four is at the bottom-right. Each room has
items that can be observed:
• Room 1: A chair and a table;
• Room 2: A rug and a fireplace;
• Room 3: Some bookshelves, a statue, and a desk; and
• Room 4: A brew rig (you know, to brew some delicious libations).
Observable items can provide useful information (once observed) and may reveal new items (some of
which can be placed in the player's inventory). In addition, each room may have some items that can be
grabbed by the player and placed in inventory:
• Room 1: A key;
• Room 3: A book; and
• Room 4: A 6-pack of a recently brewed beverage.
The rooms have various exits that lead to other rooms in the mansion:
• Room 1: An exit to the east that leads to to room 2, and an exit to the south that leads to room 3;
• Room 2: An exit to the south that leads to room 4, and an exit to the west that leads to room 1;
• Room 3: An exit to the north that leads to room 1, and an exit to the east that leads to room 4;
and
• Room 4: An exit to the north that leads to room 2, an exit to the west that leads to room 3, and an
(unlabeled) exit to the south that leads to...death! Think of it as jumping out of a window.
The gameplay
The game is text-based (egads, there are no graphics!). Situational awareness is provided by means of
meaningful text that describes the current situation in the mansion. Information such as which room the
player is located in, what objects are in the current room, and so on, is continually provided throughout
the game. The player is prompted for an action (i.e., what to do) after which the current situation is
updated.
The game supports a simple vocabulary for the player's actions that is composed of a verb followed by a
noun. For example, the action “go south” instructs the player to take the south exit in the current room
(if that is a valid exit). If the specified exit is invalid (or, for example, if the player misspells an action),
an appropriate response is provided, instructing the player of the accepted vocabulary. Supported verbs
are: go, look, and take. Supported nouns depend on the verb; for example, for the verb go, the nouns
north, east, south, and west are supported. This will allow the player to structure the following go
commands:
• go north
• go east
2
• go south
• go west (young man!)
The verbs look and take support a variety of nouns that depend on the actual items located in the rooms
of the mansion. The player cannot, for example, “look table” in a room that doesn't have a table! Some
examples of look and take actions are:
• look table
• take key
The gameplay depends on the user's input. Rooms change based on valid go actions, meaningful
information is provided based on valid look actions, and inventory is accumulated based on valid take
actions. For this game, gameplay can continue forever or until the player decides to “go south” in room
4 and effectively jump out of the window to his/her death:
At any time, the player may issue the following actions to leave the game:
• quit
• exit
• bye