#!/bin/bash

# Script Name:                  Ops Challenge 3 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      11/29/2023
# Purpose:                      Give permissions

# Function to change file permissions
Change-Permissions() {
  # Read directory path from user
  read -p "Enter the directory path: " directory

  # Validate directory path
  # Check if the directory exists
  if [ ! -d "$directory" ]; then
    echo "Error: Invalid directory path '$directory'."
    return 1
  fi

  # Read permission number from user
  read -p "Enter the input permissions number: " permission_number

  # Validate permission number
  # Ensure the permission number is within the valid range (0-777)
  if [[ ! $permission_number =~ ^[0-7]+$ ]]; then
    echo "Error: Invalid permission number '$permission_number'. Please enter a valid number between 0 and 777."
    return 1
  fi

  # Change file permissions
  # Change permissions for all files in the specified directory
  cd "$directory"
  chmod $permission_number *

  # Display updated permissions
  DisplayPermissions
}

# Function to display updated permissions
DisplayPermissions() {
  # Clear the output area
  clear

  # Display updated permissions for each file
  echo "Updated permissions:"
  ls -ld *
}

# Call the function
Change-Permissions
