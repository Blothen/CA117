#!/usr/bin/env python3

import sys

def anagram(line):
    tokens = line.split()
    word1 = tokens[0]
    word2 = tokens[1]
    if len(word1) == len(word2):
        sorted_word1 = sorted(word1)
        sorted_word2 = sorted(word2)
        if sorted_word1 == sorted_word2:
            return True
    return False

for line in sys.stdin:
    print(anagram(line.strip().lower()))
