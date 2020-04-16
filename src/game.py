import sys
import os
from time import sleep
from items import Item
from player import Player
from room import room, Room


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


# Init player
user = Player()


# Title Screen

def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        print("Shutting off. Thank you for playing.")
        os.system('cls')
        sys.exit()
        # If command is not within the below array it will keep bringing up an input
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            print("Shutting off. Thank you for playing.")
            os.system('cls')
            sys.exit()


def title_screen():
    os.system('cls')
    print('###########################################')
    print("      Welcome to Mokai Adventure Game!     ")
    print('###########################################')
    print('                ~ Play ~                   ')
    print('                ~ Help ~                   ')
    print('                ~ Quit ~                   ')
    print('###########################################')
    print('###########################################')
    title_screen_selections()


# Help Menu

def help_menu():
    os.system('cls')
    print('###########################################')
    print("      Welcome to Mokai Adventure Game!     ")
    print('###########################################')
    print("         Type ['n', 'e', 's', 'w']         ")
    print("         to move throughout the game       ")
    print("                'n' = North                ")
    print("                'e' = East                 ")
    print("                's' = South                ")
    print("                'w' = West                 ")
    print("           'pu' = Pick Up an Item          ")
    print("           'drop' = Drop an Item           ")
    print('###########################################')
    print("                'q' = Quit                 ")
    print('###########################################')
    print("                Have fun!                  ")
    print('###########################################')
    print('###########################################')
    print('                ~ Back ~                   ')
    option = input("> ")
    if option.lower() == "back":
        title_screen()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['back', 'quit']:
        print("Invalid command. Try typing 'Back' if you want to go back to the main menu.")
        print("Else, you can quit by typing 'Quit' ")
        option = input("> ")
        if option.lower() == "back":
            title_screen()
        elif option.lower() == "quit":
            print("Shutting off. Thank you for playing.")
            sys.exit()


def print_location():
    print(room[user.player_location])


# Game Loop
def game_loop():
    os.system('cls')
    while user.end_game is False:
        game_prompt()


def show_items(item_array):
    if user.player_status is True:
        print(f'{bcolors.FAIL}\n\tUser Inventory{bcolors.ENDC}\n')
        if not user.items:
            print('\tThere is nothing in your inventory!')
        else:
            for x in item_array:
                print(f'\t ~ {x}')


