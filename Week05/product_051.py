#!/usr/bin/env python3

import sys

def recursion(num):
    numstr = str(num)
    n = int(num)
    if n <= 9:
        return n
    nums = [int(c) for c in numstr if c != "0"]
    product = 1
    for item in nums:
        product *= item
    return recursion(product)
    
def main():
    num = sys.stdin.readline().strip()
    print(recursion(num))
    
if __name__ == "__main__":
    main()
