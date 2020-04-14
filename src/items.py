# This is just an item class to handle item information. Thats it.


class Item:
    def __init__(self, name, description, power):
        self.name = name
        self.description = description
        self.power = power

    def __str__(self):
        return f'{self.name}. {self.description}. Power: {self.power}'
