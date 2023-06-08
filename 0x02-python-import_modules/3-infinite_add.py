#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1

    if num_args != 0:
        added = 0
        for arg in argv[1:]:
            added += int(arg)
        print(added)

    else:
        print(0)

