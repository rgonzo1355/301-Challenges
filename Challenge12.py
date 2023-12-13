#!/usr/bin/python3
# Author:       Rodolfo Gonzalez
# Date:         12-12-23

def main():
    """
    This script allows users to choose a predefined URL and perform an HTTP request.
    """

    # Define predefined URLs with descriptive names and URLs
    predefined_urls = {
        1: ("Example Domain - This is a basic example website.", "https://www.example.com"),
        2: ("Google Search - The world's most popular search engine.", "https://www.google.com"),
        3: ("GitHub - A popular code hosting platform for developers.", "https://www.github.com"),
    }

    # Display menu with numbered options and descriptions
    print("Choose a predefined URL:")
    for index, (name, url) in enumerate(predefined_urls.items()):
        print(f"{index + 1}: {name}")
        print(f"\t- {url}")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a valid number.")
        return

    # Validate chosen URL and extract URL based on the choice
    if choice not in range(1, len(predefined_urls) + 1):
        print("Invalid choice. Please enter a number within the available range.")
        return

    url, description = predefined_urls[choice - 1]

    # TODO: Implement further functionality like choosing HTTP method, handling requests and responses, etc.

    print(f"You chose: {description} ({url})")

    # ...


if __name__ == "__main__":
    main()

