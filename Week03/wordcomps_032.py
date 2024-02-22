#!/usr/bin/env python3

import sys
line = [l.strip() for l in sys.stdin.readlines()]

def allvowels(w):
    return 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w


def most_es(lines):
    most_e = 0
    words = []
    for item in lines:
        e_count = [c for c in item if c == "e"]
        e_num = len(e_count)
        if e_num > most_e:
            words = words[:0]
            words.append(item)
            most_e = e_num
        if e_num == most_e and item not in words:
            words.append(item)
    return words

avs = [w for w in line if allvowels(w.lower())]
iary_words = [w for w in line if w.endswith("iary")]
print(f"Shortest word containing all vowels: {min(avs, key=len)}")
print(f"Words ending in iary: {len(iary_words)}")
print(f"Words with most e's: {most_es(line)}")
