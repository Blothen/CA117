#!/usr/bin/env python3

import sys

for line in sys.stdin:
    n = line.strip()
    n = int(n)
    primes = []
    for num in range(0, n + 1):
        if num > 1:
            r = range(2, num)
            for i in r:
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    print(f"Primes: {primes}")
