#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from collections import deque
    x = list(sys.argv)
    z = deque(x)
    y = z.popleft()
    g = len(y)
    if g == 0:
        print("0 : argument.")
    elif g == 1:
        print("1  argument:")
        print("{:d} : {:s}".format(g, x[g]))
    else:
        print(g, " arguments:")
        for ff in range(g):
            print("{:d} : {:s}".format((ff), y[ff]))
