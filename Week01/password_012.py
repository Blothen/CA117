#!/usr/bin/env python3

import sys
special_characters = "!@#$%^&*()-+?_=,<>/"


def check_string(string):
    count = 0
    if any(ch.islower() for ch in string):
        count += 1
    if any(ch.isupper() for ch in string):
        count += 1
    if any(ch.isnumeric() for ch in string):
        count += 1
    if any(ch in special_characters for ch in string):
        count += 1
    return count


for line in sys.stdin:
    print(check_string(line))
