#!/usr/bin/python3
"""Python script that displays the value of X-Request-Id variable"""
import sys
import requests


if __name__ == "__main__":
    """Program that gets the value of X-Request-Id from a request"""
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