def game_prompt():
    os.system('cls')
    print_location()
    show_items(user.items)
    print(f'\n{bcolors.OKGREEN}******************{bcolors.ENDC}')
    print('What do you want to do?\n')
    print('[Quit, Pick Up, Drop, or Walk]')
    print(f'{bcolors.OKGREEN}******************{bcolors.ENDC}')
    action = input('> ')
    acceptable_actions = ['quit', 'pick up', 'drop', 'walk']
    # while action input is NOT in acceptable_actions + lowered, do this..
    while action.lower() not in acceptable_actions:
        print('Unknown command. Try again\n')
        action = input('>')
    if action.lower() == 'quit':
        sys.exit()
    if action.lower() == 'pick up':
        Room.new_game = False
        print('Which item do you wish to pick up?')
        action = input('> ')
        acceptable_item_actions = room[user.player_location].items
        for i in acceptable_item_actions:
            if action.lower() == i.name.lower():
                item = i
                user.add_item(item)
                current_room_items_array = room[user.player_location].items
                index = current_room_items_array.index(i)
                del acceptable_item_actions[index]

    if action.lower() == 'drop':
        Room.new_game = False
        print('Which item do you want to drop?')
        action = input('> ')
        for i in user.items:
            acceptable_item_actions = i.name
            if action.lower() == acceptable_item_actions.lower():
                # if this is true, then we drop the entire item
                user.drop_item(i)
                # adds this dropped item in the current room
                room[user.player_location].items.append(Item(i.name, i.description, i.power))

    if action.lower() == 'walk':
        os.system('cls')
        Room.new_game = False
        print_location()
        print(f'\n{bcolors.OKGREEN}******************{bcolors.ENDC}\n')
        print('\tWhere do you want to go?')
        print('\tPlaces you can go...\n')
        print('\tUse [N,E,S,W] to navigate.')
        print('\tYou can also type in north, east, south, or west')
        print(f'\n{bcolors.OKGREEN}******************{bcolors.ENDC}\n')
        current_room = user.player_location
        curr = ""
        curr_key = ""

        # getting the keys of all possible rooms
        for key in room:
            # checking if key = current room key
            if key.lower() in current_room:
                # getting the current room name
                curr = room[current_room].name
                curr_key = key

            # making sure these exist
        if curr and curr_key:
            # creating an array outside of the for loop
            key_array = []
            for x in room:
                # appending to array
                key_array.append(x)
            if curr_key in key_array:
                # copying key_array and replacing it with altered_array so we don't effect the original
                altered_array = key_array[:]
                # removing the current key from the altered array
                altered_array.remove(curr_key)
                final = []
                if curr_key == 'a1':
                    room_a2 = altered_array[:]
                    room_a2.remove('a4')
                    final = room_a2
                elif curr_key == 'a2':
                    room_a2 = altered_array[:]
                    room_a2.remove('a4')
                    final = room_a2

                elif curr_key == 'a3':
                    final = altered_array

                # ...........................
                if curr_key == 'a1':
                    if room['a2'].name == 'Mario\'s Bedroom':
                        room['a2'].name = f'{bcolors.FAIL}Mario\'s Bedroom{bcolors.ENDC}'
                    if room['a3'].name == 'a hallway':
                        room['a3'].name = f'{bcolors.WARNING}a hallway{bcolors.ENDC}'
                    print(f'\nSeems like you can only go {bcolors.FAIL}north{bcolors.ENDC} or {bcolors.WARNING}east{bcolors.ENDC}.')
                elif curr_key == 'a2':
                    if room['a1'].name == 'Monika\'s Bedroom':
                        room['a1'].name = f'{bcolors.OKBLUE}Monika\'s Bedroom{bcolors.ENDC}'
                    if room['a3'].name == 'a hallway':
                        room['a3'].name = f'{bcolors.WARNING}a hallway{bcolors.ENDC}'
                    print(f'\nSeems like you can only go {bcolors.OKBLUE}south{bcolors.ENDC} or {bcolors.WARNING}east{bcolors.ENDC}.')
                elif curr_key == 'a3':
                    if room['a1'].name == 'Monika\'s Bedroom':
                        room['a1'].name = f'{bcolors.OKBLUE}Monika\'s Bedroom{bcolors.ENDC}'
                    if room['a2'].name == 'Mario\'s Bedroom':
                        room['a2'].name = f'{bcolors.FAIL}Mario\'s Bedroom{bcolors.ENDC}'
                    if room['a4'].name == 'Outside':
                        room['a4'].name = f'{bcolors.WARNING}Outside{bcolors.ENDC}'
                    print(f'\nSeems like you can only go {bcolors.OKBLUE}south{bcolors.ENDC}, {bcolors.WARNING}east{bcolors.ENDC} or {bcolors.FAIL}north{bcolors.ENDC}.')
                # ...........................

                for i in final:
                    value = room[i].name
                    print(f'\n\t{value}')

                # the logic here has to be relative to what info is in player location
                walk_input = input('> ')
                dest = walk_input
                # re assign the color change
                room['a1'].name = f'Monika\'s Bedroom'
                room['a2'].name = f'Mario\'s Bedroom'
                room['a3'].name = f'a hallway'
                room['a4'].name = f'Outside'
                UP = "up", 'north', 'n'
                DOWN = "down", "south", 's'
                LEFT = "left", "west", 'w'
                RIGHT = "right", "east", 'e'
                if curr_key == 'a1':
                    if dest in UP:
                        user.player_location = 'a3'
                    elif dest in RIGHT:
                        user.player_location = 'a2'
                    else:
                        print('You cannot go there!')
                if curr_key == 'a2':
                    if dest in DOWN:
                        user.player_location = 'a1'
                    elif dest in RIGHT:
                        user.player_location = 'a3'
                    else:
                        print('You cannot go there!')
                if curr_key == 'a3':
                    if dest in DOWN:
                        user.player_location = 'a1'
                    elif dest in RIGHT:
                        user.player_location = 'a2'
                    elif dest in UP:
                        user.player_location = 'a4'
                    elif dest in LEFT:
                        print('You cannot go there!')
                os.system('cls')

        # walk_input = input('> ')
        # dest = walk_input
        # # would be like a1, a2, a3, a4, etc
        # current_room = room[user.player_location]


# Setup Game

