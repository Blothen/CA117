#!/usr/bin/env python3

import sys

line = sys.stdin.readline()
pt, pd = [int(t) for t in line.strip().split()]

speeds = []

for line in sys.stdin:
	ct, cd = [int(t) for t in line.strip().split()]
	speed = (cd - pd) / (ct - pt)
	speeds.append(speed)
	pt, pd = ct, cd

print(int(max(speeds)))