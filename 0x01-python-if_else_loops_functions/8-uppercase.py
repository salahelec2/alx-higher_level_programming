#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            uppercase_c = chr(ord(c) & ~32)
            uppercase_str += uppercase_c
        else:
            uppercase_str += c

    print("{0}\n".format(uppercase_str), end="")
