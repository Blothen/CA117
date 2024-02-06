#!/usr/bin/env python3

import sys

vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

def tagger(item):
    return item[1]

for line in sys.stdin:
    line = line.lower().strip()
    tokens = line.split()
    for item in tokens:
        for char in item:
            if char in vowels:
                vowels[char] = vowels[char] + 1

max = 0
for k, v in sorted(vowels.items(), reverse=True, key=tagger):
    if len(str(v)) >= max:
        max = len(str(v))
    print(f"{k} : {v:{max}}")
