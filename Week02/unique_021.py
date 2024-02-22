#!/usr/bin/env python3

import sys
import string

data = []
count = []

for line in sys.stdin:
    data.append(line.strip().lower().translate(str.maketrans('', '', string.punctuation)).split())

data.sort()

for line in data:
    for s in line:
        if s not in count:
            count.append(s)

print(len(count))
