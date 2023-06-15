#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    for ii in range(len(n_list)):
        if n_list[ii] == search:
            del n_list[ii]
            n_list.insert(ii, replace)
    return n_list
