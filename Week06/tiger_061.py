#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    i = 0
    while i < len(line) and line[i] == "|":
        i += 1
    left = line[:i]
    while i < len(line) and line[i] != "|":
        i += 1
    exclude = i
    right = line[i:]
    if len(left) != len(right):
        print("unsafe")
    else:
        print("safe")
