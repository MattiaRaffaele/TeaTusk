import json
from colorama import Fore

def appendJson(task= "task", description= "description", priority="priority"):
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
    userInput = input()

    appendJson(task=userInput, description="", priority="")


def setDescription():
    print("Type the task description or press ENTER to skip")
    userInput = input()

    if userInput == "":
        setPriority()
    else:
        appendJson(description=userInput)


def setPriority():
    print("Set Priority (type 0, 1, 2)")
    userInput = input()

    if userInput != "0" and userInput != "1" and userInput != "2":

        print(Fore.RED + "\nInsert a valid input >:(\n" + Fore.RESET)
        setPriority()

    else:
        appendJson(priority=userInput)


setTitle()
setDescription()
setPriority()