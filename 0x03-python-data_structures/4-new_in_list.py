#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < 0 or idx >= len(new):
        return new
    else:
        del new[idx]
        new.insert(idx, element)
        return new
