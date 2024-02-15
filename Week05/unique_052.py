#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    numbers = [int(t) for t in line.strip().split()]
    uniques = [n for n in numbers if numbers.count(n) == 1]
    #print(f"line = {line}, numbers = {numbers}, Uniques = {uniques}")
    print(max(uniques) if uniques else 'none')
