#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    my_list = my_list.copy()
    if idx < 0 and idx >= (len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
