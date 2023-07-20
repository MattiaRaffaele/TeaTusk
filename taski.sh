#!/bin/bash


function LocateFolder(){
  echoMessage "Copy and paste in the terminal the location below"
  whereis
  read = newLocation
}



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
    cd 'C:\Users\\Documents\Github\taski' 2>/dev/null
  }||{

    
    echoError "The file 'newtask.py' wich is used for creating new task can't be located" 
    echoMessage "Would you like to run the troubleshoot (y/n)"


    read=userInput
    if [ $userInput = "y" ];
    then
      LocateFolder

    else
      echo "I'm sorry maybe you could help me get better on Github"
    fi

  }

  {
    python newtask.py 2>/dev/null
  }||{
    python3 newtask.py 2>/dev/null
  }||{
    echoMessage "Looks like that Python is not installed in your machine, would you like to install it? (y/n)"
    read=userInput
    

    if [ $userInput = "y" ];
    then

      sudo apt update
      sudo apt install python3

      echoMessage "Python installed!"
    fi

  }

else
  echo "$command is not recognized as a valid input"
fi
