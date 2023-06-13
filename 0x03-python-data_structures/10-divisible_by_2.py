#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ss = []
    my_new = my_list
    for k in range(len(my_new)):
        if my_new[k] % 2 == 0:
            ss.append(True)
        else:
            ss.append(False)
    return ss
