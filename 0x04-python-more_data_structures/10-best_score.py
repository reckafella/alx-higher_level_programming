#!/usr/bin/python3

def best_score(a_dictionary):
    if (not a_dictionary):
        return None
    else:
        max_value = max(a_dictionary.values(), key=lambda x: x)
        for key, val in a_dictionary.items():
            if val == max_value:
                return key
        return None
