#!/usr/bin/python3
def best_score(a_dictionary):
    big_key = None
    big_value = 0
    if a_dictionary is not None:
        for key in a_dictionary.keys():
            if a_dictionary[key] > big_value:
                big_key = key
                big_value = a_dictionary[key]
    return big_key
