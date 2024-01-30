#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def multiples(nums):
    r = range(1, nums + 1)
    r = list(r)
    mult3 = [n for n in r if n % 3 == 0]
    multi3 = [(n ** 2) for n in r if n % 3 == 0]
    mult4 = [(n * 2) for n in r if n % 4 == 0]
    mult3and4 = [n for n in r if n % 3 == 0 or n % 4 == 0]
    mult3or4 = [n for n in r if n % 3 == 0 and n % 4 == 0]
    print("Multiples of 3:", str(mult3))
    print("Multiples of 3 squared:", str(multi3))
    print("Multiples of 4 doubled:", str(mult4))
    print("Multiples of 3 or 4:", str(mult3and4))
    print("Multiples of 3 and 4:", str(mult3or4))

for line in lines:
    line = line.strip()
    multiples(int(line))
