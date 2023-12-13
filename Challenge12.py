#!/usr/bin/python3
# Author:       Rodolfo Gonzalez
# Date:         12-12-23
import requests


def translate_status_code(status_code):
    """
    Translates HTTP status code to plain terms.
    """
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
    }
    return status_codes.get(status_code, "Unknown Status Code")


def validate_url(url):
    """
    Checks if the URL is valid.
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("Invalid URL format. Please provide a valid URL.")


def validate_method(method):
    """
    Checks if the HTTP method is valid.
    """
    valid_methods = {"GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"}
    if method not in valid_methods:
        raise ValueError(f"Invalid HTTP method: {method}. Available methods: {valid_methods}")


def main():
    # Prompt user for URL and HTTP Method
    try:
        url = input("Enter the destination URL: ")
        validate_url(url)
        http_method = input(
            "Choose HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): "
        ).upper()
        validate_method(http_method)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Confirm request with user
    print(f"\nSending {http_method} request to: {url}")
    confirmation = input("Do you want to proceed? (yes/no): ").lower()

    if confirmation != "yes":
        print("Operation aborted.")
        return

    # Perform HTTP request and handle exceptions
    try:
        # Handle methods with request body
        if http_method in {"POST", "PUT", "PATCH"}:
            request_body = input("Enter request body (optional): ")
            response = requests.request(http_method, url, data=request_body)
        else:
            response = requests.request(http_method, url)

        response.raise_for_status()

        # Print response information
        print(f"\nResponse Status: {translate_status_code(response.status_code)}")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        # Print response content if available
        if response.content:
            print("\nResponse Content:")
            print(response.content.decode())

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
