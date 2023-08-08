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
    python newtask.py 2>/dev/null
  }||{
    python3 newtask.py 2>/dev/null
  }||{
    echoMessage "Looks like that Python is not installed in your machine, would you like to install it? (y/n)"
    read userInput

    if [ "$userInput" = "y" ];
    then

      {
        sudo apt update 2>/dev/null && sudo apt install python3 2>/dev/null

        echoMessage "Python installed!"
      }||{
        echoError "Python must be installed manually"
      }

    elif [ "$userInput" = "n" ];
    then
      echo "I'm sorry maybe you could help me get better on Github"
      exit
    fi

   }

else
   python main.py
fi
