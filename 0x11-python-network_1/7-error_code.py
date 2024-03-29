#!/usr/bin/python3
"""Python script that print HTTP status code of a request"""
import sys
import requests


if __name__ == "__main__":
    """Program that print HTTP status code of a request"""
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
