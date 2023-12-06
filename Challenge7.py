#!/usr/bin/env python3
# Author        Rodolfo Gonzalez
# Date          12-5-23
# Purpose:      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# Resources: https://chat.openai.com/share/04cb2776-335b-40a0-bf84-d1e3576a9cf3 
# Import libraries
import os

# Declaration of functions
def generate_directory_info(user_path):
    # This function takes a user-provided directory path and uses os.walk()
    # to print information about all directories, sub-directories, and files.

    # os.walk() returns three values: root (current directory),
    # dirs (list of sub-directories), and files (list of files in the current directory).
    for (root, dirs, files) in os.walk(user_path):
        # Print the root directory
        print(f"Root Directory: {root}")

        # Print the list of sub-directories
        print(f"Sub-directories: {dirs}")

        # Print the list of files
        print(f"Files: {files}")

        # Add a new line for better readability
        print("\n")

# Main
if __name__ == "__main__":
    # Declaration of variables

    # Read user input here into a variable
    user_path = input("Enter the directory path: ")

    # Pass the variable into the function here
    generate_directory_info(user_path)
