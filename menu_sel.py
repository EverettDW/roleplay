# Filename: menu_sel.py
def menu_sel(opts):
    menu_ind = []
    menu_dict = {}
    menu = []
    index = 0
    d_ind = 0
    for i in range(0, len(opts)):
        for o in opts:
            if index == 0:
                menu_ind.append('     < ')
                menu_ind.append(o)
                menu_ind.append(' >\n')
            else:
                if index == d_ind:
                    menu_ind.append('     < ')
                    menu_ind.append(o)
                    menu_ind.append(' >\n')
                else:
                    menu_ind.append('       ')
                    menu_ind.append(o)
                    menu_ind.append('\n')
            index += 1
        menu.append(''.join(menu_ind))
        menu_ind = []
        d_ind += len(opts) + 1
    for i in range(0, len(menu)):
        menu_dict[i+1] = menu[i]
    return menu_dict
