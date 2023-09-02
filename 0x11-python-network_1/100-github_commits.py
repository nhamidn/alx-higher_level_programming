#!/usr/bin/python3
"""Script that lists 10 commits of the repository rails"""
import requests
from sys import argv


if __name__ == "__main__":
    """Program that lists 10 commits of the repository"""
    if len(argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner>")
        exit(1)
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    result = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(result[i].get('sha'), result[i].
                                  get('commit').get('author').get('name')))
    except IndexError:
        pass
