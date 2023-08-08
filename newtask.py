import json
from colorama import Fore


def setTitle():
    print("Type the name of the task")
    userInput = input()

    with open('data.json', 'r') as f:
        jsonFile = json.load(f)

    jsonFile.append({
        'title': userInput
    })

    with open("data.json", "w") as f:
        json.dump(jsonFile, f, indent=4, separators=(',', ': '))


def setPriority():
    print("Set Priority (type 0, 1, 2)")
    userInput = input()

    if userInput != "0" or "1" or "2":
        print(Fore.RED + "\nInsert a valid input >:(\n" + Fore.RESET)
        setPriority()
    else:

        with open('data.json', 'r') as f:
            jsonFile = json.load(f)

        jsonFile.append({
            'priority': userInput
        })

        with open("data.json", "w") as f:
            json.dump(jsonFile, f, indent=4, separators=(',', ': '))


setTitle()
setPriority()
