#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        uppercase_c = chr(ord(c) & ~32)
        uppercase_str += uppercase_c

    print("{0}\n".format(uppercase_str), end="")
