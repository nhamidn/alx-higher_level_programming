#!/usr/bin/python3
"""Python script that sends a POST request"""
import urllib.request
from sys import argv, exit


if __name__ == "__main__":
    """Program that sends a POST request to URL email as a parameter"""
    if len(argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        exit(1)

    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
