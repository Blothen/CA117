#!/usr/bin/env python3

import sys

file = sys.argv[1]
translation = {}

num2word = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten"
}

with open(file, "r") as f:
    for line in f.readlines():
        tokens = line.strip().split()
        translation[tokens[0]] = tokens[1]

for num in sys.stdin:
    tokens = num.strip().split()
    english = [num2word[int(n)] for n in tokens]
    irish = [translation[n] for n in english]
    print(" ".join(irish))
