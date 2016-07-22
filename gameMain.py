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

c1_cur_place = chap_map[0][0]
c1_last_place = c1_cur_place
c1_inf_evs = c1.chap_info_evs
c1_info_evs = {}

chapters = {}
chapters['exit'] = 'exit'
chapters[1] = 'savage_palace'
chapters[2] = 'zombie_apocalypse'
chapters[3] = 'grey_and_nevaeh'
chapters[4] = 'spirit_animals'



# Action functions
def go_l(map_inf):
    for inf_node in map_inf:
        if inf_node == 'dirs':
            for di in map_inf[inf_node].keys():
                if di == 'go left':
                    return map_inf[inf_node][di]
            print
            print
            print '     Cannot go left here.'
            sleep(1)
            return '' 
                
def go_r(map_inf):
    for inf_node in map_inf:
        if inf_node == 'dirs':
            for di in map_inf[inf_node].keys():
                if di == 'go right':
                    return map_inf[inf_node][di]
            print
            print
            print '     Cannot go right here.'
            sleep(1)
            return ''
                
def go_f(map_inf):
    for inf_node in map_inf:
        if inf_node == 'dirs':
            for di in map_inf[inf_node].keys():
                if di == 'go forward':
                    return map_inf[inf_node][di]
            print
            print
            print '     Cannot go forward here.'
            sleep(1)
            return ''
                
def go_b(map_inf):
    for inf_node in map_inf:
        if inf_node == 'dirs':
            for di in map_inf[inf_node].keys():
                if di == 'go back':
                    return map_inf[inf_node][di]
            print
            print
            print '     Cannot go back here.'
            sleep(1)
            return ''
        
def talk(map_inf):
    start_with_char = False
    char_dial = {'who':'',
                 'dial':[]}
    else_dial = {'who':'',
                 'dial':[]}
    dial_total = []
    char_dial['who'] = c1.player['name']
    for inf_node in map_inf:
        if inf_node == 'dial':
            for di in map_inf[inf_node].keys():
                if di == char_dial['who']:
                    char_dial['dial'].append(map_inf[inf_node][di])
                else:
                    else_dial['who'] = di
                    else_dial['dial'].append(map_inf[inf_node][di])
                dial_total.append(map_inf[inf_node][di])
    if char_dial['dial'][0][0] == '`':
        start_with_char = True
    else:
        pass
    if start_with_char:
        system('cls')
        system('title ' + c1.player['name'] + ' : ' + 'Dialogue - ' + else_dial['who'])
        print
        print
        print
        for line in len(dial_total):
            



# Function to check actions
def check_action(u_act):
    global c1_cur_place
    global c1_last_place
    global c1_info_evs
    c1_last_place = c1_cur_place
    if u_act == 'go left':
        c1_cur_place = go_l(c1_info_evs)
        if c1_cur_place == '':
            c1_cur_place = c1_last_place
    elif u_act =='go right':
        c1_cur_place = go_r(c1_info_evs)
        if c1_cur_place == '':
            c1_cur_place = c1_last_place
    elif u_act == 'go forward':
        c1_cur_place = go_f(c1_info_evs)
        if c1_cur_place == '':
            c1_cur_place = c1_last_place
    elif u_act == 'go back':
        c1_cur_place = go_b(c1_info_evs)
        if c1_cur_place == '':
            c1_cur_place = c1_last_place
    elif u_act == 'go sec':
        print
        print
        usr_room_ch = str(raw_input('     Which room: '))
        for r in chap_map[0]:
            if usr_room_ch == r:
                c1_cur_place = usr_room_ch
    elif u_act == 'exit':
        sys.exit(0)
    else:
        print
        print
        print '     Invalid!'
        sleep(1)
    c1_info_evs = c1_inf_evs[c1_cur_place]
    return None



# Function to simulate loading
def loading():
    system('title Loading...')
    system('cls')
    print
    print
    print
    print '     Loading',
    sleep(.2)
    print '.',
    sleep(.2)
    print '.',
    sleep(.2)
    print '.',
    sleep(.2)
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
    global c1_cur_place
    global c1_last_place
    global c1_info_evs
    if user == 'evs':
        c1_cur_place = chap_map[0][0]
        c1_info_evs = c1_inf_evs[c1_cur_place]
        c1.player['name'] = 'Evs'
    else:
        c1_cur_place = chap_map[0][4]
        c1_info_evs = c1_inf_evs[c1_cur_place]
        c1.player['name'] = 'Adi'
    c1_last_place = c1_cur_place
    while True:
        system('title ' + c1.player['name'] + ' : ' + c1_cur_place)
        system('cls')
        print
        print
        print
        print c1_info['desc']
        print
        print
        usr_action = str(raw_input('     Action: ')).lower()
        check_action(usr_action)
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
