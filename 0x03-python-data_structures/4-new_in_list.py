#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    lst = []
    for element in my_list:
        lst.append(element)
    if idx >= 0 and idx < len(lst):
        lst = element
    return lst
