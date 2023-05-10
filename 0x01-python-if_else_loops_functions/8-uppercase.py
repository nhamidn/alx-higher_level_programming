#!/usr/bin/python3
def uppercase(str):
    for c in str[:-1]:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    if ord(str[-1]) >= 97 and ord(str[-1]) <= 122:
        print("{}".format(chr(ord(str[-1]) - 32)))
    else:
        print("{}".format(str[-1]))
