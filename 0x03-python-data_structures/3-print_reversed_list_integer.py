#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) == list:
        my_list.reverse()
        for f in my_list:
            if type(f) == int:
                print("{:d}".format(f))