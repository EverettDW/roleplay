# Filename: screen.py
# Made to help roleplay.py with controlling the screen
import time              # Because sleep
import sys               # For the show and hide cursor
import os                # For the show and hide cursor
from msvcrt import getch # For the menu selection

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

# Hides cursor in Windows cmd and Linux command line
def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

# Function to show the cursor in Windows cmd and Linux command line
def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

# Function to clear the screen on MSDOS systems or basically Windows.
def cls():
    os.system('cls')

# Function to set the title on a Windows command prompt using the system function in the 'os'
# module
def title(t):
    os.system('title ' + str(t))

# -== SCREEN CLASS ==-
class Screen(object):
    ''' A class for a screen on windows cmd\'s '''

    def hide_c(self):
        hide_cursor()

    def show_c(self):
        show_cursor()

    def cls(self):
        cls()

    def title(self, t):
        title(t)

    def p_loc(self, loc, opt):
        if opt == 1:
            print(loc.desc)
        elif opt == 2:
            print(loc.desc_2)

    def p_opts_screen(self, def_num, min_op, max_op, menu):
        enter_not_pressed = True
        while enter_not_pressed:
            cls()
            print()
            print()
            print()
            print(menu[def_num])
            key = ord(getch())
            if key == 224:
                key = ord(getch())
                if key == 72:  # -UP-
                    if def_num == min_op:
                        pass
                    else:
                        def_num -= 1
                if key == 80:  # -DOWN-
                    if def_num == max_op:
                        pass
                    else:
                        def_num += 1
            elif key == 13:
                enter_not_pressed = False
                return def_num
            elif key == 27:
                return False
