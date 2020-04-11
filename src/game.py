import sys
import os
import time
from player import Player


# Title Screen

def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        print("Shutting off. Thank you for playing.")
        os.system('clear')
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
            os.system('clear')
            sys.exit()


def title_screen():
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
    os.system('clear')
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

# Setup Game

def setup_game():
    os.system('clear')

    question_one = " Hello, what is your name? "
    for character in question_one:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
        player_name = input('> ')
        Player.name = player_name


# Calling the game
title_screen()
