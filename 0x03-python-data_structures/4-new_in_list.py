#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    lst = []
    for item in my_list:
        lst.append(item)
    if idx >= 0 and idx < len(lst):
        lst[idx] = element
    return lst
