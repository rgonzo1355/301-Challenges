#!/usr/bin/env python3
# Author        Rodolfo Gonzalez
# Date          12-6-23

# Create a list

#               0        1        2         3           4       5
my_list = ['apples', 'orange', 'cherry', 'watermelon', 'banana', 'kiwi']  

# Example 1: Print the entire list
print("Entire list:", my_list)

# Example 2: Print the first item
print("First item:", my_list[0])

# Example 3: Print elements from index 1 to 3 (excluding 4)
print("Elements from index 1 to 3:", my_list[1:4])

# Example 4: Print every second element starting from index 1
print("Every second element starting from index 1:", my_list[1::2])

# Example 5: Reverse the list and print it
print("Reversed list:", my_list[::-1])

# Example 6: Print elements in reverse order from index 2 to the beginning
print("Reverse order from index 2 to the beginning:", my_list[2::-1])

# Example 7: Print the item 'cherry'
print("Item 'cherry':", my_list[2])

# Example 8: Print a custom selection of elements
print("Custom selection of elements:", my_list[1:4] + my_list[-2:])



