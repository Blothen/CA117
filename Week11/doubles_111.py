#!/usr/bin/env python3

import sys

double = {}

vowels = ["aa", "ee", "ii", "oo", "uu"]

for line in sys.stdin:
    line = line.strip()
    for v in vowels:
        if v in line.lower():
            double[line] = line.count(v)

word = ""
max = 0
for k,v in double.items():
    if v > max:
        max = v
        word = k

print(k)