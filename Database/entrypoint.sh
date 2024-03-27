#!/bin/bash
echo "Enter if you want to add(press 1) or to retrive(press 2) stock data from database"
read command
if [[ $command -eq 1 ]]
then 
    python3 add_table.py
elif [[ $command -eq 2 ]]
then 
    python3 retrieveData.py
fi