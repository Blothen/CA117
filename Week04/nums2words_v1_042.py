#!/usr/bin/env python3

import sys

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

for num in sys.stdin:
    tokens = num.strip().split()
    output = [num2word[int(n)] for n in tokens]
    print(" ".join(output))
