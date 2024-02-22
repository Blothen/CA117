#!/usr/bin/env python3

import sys

def non_multiples(num):
    r = range(1, num + 1)
    r = list(r)
    mults3 = [0 if (n % 3 != 0) else n for n in r]
    return str(mults3)

for line in sys.stdin:
    line = line.strip()
    print(f"Non-multiples of 3 replaced: {non_multiples(int(line))}")
