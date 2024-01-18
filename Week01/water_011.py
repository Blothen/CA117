#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

value = int(s[0].strip())
remaining = 0
buckets = "".join(s[1:]).strip()

for bucket in buckets:
    if int(bucket) // value > 0:
        remaining = int(bucket) % value
    else:
        print(remaining)
