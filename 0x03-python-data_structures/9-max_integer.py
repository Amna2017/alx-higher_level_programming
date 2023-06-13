#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for k in range(len(my_list)):
            if my_list[k] > my_list[k+1]:
                return my_list[k]
            else:
                return my_list[k+1]
