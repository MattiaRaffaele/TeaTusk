#Import libraries
import json
import questionary
from colorama import Fore

#functions
def setTitle():
    print ("Insert Title (max. 12)")
    titleInput = input(Fore.CYAN)
 
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
    print ("\nThose prompts were made able by the python library 'questionary' wich I highly reccomend\n")
    questionaryOutput = questionary.select(
        "TeaTusk menu",
        choices = [
            "Title",
            "Description",
            "Priority",
            "Exit"
            ]).ask()


    #Menu backend
    if questionaryOutput == "Title":
        setTitle()

    elif questionaryOutput == "Description":
        setDescription()

    elif questionaryOutput == "Priority":
        print (Fore.LIGHTCYAN_EX + "\n---COMING SOON---\n" + Fore.RESET)
        _menu_()

    elif questionaryOutput == "Exit":
        questionary.confirm("Are you sure?").ask()


_menu_()