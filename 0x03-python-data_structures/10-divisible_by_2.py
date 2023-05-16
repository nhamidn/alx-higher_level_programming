#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    lst = []
    for i in my_list:
        lst.append(True if (i % 2) == 0 else False)
    return lst
