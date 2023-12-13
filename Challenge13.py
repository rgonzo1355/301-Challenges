#!/usr/bin/python3
# Author:       Rodolfo Gonzalez
# Date:         12-12-23

import requests

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

    # Prompt user to select an HTTP method
    http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
    print("\nChoose an HTTP Method:")
    for index, method in enumerate(http_methods, start=1):
        print(f"{index}: {method}")

    try:
        method_choice = int(input("Enter the number of your chosen HTTP Method: "))
        chosen_method = http_methods[method_choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number for the HTTP Method.")
        return

    print(f"\nYou chose: {chosen_method} method for {description} ({url})")

    # TODO: Implement further functionality based on the chosen HTTP method.
    if chosen_method == "GET":
        perform_get_request(url)
    elif chosen_method == "POST":
        perform_post_request(url)
    elif chosen_method == "PUT":
        perform_put_request(url)
    elif chosen_method == "DELETE":
        perform_delete_request(url)
    elif chosen_method == "HEAD":
        perform_head_request(url)
    elif chosen_method == "PATCH":
        perform_patch_request(url)
    elif chosen_method == "OPTIONS":
        perform_options_request(url)
    else:
        print("Unsupported HTTP method.")

def perform_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Handle the response as needed
        print(f"\nResponse Status Code: {response.status_code}")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Print response content if available
        if response.content:
            print("\nResponse Content:")
            print(response.content.decode())

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# TODO: Implement functions for other HTTP methods (POST, PUT, DELETE, HEAD, PATCH, OPTIONS) as needed.

if __name__ == "__main__":
    main()
