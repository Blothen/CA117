#!/usr/bin/env python3

import sys

line = sys.stdin.readline()
count = int(line.strip())

rejected = 0


for line in sys.stdin:
    line = line.strip()
    if line[0] == "e":
        if int(line[-1]) > count:
            rejected += 1
        else:
            count = count - int(line[-1])
    elif line[0] == "l":
        count = count + int(line[-1])

print(rejected)