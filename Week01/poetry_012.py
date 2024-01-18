#!/usr/bin/env python3

import sys

data = []
width = 0

for line in sys.stdin:
    data.append(line.strip())
    if len(line) > width:
        width = len(line)

for item in data:
    print(f'{item:^{width -1}}')
