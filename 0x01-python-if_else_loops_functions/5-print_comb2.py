#!/usr/bin/python3
for n in range(100):
    if n < 10 and n >= 0:
           print("{:d}{:d}, ".format(0, n), end="")
    elif n > 9 and n < 99:
            print("{:d}, ".format(n), end="")
