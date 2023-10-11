#!/usr/bin/python3
"""Save argument to a file."""
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_arguments_to_list_and_save(arguments):
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(arguments)

    save_to_json_file(existing_list, "add_item.json")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_arguments_to_list_and_save(arguments)
