#!/usr/bin/env python3

import sys


def swap_cups(start_position, swaps):
    pos = start_position
    for swap in swaps:
        if swap == "A":
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif swap == "B":
            if pos == 2:
                pos = 3
            elif pos == 3:
                pos = 2
        elif swap == "C":
            if pos == 1:
                pos == 3
            elif pos == 3:
                pos = 1
    return pos

def main():
    start_position = int(sys.stdin.readline().strip())
    swaps = sys.stdin.readline().strip()
    final_pos = swap_cups(start_position, swaps)
    print(final_pos)

if __name__ == "__main__":
    main()
