# Imports
from time import sleep
import sys
from os import system
from msvcrt import getch



# Variables
user_is_evs = False
user_is_grey = False
is_dark = True
usr_chap = 0

player = {'name':'',\
'inv_size':5,\
'inv':[],\
}

actions = ['lights',\
'exit',\
'go left',\
'go right',\
'go back',\
'go forward',\
'pick up',\
'drop']

chap_map = [['SP - Entrance',\
'SP - Entry Hallway',\
'SP - Cinema Room',\
'SP - Peanut Butter Fountain',\
'SP - Park',\
'SP - Evs\' Room',\
'SP - Adi\'s Room'],\
['',''],['',''],['','']]

chap_dial = {'SP - Entrance':"""     You walk through the door to the Savage Palace
     entrance.  The lights are off and you can see nothing
     but a faint glow straight ahead of you leading into
     a hallway.  There could be other things in the room
     but the lights are off.""",\
'SP - Entry Hallway':"""     PUT DESC HERE     """,\
}

chap_items = {'SP - Entrance':[],\
'SP - Entry Hallway':[],\
}

chap_dirs = {'SP - Entrance':['go left','go forward'],
'SP - Entry Hallway':[],\
}

chapters = {}
chapters['exit'] = 'exit'
chapters[1] = 'savage_palace'
chapters[2] = 'zombie_apocalypse'
chapters[3] = 'grey_and_nevaeh'
chapters[4] = 'spirit_animals'



# Action Functions
def lights():
    if is_dark == True:
        is_dark = False
    else:
        is_dark = True
    return None

def help():
    print
    print
    print '     YAY HELP WORKS!'
    sleep(.5)
    return None



# Chapter One
def chap_one(user_is):
    system('cls')
    usr_replay = True
    cur_place = chap_map[0][0]
    last_place = cur_place
    while usr_replay == True:
        system('title ' + cur_place)
        system('cls')
        print
        print
        print
        if is_dark == True:
            # If the room is dark
            for key in chap_dial.keys():
                if cur_place == key:
                    print chap_dial[key]
            print
            print
            usr_action = str(raw_input('     Action: ')).lower()

        else:
            pass
    return None



# Chapter Twp
def chap_two(user_is_evs):
    pass
    return None



# Chapter Three
def chap_three(user_is_grey):
    pass
    return None



# Chapter Four
def chap_four(user_is_evs):
    pass
    return None



# Main Start
def main():
    while 1 == 1:
        system('cls')
        system('title Roleplay')
        prop_char = False
        who_user_is = 'user'
        print
        print
        print
        print '     ------------------------------------------------     '
        print
        print '                         Roleplay                         '
        print
        print '     ------------------------------------------------     '
        print
        print
        print '     1 = Chapter One    -  Savage Palace     '
        print '     2 = Chapter Two    -  Zombie Apocalypse '
        print '     3 = Chapter Three  -  Grey And Nevaeh   '
        print '     4 = Chapter Four   -  Spirit Animals    '
        # Add extra chapters here - Make sure to add to the chapters dict
        print
        print

        usr_chap = raw_input('     Which chapter do you wish to visit: ')

        try:
            usr_chap = int(usr_chap)
        except:
            usr_chap = str(usr_chap).lower()

        for key in chapters.keys():
            if usr_chap == key:
                prop_char = True

        if prop_char == True:
            if usr_chap == 1:
                system('cls')
                print
                print
                print
                if who_user_is == 'user':
                    who_user_want = str(raw_input('     Do you want to be \'Evs\' or \'Adi\': '))
                    who_user_want = who_user_want.lower()
                    if who_user_want == 'evs':
                        user_is_evs = True
                        chap_one(user_is_evs)
                    elif who_user_want == 'adi':
                        user_is_evs = False
                        chap_one(user_is_evs)
                    else:
                        print
                        print '     Invalid Entry'
                        sleep(.5)
            elif usr_chap == 2:
                pass
            elif usr_chap == 3:
                pass
            elif usr_chap == 4:
                pass
            elif usr_chap == 'exit':
                print
                print
                exit()
        else:
            print
            print
            print '     Invalid Entry'
            sleep(.5)
    return None



# If program is run directly start game
if __name__=='__main__':
    main()
