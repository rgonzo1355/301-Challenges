# They python module "os" must be utilized.
# import the os as a module
import os
# import the time module
import time
# import the system module
import sys

# Requirements:

# At least three variables must be declared and referenced in Python.
def get_user_name():
    user = input("Please enter the name: ")
    return user

# The Python function print() must be used at least three times.
# Include execution of the following bash commands inside your Python script:

# function for menu passing in the user as a parameter
def menu(user):
    # Start the while loop
    while True:
        # set variable for user name
        message = "Hello " + user + ". Let's try some commands"
        # print the message and menu
        print(message)
        print('1. whoami')
        print('2. ip a ')
        print('3. lshw -short')
        print('4. Exit')
        # Get user answer and assign it to the answer variable
        answer = input("What do you want to do: ")
        # Conditional check of answers 
        if answer =='1':
            # runs the bash command
            os.system('whoami')
            # waits for the user to press enter to continue
            input('Press Enter to continue')
            # clears the screen
            os.system('clear')
        elif answer == '2':
            # adjusted for Linux
            os.system('ip addr')  # Use 'ip addr' for Linux
            input('Press Enter to continue')
            os.system('clear')  # Use 'clear' for Linux
        elif answer =='3':
            # adjusted for Linux
            os.system('lshw -short')  # Use 'lshw -short' for Linux
            input('Press Enter to continue')
            os.system('clear')  # Use 'clear' for Linux
        elif answer =='4':
            sys.exit('\nHave a Great Day')
            # catch all in case they don't enter 1-4
        else:
            print("Not a valid choice, try again")
            time.sleep(2)
            os.system('clear')  # Use 'clear' for Linux

# main gate function
if __name__ == "__main__":
    user = get_user_name()
    start_menu = input("Do you want to start the menu? (yes/no): ")
    if start_menu.lower() == "yes":
        menu(user)
    else:
        print("Exiting the script. Have a great day!")
