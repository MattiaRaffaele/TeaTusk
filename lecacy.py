import json
from colorama import Fore

def appendJson(title, description, priority):
    with open('data.json', 'r') as f:
        jsonFile = json.load(f)

    jsonFile.append({
        'task': task,
        'description': description,
        'priority': priority
    })

    with open("data.json", "w") as f:
        json.dump(jsonFile, f, indent=4, separators=(',', ': '))

def setTitle():
    print("Type the name of the task")
    titleInput = input()

    return titleInput


def setDescription():
    print("Type the task description or press ENTER to skip")
    descriptionInput = input()

    if userInput == "":
        setPriority()
    else:
        return descriptionInput


def setPriority():
    print("Set Priority (type 0, 1, 2)")
    priorityInput = input()

    if priorityInput != "0" and priorityInput != "1" and priorityInput != "2":

        print(Fore.RED + "\nInsert a valid input >:(\n" + Fore.RESET)
        setPriority()

    else:
        return priorityInput


setTitle()
setDescription()
setPriority()
appendJson(title=titleInput, description=descriptionInput, priority=priorityInput)
