#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().strip())

visited = {}

i = 0
while i < n:
    item = sys.stdin.readline().strip().split()
    if item[0] in visited:
        visited[item[0]].append(item[1])
    else:
        visited[item[0]] = [item[1]]
    i += 1


check = sys.stdin.readline().strip().split()
out = sorted(visited[check[0]])
print(out[int(check[1]) - 1])
