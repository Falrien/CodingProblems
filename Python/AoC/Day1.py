#!/usr/bin/python3
import bisect
import math
import sys
from sys import stdin


def solve():
    f = open('input.txt', 'r')
    curr_sum = 0
    calorie_count = []
    for line in f:
        if line == '\n':
            calorie_count.append(curr_sum)
            curr_sum = 0
            continue
        curr_sum += int(line)
    calorie_count.sort(reverse=True)
    print(sum(calorie_count[0:3]))

if __name__ == '__main__':
    solve()
