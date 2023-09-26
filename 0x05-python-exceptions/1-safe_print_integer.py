#!/usr/bin/python3
def safe_print_integer(value):
    """
    function that prints an integer with "{:d}".format()
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
