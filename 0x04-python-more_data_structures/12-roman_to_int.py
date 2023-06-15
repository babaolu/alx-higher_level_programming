#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    trans_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}
    total_val = 0
    current_val = 10000
    inter_val = 0
    for letter in roman_string:
        if letter not in trans_map.keys():
            return 0
        if trans_map[letter] > current_val:
            inter_val = trans_map[letter] - inter_val
            current_val = trans_map[letter]
        else:
            total_val += inter_val
            inter_val = current_val = trans_map[letter]
    total_val += inter_val
    return total_val
