#!/usr/bin/python3
for n in range(100):
    if n == 0 or n > 0 and n < 99:
        m = str(n)
        n = m.zfill(2)
        print("{:s}, ".format(n), end="")
print(99)
