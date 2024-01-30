#!/usr/bin/env python3

import sys

seventeen = []
eighteenplus = []
four_letters = []
twoq = []
cie = []
anagrams = []


def acount(string):
    """
    Checks the length of occurring a's in a string and returns the count
    """
    return len([c for c in string if "a" in c])


def qcount(string):
    """
    Checks the length of occuring q's in a string and returns the count
    """
    return len([c for c in string if "q" in c])


def anagram(string, comparison):
    word1 = string
    word2 = comparison
    if len(word1) == len(word2):
        sorted_word1 = sorted(word1)
        sorted_word2 = sorted(word2)
        if sorted_word1 == sorted_word2:
            return True
    return False


for line in sys.stdin:
    line = line.strip()
    lowercase = line.lower()
    if len(line) == 17:
        seventeen.append(line)
    if len(line) >= 18:
        eighteenplus.append(line)
    if acount(lowercase) == 4:
        four_letters.append(line)
    if qcount(lowercase) >= 2:
        twoq.append(line)
    if "cie" in lowercase:
        cie.append(line)
    if anagram(lowercase, "angle") and lowercase != "angle":
        anagrams.append(line)


print(f"Words containing 17 letters: {seventeen}")
print(f"Words containing 18+ letters: {eighteenplus}")
print(f"Words with 4 a's: {four_letters}")
print(f"Words with 2+ q's: {twoq}")
print(f"Words containing cie: {cie}")
print(f"Anagrams of angle: {anagrams}")
