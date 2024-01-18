#!/usr/bin/env python3

import sys

for line in sys.stdin:
    done = False
    lines = line.split()
    i = 0
    while i < len(lines):
        if lines[i][0] == "m" and not done:
            caps = lines[i].capitalize()
            done = True
            lines[i] = caps
        i += 1
    print(" ".join(lines))
