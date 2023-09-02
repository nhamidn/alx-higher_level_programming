#!/usr/bin/python3
"""Script that takes your GitHub credentials and display id"""
import requests
from sys import argv


if __name__ == "__main__":
    """Program that displays your github id"""
    if len(argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        exit(1)
    username = argv[1]
    token = argv[2]

    url = f"https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}",
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data.get('id'))
        else:
            print("None")
    except requests.RequestException as e:
        print("None")
