#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dict = sorted(a_dictionary)
    for key in my_dict:
        value = a_dictionary.get(key)
        print('{}: {}'.format(key, value))
