#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    biggest = 0
    for element in my_list:
        if element > biggest:
            biggest = element
    return biggest
