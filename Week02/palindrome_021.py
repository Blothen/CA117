#!/usr/bin/env python3

import sys
import string

def is_palindrome(s):
    return s == s[::-1]

for line in sys.stdin:
    line = line.strip().lower().translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    print(is_palindrome(line))
