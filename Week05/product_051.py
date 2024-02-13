#!/usr/bin/env python3

import sys

def recursion(numss):
    num = str(numss)
    n = int(num)
    if n <= 9:
        return n
    number = ""
    for item in num:
        if item != "0":
            number = number + item
    nums = [int(c) for c in number]
    product = 1
    for item in nums:
        product *= item
    return recursion(product)
    
def main():
    num = sys.stdin.readline().strip()
    print(recursion(num))
    
if __name__ == "__main__":
    main()