#!/bin/bash

echo "Programma avviato"

Command=$1

echo "Hai Scritto $Command"


{
	nohup python newtask.py
}||{
	echo "Location of newtask.py not found. -e Write the relocation here"
}
