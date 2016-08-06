# Filename: roleplay.py
# -== IMPORTS ==-
import time               # Import a function to wait between commands
import random             # Import a function to get a random number
from msvcrt import getch  # Import a function to get a single char (' ') pressed by the user
import sys                # Import sys package.  No particular reason besides sys.exit(0)
import screen             # Import module to control screen
import menus              # Import module to grab menus
import items              # Import module to grab items
import rooms              # Import module to grab rooms
import players            # Import module to grab players



# -== CODE ==-
scr = screen.Screen()
cur_room = ''

def sleep(s):
    scr.hide_c()
    time.sleep(s)
    scr.show_c()

def rooms_items_build(rooms, chapter_items, chapter):
    for r in rooms:
        item_amt = random.randint(1, 5)
        for i in range(0, item_amt):
            item_id = random.randint(1, len(chapter_items))
            r.items.append(chapter_items[item_id])

def check_notes(player):
    new_inv = []
    notes = []
    for i in player.inv:
        if i.readable:
            notes.append(i)
        else:
            new_inv.append(i)
    for n in notes:
        if n not in new_inv:
            new_inv.append(n)
        else:
            pass
    player.inv = new_inv

def check_player(player):
    if player.health == 0:
        player.die(scr, 'you failed at living')
        sleep(2.5)
        scr.cls()
        sys.exit(0)

def print_exits(room):
    if not room.n == 0:
        print('     North - ' + rooms.rooms_c1[room.n].name)
    if not room.e == 0:
        print('     East - ' + rooms.rooms_c1[room.e].name)
    if not room.s == 0:
        print('     South - ' + rooms.rooms_c1[room.s].name)
    if not room.w == 0:
        print('     West - ' + rooms.rooms_c1[room.w].name)
    if not room.up == 0:
        print('     Up - ' + rooms.rooms_c1[room.up].name)
    if not room.down == 0:
        print('     Down - ' + rooms.rooms_c1[room.down].name)

def check_action(a, player, cur_r):
    if a == 'eat':
        player.eat()
        return True, 0
    elif a == 'drink':
        player.drink()
        return True, 0
    elif a == 'read':
        player.read()
        return True, 0
    elif a == 'debug':
        player.debug([items.items_c1[1], items.items_c1[2], items.items_c1[3]])
        return True, 0
    elif a == 'n' or a == 'w' or a == 'e' or a == 's':
        new_room = player.move(a, cur_r)
        if new_room == False:
            print()
            print()
            print('     Can\'t move in that direction')
            sleep(.6)
            return False, 0
        else:
            return True, rooms.rooms_c1[new_room]
    elif a == 'look':
        player.look(cur_r, scr)
        return True, 0
    elif a == 'exit':
        scr.cls()
        sys.exit(0)
    else:
        print()
        print()
        print('     ' + a + ' - Invalid')
        sleep(.6)
        return False, 0

scr.cls()
scr.title('Roleplay')
scr.hide_c()
user_chapter_sel = scr.p_opts_screen(1, 1, 5, menus.main_menu)
if user_chapter_sel == 1:
    scr.cls()
    scr.title('Character Select')
    user_player_sel = scr.p_opts_screen(1, 1, 2, menus.player_menu_c1)
    scr.show_c()
    if user_player_sel == 1:
        player_c1 = players.players_c1[1]
        cur_room = rooms.rooms_c1[1]
    elif user_player_sel == 2:
        player_c1 = players.players_c1[2]
        cur_room = rooms.rooms_c1[1]
    rooms_items_build(rooms.rooms_c1.values(), items.items_c1, 1)
    while True:
        scr.cls()
        scr.title('Chapter One - ' + cur_room.name)
        print()
        print()
        print()
        print('     ' + player_c1.name + ' - Health: ' + str(player_c1.health) + ' | Hunger: ' + str(player_c1.hunger) + ' | Thirst: ' + str(player_c1.thirst))
        print()
        print('     ' + ('-'*50))
        print()
        if player_c1.name == 'Evs':
            scr.p_loc(cur_room, 1)
        else:
            scr.p_loc(cur_room, 2)
        print()
        print('     ' + ('-'*50))
        print()
        print_exits(cur_room)
        print()
        print()
        user_action = str(input('     Action: ')).lower()
        check_notes(player_c1)
        happened, new_r = check_action(user_action, player_c1, cur_room)
        check_player(player_c1)
        if not new_r == 0:
            cur_room = new_r
        else:
            pass

elif user_chapter_sel == 2:
    pass
elif user_chapter_sel == 3:
    pass
elif user_chapter_sel == 4:
    pass
elif user_chapter_sel == 5:
    pass
else:
    scr.cls()
    scr.show_c()
    sys.exit(0)
