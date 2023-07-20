#!/bin/bash

command=$1

if [ "$command" = "add" ];
then

  {
    cd 'C:\Users\raffa\Documents\Github\taski'
  }||{
    echo "The file 'newtask.py' wich is used for creating new task can't be located -e Would you like to start troubleshoot(y/n)" 
  }

  {
    python newtask.py
  }||{
    python3 newtask.py
  }||{
    echo "Looks like that Python is not installed in your machine, would you like to install it? (y/n)"
    read = userInput
    

    if [ userInput = "y" ];
    then

      sudo apt update
      sudo apt install python3

      echo "Python installed!"
    fi

  }

else
  echo "$command is not recognized as a valid input"
fi
