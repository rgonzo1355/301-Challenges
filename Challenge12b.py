#!/usr/bin/python3

import requests

def translate_status_code(code):
    status_codes = {
        200: "Success",
        201: "Created",
        202: "Accepted",
        204: "No Content",
        301: "Moved Permanently",
        302: "Found",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Site not found",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout"
    }
    return status_codes.get(code, f"Unknown Status Code: {code}")

def get_http_method():
    methods = {
        "1": "GET",
        "2": "POST",
        "3": "PUT",
        "4": "DELETE",
        "5": "HEAD",
        "6": "PATCH",
        "7": "OPTIONS"
    }
    print("\nSelect a HTTP Method:")
    print("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. HEAD\n6. PATCH\n7. OPTIONS")
    choice = input("Your choice (1-7): ")
    return methods.get(choice, "GET")

def add_schema_if_missing(url):
    if not url.startswith(('http://', 'https://')):
        return f'http://{url}'
    return url

def main():
    url = input("Enter the destination URL: ")
    url = add_schema_if_missing(url)
    selected_method = get_http_method()

    print(f"\nHTTP Method: {selected_method}")
    print(f"Destination URL: {url}")
    confirmation = input("Confirm request? (yes/no): ")

    if confirmation.lower() != "yes":
        print("Request cancelled.")
        return

    response = requests.request(selected_method, url)

    print(f"\nResponse Status: {response.status_code} ({translate_status_code(response.status_code)})")
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()


