#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        my_list.remove(idx)
    return my_list
