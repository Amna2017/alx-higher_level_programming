#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = list(set(my_list))
    xd = 0
    for i in range(len(unique_numbers)):
        xd = xd + unique_numbers[i]
    return xd
