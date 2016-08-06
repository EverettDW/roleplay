# Filename: assets.py
import sys
import time
import os
import menu_sel
from msvcrt import getch



# -== PLAYER ==-
class Player(object):
    ''' A base class for the player '''

    def __init__(self, name, health, hunger, thirst, damage, weapon):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.damage = damage
        self.weapon = weapon
        self.inv = []

    def debug(self, items):
        self.inv.extend(items)

    def add_item(self, item):
        self.inv.append(item)

    def move(self, side, cur_map):
        if side == 'n':
            if cur_map.n == 0:
                return False
            else:
                if not self.hunger <= 20:
                    self.hunger -= 4
                else:
                    if not self.health <= 0:
                        self.health -= 2
                if not self.thirst <= 20:
                    self.thirst -= 3
                else:
                    if not self.health <= 0:
                        self.health -= 2
                return cur_map.n
        if side == 'e':
            if cur_map.e == 0:
                return False
            else:
                if not self.hunger <= 20:
                    self.hunger -= 4
                else:
                    if not self.health <= 0:
                        self.health -= 2
                if not self.thirst <= 20:
                    self.thirst -= 3
                else:
                    if not self.health <= 0:
                        self.health -= 2
                return cur_map.e
        if side == 's':
            if cur_map.s == 0:
                return False
            else:
                if not self.hunger <= 20:
                    self.hunger -= 4
                else:
                    if not self.health <= 0:
                        self.health -= 2
                if not self.thirst <= 20:
                    self.thirst -= 3
                else:
                    if not self.health <= 0:
                        self.health -= 2
                return cur_map.s
        if side == 'w':
            if cur_map.w == 0:
                return False
            else:
                if not self.hunger <= 20:
                    self.hunger -= 4
                else:
                    if not self.health <= 0:
                        self.health -= 2
                if not self.thirst <= 20:
                    self.thirst -= 3
                else:
                    if not self.health <= 0:
                        self.health -= 2
                return cur_map.w

    def eat(self):
        food = []
        last_item = ''
        counter = 0
        for i in self.inv:
            if i.eatable:
                food.append(i)
        if food == []:
            return False
        while True:
            os.system('cls')
            os.system('title Inv')
            print()
            print()
            print()
            for f in food:
                if counter == 0 :
                    last_item = f.name.lower()
                    print('     ' + f.name + ' *', end='', flush=True)
                else:
                    if f.name.lower() == last_item:
                        print('*', end='', flush=True)
                    else:
                        print()
                        print('     ' + f.name + ' *', end='', flush=True)
                last_item = f.name.lower()
                counter += 1
            print()
            print()
            user_food = str(input('     Food: ')).lower()
            if user_food == 'exit':
                return True
            for f in food:
                if user_food == f.name.lower():
                    f.use(self, 'eat')
                    return True

    def drink(self):
        drink = []
        last_item = ''
        counter = 0
        for i in self.inv:
            if i.drinkable:
                drink.append(i)
        if drink == []:
            return False
        while True:
            os.system('cls')
            os.system('title Inv')
            print()
            print()
            print()
            for d in drink:
                if counter == 0 :
                    last_item = d.name.lower()
                    print('     ' + d.name + ' *', end='', flush=True)
                else:
                    if d.name.lower() == last_item:
                        print('*', end='', flush=True)
                    else:
                        print()
                        print('     ' + d.name + ' *', end='', flush=True)
                last_item = d.name.lower()
                counter += 1
            print()
            print()
            user_drink = str(input('     Drink: ')).lower()
            if user_drink == 'exit':
                return True
            for d in drink:
                if user_drink == d.name.lower():
                    d.use(self, 'drink')
                    return True

    def read(self):
        notes = []
        for i in self.inv:
            if i.readable:
                notes.append(i)
        if notes == []:
            return False
        while True:
            os.system('cls')
            os.system('title Inv')
            print()
            print()
            print()
            for n in notes:
                print('     ' + n.name)
            print()
            print()
            user_note = str(input('     Note: ')).lower()
            if user_note == 'exit':
                return True
            for n in notes:
                if user_note == n.name.lower():
                    n.use(self, 'read')
                    return True

    def look(self, cur_room, scr):
        if cur_room.items != []:
            cur_rooms_dict = {}
            cur_rooms_dict_r = {}
            index = 1
            for i in cur_room.items:
                if i.name not in cur_rooms_dict.keys():
                    cur_rooms_dict[i.name] = i
                else:
                    cur_rooms_dict[i.name + '-'] = i
                cur_rooms_dict_r[index] = i
                index += 1
            scr.cls()
            scr.title('     Items in ' + cur_room.name)
            cur_room_items = menu_sel.menu_sel(cur_rooms_dict.keys())
            user_item_sel = scr.p_opts_screen(1, 1, len(cur_room_items), cur_room_items)
            self.add_item(cur_rooms_dict_r[user_item_sel])
            cur_room.items.remove(cur_rooms_dict_r[user_item_sel])
        else:
            pass

    def die(self, scr, cause):
        scr.cls()
        scr.hide_c()
        scr.title('GAME OVER')
        print()
        print()
        print()
        print('     ---------------------------')
        print()
        print('              GAME OVER')
        print()
        print('     ---------------------------')
        print()
        print()
        print('     You died cause ' + cause)
        print()
        print()



# -== ITEMS ==-
class Item(object):
    ''' A class to make items that can be eaten, equipped, etc, etc '''

    def __init__(self, name, hunger_r, thirst_r, damage, writing):
        self.name = name
        self.hunger_rec = hunger_r
        self.thirst_rec = thirst_r
        self.damage = damage
        self.writing = writing
        if self.hunger_rec > 0 and self.thirst_rec > 0:
            self.eatable = True
            self.drinkable = False
        elif self.hunger_rec > 0 and not self.thirst_rec > 0:
            self.eatable = True
            self.drinkable = False
        elif not self.hunger_rec > 0 and self.thirst_rec > 0:
            self.drinkable = True
            self.eatable = False
        else:
            self.drinkable = False
            self.eatable = False
        if self.damage > 0:
            self.equipable = True
        else:
            self.equipable = False
        if not self.writing == '':
            self.readable = True
        else:
            self.readable = False

    def use(self, player, a):
        if a == 'eat':
            if self.eatable:
                if player.hunger + self.hunger_rec > 100:
                    player.hunger == 100
                else:
                    player.hunger += self.hunger_rec
                player.inv.remove(self)
            if self.drinkable:
                if player.thirst + self.thirst_rec > 100:
                    player.thirst == 100
                else:
                    player.thirst += self.thirst_rec
                player.inv.remove(self)
        elif a == 'drink':
            if self.drinkable:
                if player.thirst + self.thirst_rec > 100:
                    player.thirst == 100
                else:
                    player.thirst += self.thirst_rec
                player.inv.remove(self)
        elif a == 'equip':
            if self.equipable:
                player.weapon = self.name
                player.damage = self.damage
        elif a == 'read':
            if self.readable:
                os.system('cls')
                os.system('title Note - ' + self.name)
                print()
                print()
                print()
                print(self.writing)
                print()
                print()
                print('     Press any button to continue: ', end='', flush=True)
                _ = getch()



# -== ROOMS ==-
class Room(object):
    ''' A class for rooms '''

    def __init__(self, name, desc, desc_2, items, n, e, s, w, up, down):
        self.name = name
        self.desc = desc
        self.desc_2 = desc_2
        self.items = items
        self.n = n
        self.e = e
        self.s = s
        self.w = w
        self.up = up
        self.down = down
