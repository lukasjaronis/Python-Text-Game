# Player Information
# Items
# Player Name
# Player Role
#############
# Monika
# Kai
# Squirrel
#############
# Current Room


class Player:
    def __init__(self):
        self.player_status = True
        self.name = None
        self.player_role = None
        # starting point of the player.
        self.player_location = 'a1'
        # We're checking if player has finished the game or not
        self.end_game = False
        # player items
        items = None

        # If there are no items then it becomes an empty array, else the array is populated if its not empty
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item):
        # adding passed in item to the array
        self.items.append(item)
        print(f"You've picked up {item}!")

    def drop_item(self, item):
        # removing item from array
        self.items.remove(item)
        print(f"{self.name}, you've dropped {self.item}!")
