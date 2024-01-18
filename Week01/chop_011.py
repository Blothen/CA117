#!/usr/bin/env python3
import sys

for item in sys.stdin:
    line = item[1:-1 - 1]
    if len(line) > 0:
        print(line.strip())
