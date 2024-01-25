#!/usr/bin/env python3

import sys
from math import pi

for line in sys.stdin:
    p = int(line.strip())
    print(f'{pi:.{p:d}f}')
