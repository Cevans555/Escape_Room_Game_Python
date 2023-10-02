#text based game

import cmd
import textwrap
import sys
import os 
import time 
import random

screen_width = 100

### player setup ###
class player:
    def __init__(self):
        self.name = ''
        self.items = []
        self.location = 'w1'
        self.game_over = False

my_player = player()

### title screen ###
def title_screen_selections():
    option  = input('> ')
    if option.lower().strip() == ('play'):
        setup_game() 
    elif option.lower().strip()  == ('help'):
        help_menu()
    elif option.lower().strip()  == ('quit'):
        sys.exit()
    while option.lower().strip()  not in ['play', 'help', 'quit']:
        print('Please enter valid command.')
        option = input('> ')
        if option.lower().strip()  == ('play'):
            setup_game() 
        elif option.lower().strip()  == ('help'):
            help_menu()
        elif option.lower().strip()  == ('quit'):
            sys.exit()

def title_screen():
    os.system('cls')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print(' Copyright 2021 Cevans Corp ')
    title_screen_selections()

def help_menu():
    print('Type your commands to do them')
    print('Use "move", "go", and "look" + direction to look/move around room')
    print('Use above  + "up", "down", "left", "right" to look/move around room')
    print('Use "examine", "inspect", "interact", and "search" to inspect things')
    print('Good luck and have fun!')
    title_screen_selections()

def help_menu_1():
    print('Type your commands to do them')
    print('Use "move", "go", and "look" + direction to look/move around room')
    print('Use above  + "up", "down", "left", "right" to look/move around room')
    print('Use "examine", "inspect", "interact", and "search" to inspect things')
    print('Good luck and have fun!')
    
def items_menu():
    print(my_player.items)

def walls():
    if my_player.location == 'w1':    
        print("############################################")
        print("#                         __________       #")
        print("#      __________         |        |       #")
        print("#     |          |        |        |       #")
        print("#     |          |        |        |       #")
        print("#     |__________|        |      * |  |*|  #")
        print("#                         |        |       #")
        print("# _____________________   |        |       #")
        print("# | |   | |   | |   | |   |        |       #")
        print("############################################")
        print("\n The wall has a 'tv' mounted to it, some 'shoe cubbies', a 'light switch', and a 'door'.")

    elif my_player.location == 'w2':
        print("############################################")
        print("#                                          #")
        print("#   _________                              #")
        print("#  |    |    |                          _  #")
        print("#  |----|----|                         | | #")
        print("#  |____|____|                    ____ | | #")
        print("#                 _______________|    || | #")
        print("#                |_____________________| | #")
        print("#                ||         ||         | | #")
        print("############################################")
        print("\n The wall has a 'window' and a 'bed'.")

    elif my_player.location == 'w3':
        print("############################################")
        print("#                            _____________ #")
        print("#    ___    ________         |  |  |  |  | #")
        print("#   |   |  |        |        |  |  |  |  | #")
        print("#   |   |  |________|        |  |  |  |  | #")
        print("#  _|___|_____/__\_____      |  | *|* |  | #")
        print("#  |  ______________  | __   |  |  |  |  | #")
        print("#  | |              | ||  |  |  |  |  |  | #")
        print("#  | |              | ||  |  |  |  |  |  | #")
        print("############################################")
        print("\n The wall has a 'computer' on a desk, a 'trash' can, and a 'closet'.")

    elif my_player.location == 'w4':
        print("############################################")
        print("#                ---------   _____________ #")
        print("#                | *   * |   |-----------| #")
        print("#                | \___/ |   |     *     | #")
        print("#    ________    ---------   |-----------| #")
        print("# __|________|____________   |     *     | #")
        print("#  |  ________________  |    |-----------| #")
        print("#  | |                | |    |     *     | #")
        print("#  | |                | |    |-----------| #")
        print("############################################")
        print("\n The wall has a 'painting' hung up, a table with a 'record player' on it, and a tall 'dresser'.")

    elif my_player.location == 'c1':
        print("############################################")
        print("#                                          #")
        print("#                                          #")
        print("#                  \ | /                   #")
        print("#                 --(O)--                  #")
        print("#                  / | \                   #")
        print("#                                          #")
        print("#                                          #")
        print("#                                          #")
        print("############################################")
        print("\n The ceiling has doesn't have anything but a 'light'.")

    elif my_player.location == 'g1':
        print("############################################")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~  \  ~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~   ) ~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~  /  ~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("############################################")
        print("\n The ground is carpeted, but there's a weird 'bump' in one section.")

