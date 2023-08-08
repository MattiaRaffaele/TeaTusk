import json
from colorama import Fore


def setTitle():
    print("Type the name of the task")
    userInput = input()

    appendJson(task=userInput)


def setPriority():
    print("Set Priority (type 0, 1, 2)")
    userInput = input()

    if userInput != "0" and userInput != "1" and userInput != "2":

        print(Fore.RED + "\nInsert a valid input >:(\n" + Fore.RESET)
        setPriority()

    else:
        appendJson(priority=userInput)


def appendJson(task, priority):
    with open('data.json', 'r') as f:
        jsonFile = json.load(f)

    jsonFile.append({
        'task': task,
        'priority': priority
    })

    with open("data.json", "w") as f:
        json.dump(jsonFile, f, indent=4, separators=(',', ': '))


setTitle()
setPriority()
appendJson()