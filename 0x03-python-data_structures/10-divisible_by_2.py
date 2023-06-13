#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_new = copy(my_list)
    for k in range(len(my_new)):
        if my_new[k] % 2 == 0:
            return True
        else:
            return False
