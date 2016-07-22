from time import sleep
from os import system
from msvcrt import getch
import sys

# Assets module for gameMain.py
# Storing variables like 'title_screen' here and so forth, so on :P
# Oh and also encaspulates some functions needed for character selection, etc...
title_screen = """     --------------------------------------------------------
                             
                             Roleplay
                             
     --------------------------------------------------------
     
     
     > Chapter One   -   Savage Palace
       Chapter Two   -   Zombie Apocolypse
       Chapter Three -   Grey and Nevaeh
       Chapter Four  -   Spirit Animals"""

# Function used by 'character_choose' to optimize the readability
def choose_name(str1, str2):
    while True:
        system('cls')
        system('title Choose Your Name')
        print
        print
        print
        print '     Do you want to be \'' + str1 + '\' or \'' + str2 + '\':',
        usr_wants_to_be = str(raw_input()).lower()
        str1 = str1.lower()
        str2 = str2.lower()
        if usr_wants_to_be == str1:
            return str1
        elif usr_wants_to_be == str2:
            return str2
        else:
            print
            print
            print '     Invalid!'
            sleep(1)
        

# Function for choosing a character
def chr_choose(chap):
    user_is = ''
    if chap == 'savage_palace':
        user_is = choose_name('Evs','Adi')
    elif chap == 'zombie_apocalypse':
        user_is = choose_name('Evs','Adi')
    elif chap == 'grey_and_nevaeh':
        user_is = choose_name('Grey','Nevaeh')
    elif chap == 'spirit_animals':
        user_is = choose_name('Evs','Adi')
    else:
        user_is = 'user'
    return user_is