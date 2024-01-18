#!/usr/bin/env python3

import sys

for line in sys.stdin:
    text = line.capitalize().strip()
    last_value = text[-1]
    last_value = last_value.swapcase()
    out = text[:-1] + last_value
    print(out)
