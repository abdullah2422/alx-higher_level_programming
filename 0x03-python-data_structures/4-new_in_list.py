#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx >= (len(my_list)):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
