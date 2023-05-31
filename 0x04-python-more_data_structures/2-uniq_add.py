#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for i, element in enumerate(my_list):
        if i > 0:
            if element not in my_list[:i]:
                result = result + element
        else:
            result = result + element
    return result
