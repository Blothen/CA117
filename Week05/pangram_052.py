#!/usr/bin/env python3

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    for line in sys.stdin:
        missing = [c for c in alphabet if c not in line.strip().lower()]
        missing = ''.join(missing)
        print("missing " + missing if missing else 'pangram')

if __name__ == "__main__":
    main()
