#!/bin/bash

import json

userInput = input()
    


with open ('data.json' , 'r') as f:
    jsonFile = json.load(f)

jsonFile.append({
        'title':userInput
    })
    
with open("data.json" , "w") as f:
    json.dump(jsonFile , f, indent=4 , separators=(',',': '))

