#!/usr/bin/env python3

import sys

for line in sys.stdin:
    if len(line) % 2 != 0:
        print("No middle character!")
    else:
        out = line[len(line) // 2 - 1]
        print(out)