def channels():
    print("############################################")
    print("# Channel 235 - News                       #")
    print("# Channel 456 - Missing Persons            #")
    print("# Channel 5786 - Space the Infinite        #")
    print("# Channel 9379 - Codex Gameshow            #")
    print("# Channel 1234 - ABCs                      #")
    print("############################################")

def channel_235():
    print("############################################")
    print("#                                          #")
    print("#                   0                      #")
    print("#              0    \/                     #")
    print("#             \/     |         0           #")
    print("#             |   __/\___     \/           #")
    print("#         ___/\__|       |    |            #")
    print("#        |       |       |___/\__          #")
    print("#        |       |       |       |         #")
    print("############################################")

def channel_456():
    print( "############################################")
    print(f"#  A man by the name of {my_player.name}            #")
    print( "#  has been missing for over a week no one #")
    print( "#  has seen or heard from him.             #")
    print( "############################################")

def channel_5786():
    print("############################################")
    print("#  *              *                  *     #")
    print("#        *                   *             #")
    print("#                /\                        #")
    print("#         *     /  \                       #")
    print("#              /____\             *        #")
    print("# *           |      |                     #")
    print("#             |      |        *        *   #")
    print("#      *      |      |                     #")
    print("############################################")

def channel_9379():
    print("############################################")
    print("#  Come on down and play the game!         #")
    print("#  The prize this week is a mini safe!     #")
    print("#  Perfect for under your bed!             #")
    print("############################################")
 
def channel_1234():
    print("############################################")
    print("#       ABCDEFGHIJKLMNOPQRSTUVWXYZ         #")
    print("############################################")


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


zonemap = {
    'w1': {
        UP: 'c1',
        DOWN: 'g1',
        LEFT: 'w4',
        RIGHT: 'w2'
    },
    'w2': {
        UP: 'c1',
        DOWN: 'g1',
        LEFT: 'w1',
        RIGHT: 'w3'
    },
    'w3': {
        UP: 'c1',
        DOWN: 'g1',
        LEFT: 'w2',
        RIGHT: 'w4'
    },
    'w4': {
        UP: 'c1',
        DOWN: 'g1',
        LEFT: 'w3',
        RIGHT: 'w1'
    },
    'c1': {
        UP: 'c1',
        DOWN: 'g1',
        LEFT: 'w1',
        RIGHT: 'w1'
    },
    'g1': {
        UP: 'c1',
        DOWN: 'g1',
        LEFT: 'w1',
        RIGHT: 'w1'
    }
}

### Game Interactivity ###

def prompt():
    print('\n' + '================================')
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'look', 'turn',
                          'quit', 'help', 'items',
                          'examine', 'inspect', 'interact', 'search']
    while action.lower().strip()  not in acceptable_actions:
        print('Unknown action, try again. \n')
        action = input('> ')
    if action.lower().strip()  == 'quit':
        sys.exit()
    elif action.lower().strip()  in ['move', 'go', 'look', 'turn']:
        player_move(action.lower())
    elif action.lower().strip()  in ['examine', 'inspect', 'interact', 'search']:
        player_examine(action.lower())
    elif action.lower().strip()  == 'items':
        items_menu()
    elif action.lower().strip()  == 'help':
        help_menu_1()
    
def player_move(my_action):
    ask = "Where would you like to look?\n"
    dest = input(ask)
    if dest in ['up']:
        destination = zonemap[my_player.location][UP]
        movement_handler(destination)
        walls()
    elif dest in ['left']:
        destination = zonemap[my_player.location][LEFT]
        movement_handler(destination)
        walls()
    elif dest in ['right']:
        destination = zonemap[my_player.location][RIGHT]
        movement_handler(destination)
        walls()
    elif dest in ['down']:
        destination = zonemap[my_player.location][DOWN]
        movement_handler(destination)
        walls()

