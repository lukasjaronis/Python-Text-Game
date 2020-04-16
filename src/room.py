from player import Player
import sys
from items import Item
from time import sleep

screen_width = 100


# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Room class

# Key value = name
# Value = description

class Room:
    new_game = True

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

    def __str__(self):
        if Room.new_game is True:
            output = f"\n\t{bcolors.OKBLUE}You are in {self.name}.\n \n\t{self.description}{bcolors.ENDC}\n"
            for character in output:
                sleep(0.05)
                sys.stdout.write(character)
                sys.stdout.flush()
            if self.items:
                output_items = f"\n{bcolors.FAIL}The following items in this area are...{bcolors.ENDC}\n"

                for character in output_items:
                    sleep(0.05)
                    sys.stdout.write(character)
                    sys.stdout.flush()
                value = ''

                for i in self.items:
                    value += f'\n\t ~ {i}'
                return value
        elif Room.new_game is False:
            print(
                f"\n\t{bcolors.OKBLUE}You are in {self.name}.\n \n\t{self.description}{bcolors.ENDC}\n")
            if self.items:
                print(f"\n{bcolors.FAIL}The following items in this area are...{bcolors.ENDC}\n")
                value = ''
                for i in self.items:
                    value += f'\n\t ~ {i}'
                return value


# N - North
# E - East
# S - South
# W - West

# Monika's Bedroom => Mario's Bedroom
# Monika's Bedroom => Hallway
# Mario's Bedroom => Monika's Bedroom
# Mario's Bedroom => Hallway
# Hallway => Monika's Bedroom
# Hallway => Mario'S Bedroom
# Hallway => Outside

room = {
    'a1': Room("Monika\'s Bedroom", 'An delightful room, a white room, a lot of art and a lot of plants. A cozy room.'),
    'a2': Room('Mario\'s Bedroom',
               'The room containing the worlds fastest computer, able to hack into the mainframe in less than 1 second.'),
    'a3': Room("a hallway", "The hallway leading to the living room."),
    'a4': Room("Outside", "The backyard")
}

# Linking rooms together.
room['a1'].n_to = 'a3'  # Monika's Bedroom => Hallway
room['a1'].e_to = 'a2'  # Monika's Bedroom => Mario's Bedroom

room['a2'].s_to = 'a1'  # Mario's Bedroom => Monika's Bedroom
room['a2'].e_to = 'a3'  # Mario's Bedroom => Hallway

room['a3'].s_to = 'a1'  # Hallway => Monika's Bedroom
room['a3'].e_to = 'a2'  # Hallway => Mario'S Bedroom
room['a3'].n_to = 'a4'  # Hallway => Outside

# Setting up Items
room['a1'].items = [Item('Kai', 'The Squirrel Hunter', 'Powerful K9\'s'),
                    Item('Blanket', 'A blanket with doggos scent on it', 'Snuggle attack'),
                    Item('Scientific Books', 'Learn the Wonders of the Universe', 'The power within')]
room['a2'].items = [Item('Vape', 'The cloud master 3000', 'Can kill by sick clouds'),
                    Item('Computer', 'JumpyWizard Mega v3', 'Can kill by graphics card'),
                    Item('Beer', 'Fat Tire', 'Black out')
                    ]
room['a3'].items = [Item('Bubba', 'The Wise One', 'Rat Attack'),
                    Item('Leash', 'Leash for dogs', 'Strangling'),
                    Item('Pretzels', 'A big tub of pretzels', 'Get Fat')
                    ]
room['a4'].items = [Item('Flower', 'Sun Flower', 'Powerful Scent')]
