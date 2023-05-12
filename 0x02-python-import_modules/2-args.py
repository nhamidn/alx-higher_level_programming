#!/usr/bin/python3
import sys

if __name__ == "__main__":
    msg = "{:d} argument"
    argc = len(sys.argv) - 1
    if argc == 0:
        msg += 's.'
    elif argc == 1:
        msg += ':'
    else:
        msg += 's:'
    print(msg.format(argc))

    for i, arg in enumerate(sys.argv):
        if i > 0:
           print("{:d}: {:s}".format(i, arg))
