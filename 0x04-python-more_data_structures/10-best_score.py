#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_score = list(a_dictionary.keys())[0]
        for key, value in a_dictionary.items():
            if  a_dictionary[key] > a_dictionary[max_score]:
                max_score = key
        return max_score
