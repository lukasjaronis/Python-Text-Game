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
        output = f"{bcolors.HEADER}You are in {self.name}. {self.description}{bcolors.ENDC}\n"
        print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(output))))
        for character in output:
            sleep(0.05)
            sys.stdout.write(character)
            sys.stdout.flush()
        print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(output))))
        if self.items:
            output_items = f"\nThe following items in this area are...\n"

            for character in output_items:
                sleep(0.05)
                sys.stdout.write(character)
                sys.stdout.flush()
            value = ''

            for i in self.items:
                value += f'\n\t ~ {i}'
            return value


# N - North
# E - East
# S - South
# W - West

# Monika's Bedroom => Hallway
# Hallway => Monika's Bedroom
# Hallway => Outside

room = {
    'a1': Room("Monika\'s Bedroom",
               "\nAn adequate room, a white room, a lot of arts and a lot of plants. A cozy room."),
    'a2': Room("a hallway", "The hallway leading to the living room."),
    'a3': Room("Outside", "The backyard")
}

# Linking rooms together.
room['a1'].n_to = 'a2'
room['a2'].s_to = 'a1'
room['a2'].n_to = 'a3'

# Setting up Items
room['a1'].items = [Item('Kai', 'The Squirrel Hunter', 'Powerful K9\'s'),
                    Item('Blanket', 'A blanket with doggos scent on it', 'Snuggle attack'),
                    Item('Scientific Books', 'Learn the Wonders of the Universe', 'The power within.')]
room['a2'].items = [Item('Bubba', 'The wise one', 'Rat Attack')]
room['a3'].items = ['Flower']



