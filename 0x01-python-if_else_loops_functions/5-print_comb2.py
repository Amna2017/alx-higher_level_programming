#!/usr/bin/python3
for n in range(100):
    if n >= 0 and n < 99:
        n = str(n)
        n = n.zfill(2)
        print("{:s}, ".format(n),end="")
print(99)
