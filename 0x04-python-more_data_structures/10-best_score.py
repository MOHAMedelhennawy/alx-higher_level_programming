#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        return max(a_dictionary.keys())
