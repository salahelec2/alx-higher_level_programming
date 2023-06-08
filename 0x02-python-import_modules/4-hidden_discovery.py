#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)

for nm in names:
    if nm[:2] == "__":
        continue
    else:
        print(nm)
