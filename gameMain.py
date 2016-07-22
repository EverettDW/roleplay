# Imports
from time import sleep
import sys
from os import system
from msvcrt import getch
import c1
import assets



# Variables
is_dark = True
usr_chap = 0

actions = ['lights',\
'exit',\
'go left',\
'go right',\
'go back',\
'go forward',\
'pick up',\
'drop',\
'eat',\
'drink',\
]

chap_map = [['SP - Entrance',\
'SP - Entry Hallway',\
'SP - Peanut Butter Fountain',\
'SP - Park',\
'SP - Park 1',\
'SP - Park 2',\
'SP - Park 3',\
'SP - Park 4',\
'SP - Park 5',\
'SP - Evs\' Room',\
'SP - Adi\'s Room'],\
['',''],['',''],['','']]

chapters = {}
chapters['exit'] = 'exit'
chapters[1] = 'savage_palace'
chapters[2] = 'zombie_apocalypse'
chapters[3] = 'grey_and_nevaeh'
chapters[4] = 'spirit_animals'



# Function to simulate loading
def loading():
    system('title Loading...')
    system('cls')
    print
    print
    print
    print '     Loading',
    sleep(.3)
    print '.',
    sleep(.3)
    print '.',
    sleep(.3)
    print '.',
    sleep(.3)
    print ' Done :)'
    sleep(.5)
    return None



# The actual function that will go in the loop to use the title screen
# Right key: 224-77 | Left key: 224-75 | Up key: 224-72 | Down key: 224-80
def nav_title_screen():
    print_title_screen(0)
    usr_select_title = 0
    enter_not_pressed = True
    while enter_not_pressed:
        print_title_screen(usr_select_title)
        key = ord(getch())
        if key == 224:
            key = ord(getch())
            if key == 72:
                if usr_select_title == 0:
                    system('cls')
                    print_title_screen(usr_select_title)
                else:
                    usr_select_title -= 1
                    system('cls')
                    print_title_screen(usr_select_title)
            elif key == 80:
                if usr_select_title == 3:
                    system('cls')
                    print_title_screen(usr_select_title)
                else:
                    usr_select_title += 1
                    system('cls')
                    print_title_screen(usr_select_title)
        elif key == 13:
            enter_not_pressed = False
            loading()
            if usr_select_title == 0:
                usr_chosen_name = assets.chr_choose(chapters[1])
                chap_one(usr_chosen_name)
            elif usr_select_title == 1:
                usr_chosen_name = assets.chr_choose(chapters[2])
                chap_two(usr_chosen_name)
            elif usr_select_title == 2:
                usr_chosen_name = assets.chr_choose(chapters[3])
                chap_three(usr_chosen_name)
            elif usr_select_title == 3:
                usr_chosen_name = assets.chr_choose(chapters[4])
                chap_four(usr_chosen_name)
            
# Display title screen function
def print_title_screen(sel):
    system('cls')
    system('title Roleplay')
    print
    print
    print
    edit_title = assets.title_screen
    if sel == 0:
        print assets.title_screen
    elif sel == 1:
        edit_title = edit_title.replace('>', ' ')
        edit_title = edit_title[:278] + '>' + edit_title[279:]
        print edit_title
    elif sel == 2:
        edit_title = edit_title.replace('>', ' ')
        edit_title = edit_title[:321] + '>' + edit_title[322:]
        print edit_title
    elif sel == 3:
        edit_title = edit_title.replace('>', ' ')
        edit_title = edit_title[:362] + '>' + edit_title[363:]
        print edit_title
    print
    print '     ',
    return None



# Action Functions
def lights():
    if is_dark == True:
        is_dark = False
    else:
        is_dark = True
    return None

def help():
    system('cls')
    print
    print
    print

    sleep(.5)
    return None



# Chapter One
def chap_one(user):
    system('cls')
    if user == 'evs':
        cur_place = chap_map[0][0]
        c1.player['name'] = 'Evs'
    else:
        cur_place = chap_map[0][4]
        c1.player['name'] = 'Adi'
    last_place = cur_place
    while True:
        chap_inf = c1.chap_info[cur_place]
        system('title ' + c1.player['name'] + ' : ' + cur_place)
        system('cls')
        print
        print
        print
        print chap_inf['desc']
        print
        print
        usr_action = str(raw_input('     Action: ')).lower()
        if usr_action == 'exit':
            return None
        elif usr_action == 'go left':
            pass
    return None



# Chapter Twp
def chap_two(user):
    pass
    return None



# Chapter Three
def chap_three(user):
    pass
    return None



# Chapter Four
def chap_four(user):
    pass
    return None



# Main Start
def main():
    while 1 == 1:
        nav_title_screen()
        break
    return None



# If program is run directly start game
if __name__=='__main__':
    main()
