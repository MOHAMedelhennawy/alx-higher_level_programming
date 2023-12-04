#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        my_list.remove(idx + 1)
        # or: del my_list[idx]
    return my_list
