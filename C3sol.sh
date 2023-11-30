#!/bin/bash

# Script Name:                  Ops Challenge 2 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      11/30/2023
# Purpose:                      Sol 

# Declare Variables

# Get input from the user - a directory to change permissions for
read -p "what directory do you want to change permissions for?" Input_dir

# Get the permission that the user wants to use
read -p "What permissions do you want to give the folder?" input_perm

# Do the actual changing of permissions
chmod -R $input_perm $Input_dir
# Show the permission to verify the changes
ls -al $input_dir