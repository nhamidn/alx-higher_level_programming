#!/usr/bin/python3
"""Python script that print HTTP status code of a request"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """Program that print HTTP status code of a request"""
    if len(argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        exit(1)

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
