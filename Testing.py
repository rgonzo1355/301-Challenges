import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Allow the user three attempts to guess the number
for _ in range(3):
    guess = int(input("Guess the number between 1 and 10: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again!")

# If the user couldn't guess the correct number in three attempts
else:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
