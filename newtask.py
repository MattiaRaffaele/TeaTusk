#!/bin/bash

import json

print("Type the name of the task")
userInput = input()
    


with open ('data.json' , 'r') as f:
    jsonFile = json.load(f)

jsonFile.append({
        'title':userInput
    })
    
with open("data.json" , "w") as f:
    json.dump(jsonFile , f, indent=4 , separators=(',',': '))

