#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

# Usage in your script:
if __name__ == '__main__':
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