def movement_handler(destination):
    my_player.location = destination

def player_examine(action):
    print('\n' + '================================')
    print("What would you like to search?")
    thing = input('> ')
    w1_acceptable_actions = ['door','light switch', 'tv', 'shoe cubbies']
    w2_acceptable_actions = ['window', 'bed']
    w3_acceptable_actions = ['computer', 'trash', 'closet']
    w4_acceptable_actions = ['painting', 'record player', 'dresser']
    c1_acceptable_actions = ['light']
    g1_acceptable_actions = ['bump']
    
    if my_player.location == 'w1':
        while thing.lower().strip()  not in w1_acceptable_actions:
            print('Unknown action, try again. \n')
            thing = input('> ')
        if thing.lower().strip()  == 'quit':
            sys.exit()
        elif thing.lower().strip()  == 'light switch':
             print('Light switch is on!')
        elif thing.lower().strip()  == 'tv':
            if 'remote' in my_player.items:
                ask_tv = 'Do you want to turn the TV on? (Yes/No): '
                tv = input(ask_tv)
                if tv.lower().strip() == 'yes':
                    print('The TV is now on, but theres nothing but static.')
                    ask_channel = 'Do you want to change the channel? (Yes/No): '
                    channel = input(ask_channel)
                    if channel.lower().strip() == 'yes':
                        ask_channel_num = 'What channel do you want?: '
                        channel_num = input(ask_channel_num)
                        if channel_num == '235':
                            channel_235()
                        elif channel_num == '456':
                            channel_456()
                        elif channel_num == '5786':
                            channel_5786()
                        elif channel_num == '9379':
                            channel_9379()
                        elif channel_num == '1234':
                            channel_1234()
                else:
                    print('The TV is off.')
            else:
                print('The TV is off.')
        elif thing.lower().strip()  == 'shoe cubbies':
            if 'flashlight' not in my_player.items:
                my_player.items.append('flashlight')
                print('You found a flashlight!')
            else:
                print('There is nothing else here to find')
        elif thing.lower().strip()  == 'door':
            print('The door is locked.')
            if 'key' in my_player.items:
                ask_door = 'Do you want to use the key on the door? (Yes/No): '
                door = input(ask_door)
                if door.lower().strip() == 'yes':
                    end_game = 'The door is now open. Would you like to leave? (Yes/No): '
                    end = input(end_game)
                    print('Congrats you beat my game!')
                    my_player.game_over = True
    
    elif my_player.location == 'w2':
        while thing.lower().strip()  not in w2_acceptable_actions:
            print('Unknown action, try again. \n')
            thing = input('> ')
        if thing.lower().strip()  == 'quit':
            sys.exit()
        elif thing.lower().strip()  == 'window':
            if 'normal light bulb' in my_player.items:
                print("There's a message on the window. It says \"Play it in Reverse\".")
            else:
                print("It's too dark to see out there.")
        elif thing.lower().strip()  == 'bed':
            if 'flashlight' in my_player.items:
                if 'knife' not in my_player.items:
                    my_player.items.append('remote')
                    print('You found a remote!\n')
                    print('There is also a mini safe under here.')
                    ask_safe = 'Would you like to try and open it? (Yes/No): '
                    safe = input(ask_safe)
                    if safe.lower() == 'yes':
                        ask_safe_code = "Please enter the safe's 4 digit code: "
                        safe_code = input(ask_safe_code)
                        if safe_code == '9379':
                            my_player.items.append('knife')
                            print('You found a knife!\n')
                        else:
                            print('Incorrect code.')
            elif'knife' in my_player.items:
                print('There is nothing else here to find')
            else:
                print('It\'s too dark to see under the bed.')

    elif my_player.location == 'w3':
        while thing.lower().strip()  not in w3_acceptable_actions:
            print('Unknown action, try again. \n')
            thing = input('> ')
        if thing.lower().strip()  == 'quit':
            sys.exit()
        elif thing.lower().strip()  == 'computer':
            ask_password = 'Please enter the password: '
            password = input(ask_password)
            if password == 'Ranger Danger':
                channels()
            else:
                print("Incorrect password please try again.")
        elif thing.lower().strip()  == 'trash':
            if 'UV light bulb' not in my_player.items:
                my_player.items.append('UV light bulb')
                print('You found a UV light bulb!')
            else:
                print('There is nothing else here to find')
        elif thing.lower().strip()  == 'closet':
            if 'step ladder' not in my_player.items:
                my_player.items.append('step ladder')
                print('You found a step ladder!')
            else:
                print('There is nothing else here to find')


    elif my_player.location == 'w4':
        while thing.lower().strip()  not in w4_acceptable_actions:
            print('Unknown action, try again. \n')
            thing = input('> ')
        if thing.lower().strip()  == 'quit':
            sys.exit()
        elif thing.lower().strip()  == 'painting':
            if 'normal light bulb' in my_player.items:
                if 'record' not in my_player.items:
                    print("There's a message on the painting. It says \"Look behind me\".")
                    ask_behind = "Would you like to look behind the painting? (Yes/No): "
                    behind = input(ask_behind)
                    if behind.lower().strip()  == 'yes':
                        my_player.items.append('record')
                        print('You found a record!')
                else:
                    print('There is nothing else here to find')
            else:
                print("It's just a regualar painting.")
        elif thing.lower().strip()  == 'record player':
            if 'record' in my_player.items:
                ask_record = "Would you like to play the record in forward or reverse: "
                record = input(ask_record)
                if record.lower().strip()  == 'forward':
                    print("regnaD regnaR")
                elif record.lower().strip()  == 'reverse':
                    print("Ranger Danger")
        elif thing.lower().strip()  == 'dresser':
            if 'gloves' not in my_player.items:
                my_player.items.append('gloves')
                print('You found gloves!')
            else:
                print('There is nothing else here to find')


    
    elif my_player.location == 'c1':
        while thing.lower().strip()  not in c1_acceptable_actions:
            print('Unknown action, try again. \n')
            thing = input('> ')
        if thing.lower().strip()  == 'quit':
            sys.exit()
        elif thing.lower().strip()  == 'light':
            if 'gloves' in my_player.items and 'UV light bulb' in my_player.items and 'step ladder' in my_player.items:
                ask_light = "Would you like to remove the normal light bulb and replace it with the UV light bulb (Yes/No): "
                light = input(ask_light)
                if light.lower().strip()  == 'yes':
                    print('You have swapped the light bulbs.')
                    my_player.items.append('normal light bulb')
                    print('You have obtained a normal light bulb!')
                else:
                    print('The normal light bulb remains.')
            elif 'step ladder' not in my_player.items:
                print('The light is just out of reach.')
            elif 'gloves' not in my_player.items:
                print('The light bulb is too hot to handle.')
            elif 'UV light bulb' not in my_player.items:
                print('You don\'t have any lightbulbs to switch.')
                
    
    elif my_player.location == 'g1':
        while thing.lower().strip()  not in g1_acceptable_actions:
            print('Unknown action, try again. \n')
            thing = input('> ')
        if thing.lower().strip()  == 'quit':
            sys.exit()
        elif thing.lower().strip()  == 'bump':
            if 'knife' in my_player.items:
                ask_knife = 'Would you like to cut the carpet? (Yes/No): '
                knife = input(ask_knife)
                if knife.lower().strip()  == 'yes':
                    my_player.items.append('key')
                    print('You found a key!')
            else:
                print('There is nothing else here to find')
            


### Game Functionality ###

def main_game_loop():
    while my_player.game_over is False:
        prompt()
    # here handle is puzzles have been solved, boss defeated, explored everthing, etc. #

def setup_game():
    os.system('cls')
    # Name Collecting #
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    my_player.name = player_name

    

    # Introduction #
    question3 = 'Welcome, ' + player_name + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "You wake up in a pitch black room with no memory of how you got there.\n"
    speech2 = "You feel the wall in front of you and find a light switch.\n"
    speech3 = "You turn the light switch on.\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    walls()

    main_game_loop()




title_screen()