#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    function that prints the first x
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed
    """
    printed_integers = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
    except IndexError:
        pass
    finally:
        print()
    return printed_integers
