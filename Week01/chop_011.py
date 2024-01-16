#!/usr/bin/env python3
import sys

s = sys.stdin.read().split()

i = 0
while i < len(s):
    word = s[i]
    print(word[1:-1])
    i += 1
