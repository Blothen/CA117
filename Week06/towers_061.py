#!/usr/bin/env python3

import sys

values = [int(n.strip()) for n in sys.stdin.readline().split()]

towers = {}
i = 0
while i < len(values):
    towers[i] = [0]
    i += 1


def create_tower(item):
    for k, v in sorted(towers.items()):
        if v[0] == 0:
            towers[k][0] = item
            return
        elif v[-1] >= item:
            towers[k].append(item)
            return
    return

for item in values:
    create_tower(item)

count = 0
for k, v in towers.items():
    if v != [0]:
        count += 1

print(count)
