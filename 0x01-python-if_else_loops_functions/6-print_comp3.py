#!/usr/bin/python3
for amna in range(99):
    if amna == 0 or amna > 0 and amna < 98:
        amna = str(amna).zfill(2)
        print("{:s}, ".format(amna), end="")
print("98")
