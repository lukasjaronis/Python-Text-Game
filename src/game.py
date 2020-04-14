import sys
import os
from time import sleep
from items import Item
from player import Player
from room import room


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


def player_status():
    if user.player_status is True:
        print('\nUser Inventory\n')
        print(user.items)
    else:
        print('You have nothing in your inventory!')


def item_parser(i):
    item = Item(i.name, i.description, i.power)
    return item


def game_prompt():
    # os.system('cls')
    print_location()
    player_status()
    print('\n#######################\n')
    print('What do you want to do?\n')
    print('[Quit, Pick Up, Drop, or Walk]\n')
    action = input('> ')
    acceptable_actions = ['quit', 'pick up', 'drop', 'walk']
    # while action input is NOT in acceptable_actions + lowered, do this..
    while action.lower() not in acceptable_actions:
        print('Unknown command. Try again\n')
        action = input('>')
    if action.lower() == 'quit':
        sys.exit()
    if action.lower() == 'pick up':
        print('Which item do you wish to pick up?')
        action = input('> ')
        acceptable_item_actions = room[user.player_location].items
        for i in acceptable_item_actions:
            if action.lower() == i.name.lower():
                item = i.name.lower()
                user.add_item(item)
                current_room_items_array = room[user.player_location].items
                index = current_room_items_array.index(i)
                del acceptable_item_actions[index]


        # for i in acceptable_item_actions:
        #     if action.lower() == i.name.lower():
        #         item = i.name.lower()
        #         user.add_item(item)






            #
            # for x in range(0, len(acceptable_item_actions) - 1):
            #     print(x)


                # print(acceptable_item_actions.index(i))
                # item_parse = item_parser(i)
                #
                #
                #
                # if (i.name, i.description, i.power) == (item_parse.name, item_parse.description, item_parse.power):
                #     del room[user.player_location].items[0]





                # # an array of items
                # for x in room[user.player_location].items:
                #     # item_parse is a function that takes in x and returns x.name, x.description, and x.power, then returns itself.
                #     item_checker = item_parser(x)
                #     print(type(item_checker))
                #     print(type(x))
                #     print(x == item_checker)
                #     if x in item_checker:
                #         print(x)
                #         print('i got here?')


# Setup Game

def setup_game():
    os.system('cls')
    question_one = "Hello, what is your name?\n"
    for character in question_one:
        sleep(0.08)
        sys.stdout.write(character)
        sys.stdout.flush()
    player_name = input('> ')
    user.name = player_name.lower()
    if player_name == 'monika':
        question_two = f'{player_name.capitalize()}... is that you? I knew you would play this game :)\n'
        for character in question_two:
            sleep(0.06)
            sys.stdout.write(character)
            sys.stdout.flush()
        question_two_addition = f'You can even play yourself!\n'
        for character in question_two_addition:
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
