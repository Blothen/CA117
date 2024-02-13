#1!/usr/bin/env python3

import sys

for line in sys.stdin:
    hey = line.strip()
    print(hey[0] + hey[1:-1] * 2 + hey[-1])