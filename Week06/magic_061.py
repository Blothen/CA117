#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().strip())

def added(n):
    s = str(n)
    total = 0
    for item in s:
        total += int(item)
    return total

def magic(n, n1=added(n)):
    if n % n1 == 0:
        return n
    elif n == 25:
        return 27
    else:
        return magic(n + 1)

print(magic(n))
