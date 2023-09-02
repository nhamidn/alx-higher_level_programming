#!/usr/bin/python3
"""Script that Sends a POST request with post param"""
import sys
import requests


if __name__ == "__main__":
    """Program that sends a POST request to URL email as a parameter"""
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
