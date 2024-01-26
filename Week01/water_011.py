#!/usr/bin/env python3

import sys

def fill_buckets(water, buckets):
    filled_buckets = 0
    for bucket in buckets:
        if water >= bucket:
            water -= bucket
            filled_buckets += 1
        else:
            break
    return filled_buckets

water = int(input().strip())
buckets = list(map(int, input().strip().split()))

filled_buckets = fill_buckets(water, buckets)
print(filled_buckets)
