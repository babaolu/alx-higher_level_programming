#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if list(a_dictionary):
        best_val = sorted(a_dictionary.values())[-1]
        for x, y in a_dictionary.items():
            if y == best_val:
                return x
