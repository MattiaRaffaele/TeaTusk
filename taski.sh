#!/bin/bash

terminalColorClear='\033[0m'
terminalColorEmphasis='\033[1;32m'
terminalColorError='\033[1;31m'
terminalColorMessage='\033[1;33m'
terminalColorWarning='\033[1;34m'
 
echoDefault() {
    echo -e "${terminalColorClear}$1${terminalColorClear}"
}
 
echoMessage() {
    echo -e "${terminalColorMessage}$1${terminalColorClear}"
}
 
echoWarning() {
    echo -e "${terminalColorWarning}$1${terminalColorClear}"
}
 
echoError() {
    echo -e "${terminalColorError}$1${terminalColorClear}"
}


command=$1

if [ "$command" = "add" ];
then

  {
    cd 'C:\Users\\Documents\Github\taski'
  }||{
    echo "The file 'newtask.py' wich is used for creating new task can't be located \ Would you like to start troubleshoot(y/n)" 
  }

  {
    python newtask.py
  }||{
    python3 newtask.py
  }||{
    echoMessage "Looks like that Python is not installed in your machine, would you like to install it? (y/n)"
    read = userInput
    

    if [ userInput = "y" ];
    then

      sudo apt update
      sudo apt install python3

      echoMessage "Python installed!"
    fi

  }

else
  echo "$command is not recognized as a valid input"
fi
