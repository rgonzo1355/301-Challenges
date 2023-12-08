#!/bin/python3

# Script Name:                  Ops Challenge 9 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      12/7/2023
# Purpose: 

""" Objectives
Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

Create an if statement that includes both elif and else to execute when both if and elif are not met.
Resources: https://chat.openai.com/share/7b3b9e0d-1061-47b7-b4e2-216253f1b7fd https://www.youtube.com/watch?v=rfscVS0vtbw"""

# Fitness Recommendations

# Define a function to validate user input and ensure correct data type.
def validate_input(value, data_type, prompt):
    """
    This function checks if the user's input is a valid data type.
    Args:
        value: The current input value.
        data_type: The expected data type (e.g., str, int, float).
        prompt: The message displayed to the user for input.
    Returns:
        The validated user input.
    """
    while True:
        try:
            # Convert the user input to the specified data type.
            return data_type(input(prompt))
        except ValueError:
            # If the input is invalid, display an error message and ask again.
            print("Invalid input. Please enter a valid", data_type.__name__, ".")

# Get the user's name.
participant_name = validate_input(None, str, "Enter your name: ")

# Get the user's current weight in pounds.
current_weight = validate_input(None, float, "Enter your current weight in pounds: ")

# Get the user's goal weight in pounds.
goal_weight = validate_input(None, float, "Enter your goal weight in pounds: ")

# Check if the goal weight is higher than the current weight and display an error message if so.
if goal_weight > current_weight:
    print("Goal weight cannot be higher than current weight.")
    exit()

# Get the desired number of weeks to achieve the goal.
desired_weeks = validate_input(None, int, "Enter the number of weeks you want to achieve your goal in: ")

# Calculate the total weight to lose and the recommended weight loss per week.
total_weight_to_lose = current_weight - goal_weight
recommended_weight_loss_per_week = total_weight_to_lose / desired_weeks

# Display a personalized message with the user's information and goal.
print(f"\nHello, {participant_name}!\n")
print(f"Current weight: {current_weight:.2f} pounds")
print(f"Goal weight: {goal_weight:.2f} pounds")
print(f"Desired time to achieve goal: {desired_weeks} weeks\n")

# Check if the goal is achievable and display a message accordingly.
if recommended_weight_loss_per_week > 0:
    print(f"To reach your goal in {desired_weeks} weeks, it is recommended to lose approximately {recommended_weight_loss_per_week:.2f} pounds per week.")
else:
    print("Your goal weight has already been achieved! Congratulations!")

# Provide additional resources for workout plans, diet advice, and progress tracking.
print("\nHere are some additional resources to help you reach your fitness goals:")
print("- Workout plans: https://madmuscles.com/")
print("- Diet advice: https://healthinsider.news/perfectbody-me-review-perfect-weight-loss-en/")
print("- Progress tracker: https://www.myfitnesspal.com/")

# Encourage the user to track their progress for motivation.
print("\nRemember to track your progress regularly to stay motivated!")

# Disclaimer: 
print("\nDisclaimer: This program is for entertainment purposes only\n"
      "and is not intended to be a substitute for professional medical advice.\n"
      "Please consult with a healthcare professional before making any changes to your diet or exercise routine.")



