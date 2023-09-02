#!/usr/bin/python3
"""Python script that displays the value of X-Request-Id variable"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """Program that gets the value of X-Request-Id from a request"""
    with urllib.request.urlopen(argv[1]) as response:
        request_id = response.info().get('X-Request-Id')
        print(request_id)
