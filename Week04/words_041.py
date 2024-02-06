#!/usr/bin/env python

import sys
import string

words = {}

for line in sys.stdin:
    tokens = line.strip().lower().replace(".", "").replace("?", "").split()
    for word in tokens:
        if word not in words:
            words[word] = 1
        else:
            words[word] = words[word] + 1

for w, c in sorted(words.items()):
    print(f"{w} : {c}")
