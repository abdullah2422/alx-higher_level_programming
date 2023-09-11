#!/usr/bin/python3
# 4. Replace in a copy
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position without modifying """
    my_list = my_list.copy()
    if idx >= 0 and idx <= (len(my_list)):
        my_list[idx] = element
        return (my_list)
