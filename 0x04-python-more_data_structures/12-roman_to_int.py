#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
    result = 0
    dict_len = len(roman_string) - 1

    while dict_len > -1:
        if dict_len < (len(roman_string) - 1) \
                and my_dict[roman_string[dict_len]] \
                < my_dict[roman_string[dict_len + 1]] \
                and roman_string[dict_len] == "I":
            result -= my_dict[roman_string[dict_len]]
        else:
            result += my_dict[roman_string[dict_len]]
        dict_len -= 1
    return result
