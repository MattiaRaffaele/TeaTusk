#Import libraries
import json
import pick
from colorama import Fore

#functions
def setTitle():
    print ("Insert Title (max. 12)")
    titleInput = input()

    #Checks the length of the input
    if len(titleInput) < 12:
        return titleInput
    else:
        print (Fore.RED + '\n---The title must have a maximum of 12 letters---\n' + Fore.RESET)
        setTitle()

def setDescription():
    print ("Description")
    descriptionInput = input()

    return descriptionInput

def _menu_():

    # Menu GUI
    options = ['Title', 'Description', 'Priority', 'Exit']
    pickle = pick.pick(options, "TeaTusk Menu", indicator='>>', default_index=0)

    # Menu backend
    if 'Title' in pickle:
        setTitle()

    elif 'Description' in pickle:
        setDescription()

    elif 'Priority' in pickle:
        print (Fore.BLUE + "\n!!!Coming Soon!!!\n" + Fore.RESET)

_menu_()