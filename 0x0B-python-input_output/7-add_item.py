#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Function to add items to the list and save it to a JSON file
def add_items_to_list_and_save(args):
    try:
        # Try to load an existing list from the file
        my_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list
        my_list = []

    # Add the provided arguments to the list
    my_list.extend(args)

    # Save the updated list to the JSON file
    save_to_json_file('add_item.json', my_list)

if __name__ == "__main__":
    # Remove the script name (first argument)
    args = sys.argv[1:]

    if args:
        add_items_to_list_and_save(args)