def setup_game():
    os.system('cls')
    question_one = "Hello, what is your name?\n"
    for character in question_one:
        sleep(0.08)
        sys.stdout.write(character)
        sys.stdout.flush()
    player_name = input('> ')
    os.system('cls')
    user.name = player_name.lower()

    if player_name == 'monika':
        question_two = f'{player_name.capitalize()}! I know you!\n'
        for character in question_two:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_two_addition = f'In this game you can play yourself!\n'
        for character in question_two_addition:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_three = f'The roles to choose from are...\n'
        for character in question_three:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_four = f'Monika, Kai, or Squirrel.\n'
        for character in question_four:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        # valid options for roles
        valid_options = ['monika', 'kai', 'squirrel']
        # player inputs name
        role = input('> ')
        # the Player class player_role gets updated with the inputed value
        user.player_role = role
        # taking role that is converted to lowercase and checking if its in valid_options
        if role.lower() in valid_options:
            if role.lower() == 'monika':
                describe = 'The Artist'
            elif role.lower() == 'kai':
                describe = 'The Squirrel Hunter'
            elif role.lower() == 'squirrel':
                describe = 'The Ultra Fast Crackhead'
            os.system('cls')
            print(f' You are {role.capitalize()}, {describe}!\n')
            os.system('cls')
            startup = '###'
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            for character in startup:
                sleep(0.06)
                sys.stdout.write(character)
                sys.stdout.flush()

            game_loop()

        else:
            while role.lower() not in valid_options:
                os.system('cls')
                print('Invalid command, try again.\n')
                print('Options are... \n')
                print('Monika, Kai, or Squirrel.\n')
                role = input('> ')
                if role.lower() in valid_options:
                    user.player_role = role
                    if role == 'monika':
                        describe = 'The Artist'
                    elif role == 'kai':
                        describe = 'The Squirrel Hunter'
                    elif role == 'squirrel':
                        describe = 'The Ultra Fast Crackhead'
                    os.system('cls')
                    print(f' You are {role.capitalize()}, {describe}!')

    if player_name != 'monika':
        question_two = f'Hello {player_name.capitalize()}!\n'
        for character in question_two:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_three = f'The roles to choose from are...\n'
        for character in question_three:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_four = f'Monika, Kai, or Squirrel.\n'
        for character in question_four:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        # valid options for roles
        valid_options = ['monika', 'kai', 'squirrel']
        # player inputs name
        role = input('> ')
        # the Player class player_role gets updated with the inputed value
        user.player_role = role
        # taking role that is converted to lowercase and checking if its in valid_options
        if role.lower() in valid_options:
            if role.lower() == 'monika':
                describe = 'The Artist'
            elif role.lower() == 'kai':
                describe = 'The Squirrel Hunter'
            elif role.lower() == 'squirrel':
                describe = 'The Ultra Fast Crackhead'
            os.system('cls')
            print(f' You are {role.capitalize()}, {describe}!\n')
            os.system('cls')
            startup = '###'
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            print(f'{bcolors.BOLD}#{bcolors.ENDC}' + (f'{bcolors.BOLD}#{bcolors.ENDC}' * (3 + len(startup))))
            for character in startup:
                sleep(0.06)
                sys.stdout.write(character)
                sys.stdout.flush()

            game_loop()

        else:
            while role.lower() not in valid_options:
                os.system('cls')
                print('Invalid command, try again.\n')
                print('Options are... \n')
                print('Monika, Kai, or Squirrel.\n')
                role = input('> ')
                if role.lower() in valid_options:
                    user.player_role = role
                    if role == 'monika':
                        describe = 'The Artist'
                    elif role == 'kai':
                        describe = 'The Squirrel Hunter'
                    elif role == 'squirrel':
                        describe = 'The Ultra Fast Crackhead'
                    os.system('cls')
                    print(f' You are {role.capitalize()}, {describe}!')

    else:
        question_two = f'{player_name}, what role would you like to play?\n'
        for character in question_two:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_three = f'Options include...\n'
        for character in question_three:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_four = f'Monika, Kai, or Squirrel.\n'
        for character in question_four:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        role = input('> ')
        valid_options = ['monika', 'kai', 'squirrel']
        if role.lower() in valid_options:
            user.player_role = role
            if role == 'monika':
                describe = 'The Artist'
            elif role == 'kai':
                describe = 'The Squirrel Hunter'
            elif role == 'squirrel':
                describe = 'The Ultra Fast Crackhead'
            os.system('cls')
            print(f' You are {role.capitalize()}, {describe}!')

        else:
            while role.lower() not in valid_options:
                os.system('cls')
                print('Invalid command, try again.\n')
                print('Options are... \n')
                print('Monika, Kai, or Squirrel.\n')
                role = input('> ')
                if role.lower() in valid_options:
                    user.player_role = role.lower()
                    if role == 'monika':
                        describe = 'The Artist'
                    elif role == 'kai':
                        describe = 'The Squirrel Hunter'
                    elif role == 'squirrel':
                        describe = 'The Ultra Fast Crackhead'
                    os.system('cls')
                    print(f' You are {role.capitalize()}, {describe}!')


# Calling the game
title_screen()
