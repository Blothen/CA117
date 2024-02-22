#!/usr/bin/env python3

import sys

values = sys.stdin.readline().split()
order = sys.stdin.readline().strip()

order_trans = {
    "A":"0",
    "B":"1",
    "C":"2"
}
nums = []
output = ""
for item in values:
    nums.append(int(item))

nums.sort()

for item in order:
    value = int(order_trans[item])
    output = output + " " + str(nums[value])

print(output.lstrip())
