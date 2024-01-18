#!/usr/bin/env python3

import sys

for line in sys.stdin:
    lines = line.lower().split()
    ll = lines[0]
    lr = lines[1]
    if ll in lr:
        print("True")
    else:
        print("False")
