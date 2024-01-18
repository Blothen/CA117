#!/usr/bin/env python3

import sys

for line in sys.stdin:
    lines = line.lower().split()
    ll = lines[0]
    lr = lines[1]
    value = True
    checked = []
    for char in ll:
        if char in lr and char not in checked and value != False:
            checked.append(char)
            value = True
        else:
            value = False
    print(value)
