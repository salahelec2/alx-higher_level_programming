#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1
print(
    "{} {}{}".format(
        num_args,
        "argument :" if num_args == 1 else "arguments",
        "." if num_args == 0 else ":",
    )
)
if num_args != 0:
    n=0
    for arg in argv[1:]:
        print("{}: {}".format((n := n + 1), arg))
