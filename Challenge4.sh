#!/bin/bash

# Script Name:                  Ops Challenge 2 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      11/30/2023
# Purpose:                      Conditionals in menu systems

# This line tells the shell which interpreter to use to execute the script.

while true; do
  # This loop will continue to run until the user chooses to exit the program.
  echo "Menu:"
  # This line displays the menu options to the user.
  echo "1. Hello world"
  # This line displays the first menu option.
  echo "2. Ping self"
  # This line displays the second menu option.
  echo "3. IP info"
  # This line displays the third menu option.
  echo "4. Exit"
  # This line displays the fourth menu option.

  read -p "Enter your choice (1-4): " choice
  # This line prompts the user to enter their choice.

  case $choice in
    1)
      echo "Hello world!"
      # This line displays the "Hello world!" message if the user chooses option 1.
      ;;
    2)
      ping -c 4 127.0.0.1
      # This line pings the loopback address (127.0.0.1) four times if the user chooses option 2.
      ;;
    3)
      ifconfig
      # This line displays the network adapter information if the user chooses option 3.
      ;;
    4)
      echo "Exiting the program. Goodbye!"
      # This line displays the exit message if the user chooses option 4.
      exit 0
      # This line exits the program with a status code of 0.
      ;;
    *)
      echo "Invalid choice. Please enter a number between 1 and 4."
      # This line displays an error message if the user enters an invalid choice.
      ;;
  esac

  echo
  # This line adds a newline for better readability.
done
