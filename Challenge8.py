#!/usr/bin/env python3
# Author: Rodolfo Gonzalez
# Date: 12-6-23

# Objectives:

# Assign a list of ten string elements to a variable: The code assigns ten strings to the my_list variable, fulfilling this requirement.
# Print the fourth element of the list: The code uses list indexing to access and print the fourth element (date) of the list, satisfying this requirement.
# Print the sixth through tenth element of the list: 
# The code uses list slicing to access and print elements from the sixth (fig) to tenth (lemon) positions, fulfilling this requirement.
# Change the value of the seventh element to "onion": The code uses list assignment to modify the seventh element ("grape") to "onion", achieving this objective.

# Stretch Goals:

# Use Python methods to manipulate the list: The code utilizes various list methods like append, # 
# copy, count, extend, index, insert, pop, remove, reverse, and sort to manipulate the list, demonstrating understanding of these methods.
# Create one tuple, set, and dictionary: The code defines separate variables 
# # for a my_tuple, my_set, and my_dict, each containing elements appropriate for their respective data structures. This satisfies the stretch goals.
# Resources: https://chat.openai.com/share/3f6929d2-a439-4b3d-82e3-c61441535a65  

# List of fruits
fruits_list = ["apple", "banana", "cherry", "date", "watermelon", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Print the fourth element
print("Fourth element:", fruits_list[3])

# Print elements from sixth to tenth
print("Sixth through tenth elements:", fruits_list[5:])

# Change the seventh element to "onion"
fruits_list[6] = "onion"

# Print the modified list
print("Modified list:", fruits_list)

# --- Stretch Goals ---

# Append "mango" to the list
fruits_list.append("mango")

# Create a copy of the list
list_copy = fruits_list.copy()

# Count the occurrences of "apple"
count_of_apple = fruits_list.count("apple")

# Extend the list with ["orange", "pear"]
fruits_list.extend(["orange", "pear"])

# Find the index of "cherry"
index_of_cherry = fruits_list.index("cherry")

# Insert "blueberry" at the second position
fruits_list.insert(2, "blueberry")

# Remove the last element and store it in a variable
popped_element = fruits_list.pop()

# Remove "banana" from the list
fruits_list.remove("banana")

# Reverse the order of the list
fruits_list.reverse()

# Sort the list in ascending order
fruits_list.sort()

# Print the final list after manipulations
print("Final list after manipulations:", fruits_list)

# --- Optional Data Structures ---

# Create a tuple of numbers
numbers_tuple = (1, 2, 3, 4, 5)

# Create a set of unique numbers
unique_numbers_set = {1, 2, 3, 4, 5}

# Create a dictionary mapping items to their prices
item_price_dict = {"apple": 1, "banana": 0.5, "cherry": 2, "blueberry": 1.5, "date": 1, "fig": 1.2, "grape": 1.8, "honeydew": 2.5, "kiwi": 1.5, "lemon": 1}

# Print the created data structures
print("Tuple:", numbers_tuple)
print("Set:", unique_numbers_set)
print("Dictionary:", item_price_dict)
