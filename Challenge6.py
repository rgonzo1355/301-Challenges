# Script Name:                  Ops Challenge 6 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      12/04/2023
# Purpose: To learn for a career in cyber security. Today, you will be executing a Linux terminal commands from within a Python script.  

import os

# Declare and reference three variables
name = "John"
age = 25
location = "CityX"

# Print variables using the print() function
print("Name:", name)
print("Age:", age)
print("Location:", location)

# Execute bash commands using os.popen() and capture the results
print("\nExecuting bash commands:")

try:
    # Execute 'whoami' command and capture the output
    whoami_output = os.popen('whoami').read()
    print("Current user:", whoami_output.strip())

    # Execute 'ip a' command and capture the output
    ip_address_output = os.popen('ip a').read()
    print("IP address information:")
    print(ip_address_output)

    # Execute 'lshw -short' command and capture the output
    hardware_info_output = os.popen('lshw -short').read()
    print("Hardware information:")
    print(hardware_info_output)

except Exception as e:
    print("Error executing bash commands:", e)
