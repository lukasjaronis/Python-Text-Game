from player import Player


# Room class

# Key value = name
# Value = description

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else:
            self.items = items


# N - North
# E - East
# S - South
# W - West

# Monika's Bedroom => Hallway
# Hallway => Monika's Bedroom
# Hallway => Outside

room = {
    "a1": Room('Monika\'s Bedroom', 'An adequate room, a white room, a lot of arts and a lot of plants. A cozy room.', items=['Kai']),
    "a2": Room('Hallway', 'The hallway leading to the living room.', items=['Bubbah']),
    "a3": Room('Outside', 'The backyard', items=['Flower'])
}

# Linking rooms together.
room['a1'].n_to = "a2"
room['a2'].s_to = "a1"
room['a2'].n_to = 'a3'

