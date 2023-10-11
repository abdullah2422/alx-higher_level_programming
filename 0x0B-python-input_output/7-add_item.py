import sys
import json

# Function to save a Python object to a JSON file
def save_to_json_file(filename, my_obj):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

# Function to load a Python object from a JSON file
def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Check if there are command-line arguments
if len(sys.argv) > 1:
    # Load the existing list from the file if it exists, or initialize an empty list
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    # Add the command-line arguments to the list
    arguments = sys.argv[1:]
    existing_list.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file('add_item.json', existing_list)
else:
    print("No arguments provided. Usage: python add_items_to_json.py <item1> <item2> ...")


