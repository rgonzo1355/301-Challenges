
#!/bin/python3

# Script Name:                  Ops Challenge 10 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      12/8/2023
# Objectives:
""" Creates a new text file named "example.txt" 
    Appends three lines to it
    Reads and prints the first line from the file.
    Deletes the file afterward."""                      

# Import the os module for operating system-related tasks
import os

# Step 1: Create a new .txt file
file_path = "example.txt"

# Step 2: Append three lines to the file
with open(file_path, "a") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Step 3: Read and print the first line
with open(file_path, "r") as file:
    # Read the first line from the file
    first_line = file.readline()
    # Print the first line (strip removes newline characters for cleaner output)
    print("First line:", first_line.strip())

# Step 4: List the file in its location
print(f"\nThe file '{file_path}' is located in: {os.path.abspath(file_path)}")

# Step 5: Prompt the user to press Enter to delete the file
input("\nPress Enter to delete the file...")

# Step 6: Delete the .txt file
os.remove(file_path)

# Step 7: Display a message indicating successful deletion
print("File deleted successfully.")


