#!/usr/bin/python3
for n in range(100):
    if n == 0 or n > 0 and n < 98:
        n = str(n).zfill(2)
        print("{:s}, ".format(str(n).zfill(2)), end="")
print(98)
