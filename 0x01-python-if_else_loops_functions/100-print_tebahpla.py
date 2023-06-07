#!/usr/bin/python3
for i in range(1, 27, 2):
    print("{1}{0}".format(chr(90 - i), chr(122 - i + 1)), end="")
