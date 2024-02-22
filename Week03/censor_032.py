#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
args = sys.argv[1]

censor_words = []

with open(args, "r") as f:
    data = f.readlines()
    for line in data:
        censor_words.append(line.strip())

for line in lines:
    line = line.strip()
    for censor in censor_words:
        if censor in line:
            line = line.replace(censor, "@" * len(censor))
    print("".join(line))

