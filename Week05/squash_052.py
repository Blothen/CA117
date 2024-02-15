#!/usr/bin/env python3

import sys


def squash_string(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    result.append(str(count) + s[-1])
    return ''.join(result)


if __name__ == "__main__":
    for line in sys.stdin:
        print(squash_string(line.strip()))
