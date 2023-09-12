separator = "\n------------------------------------------------------------------------------------------------"

import json
from colorama import Fore


def err():
    print(Fore.RED + "Something wrong has happened."
                     "\nPossible cases:"
                     "\n>> 'data.json' can't be located (highly possible)"
                     "\n"
          + Fore.LIGHTBLACK_EX +
          ">> 'data.json' could be corrupted"
          "\n>> 'data.json' could contain syntax errors, have you tried to open it?"
          + separator + Fore.RED +
          "\nDo not consider uninstalling because the task are saved locally and this would delete everything!")


def jsonLoad():
    with open('data.json', 'r') as f:
        jsonFile = json.load(f)

    for title in jsonFile:

        for title in jsonFile:
            titleToPrint = title['title']

        for description in jsonFile:
            descriptionToPrint = description['description']

        print("Task:    Author:"
              "\n"
              + titleToPrint + "  " + descriptionToPrint)


def stop():
    print(Fore.RESET)


try:
    jsonLoad()

except:
    err()

stop()
