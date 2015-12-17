#!/usr/bin/env python3
# usage:
# echo $input | ./3b.py
# OR
# ./3b.py input.txt
#
# test with:
# python3 -m doctest 3b.py

import fileinput
from collections import defaultdict

def process(line, loca=(0,0), locb=(0,0)):
    """Calculate the number of houses visited.

    >>> process('^v')
    3
    >>> process('^>v<')
    3
    >>> process('^v^v^v^v^v')
    11
    """
    visits=defaultdict(lambda: 0)
    c=0
    while True:
        visits[loca] += 1
        visits[locb] += 1
        c += 1
        if len(line) == 0: return len(visits.keys())
        elif (line[0] == '^'): line, loca, locb = line[1:], (loca[0], loca[1]+(c%2)), (locb[0], locb[1]+(1-(c%2)))
        elif (line[0] == 'v'): line, loca, locb = line[1:], (loca[0], loca[1]-(c%2)), (locb[0], locb[1]-(1-(c%2)))
        elif (line[0] == '>'): line, loca, locb = line[1:], (loca[0]+(c%2), loca[1]), (locb[0]+(1-(c%2)), locb[1])
        elif (line[0] == '<'): line, loca, locb = line[1:], (loca[0]-(c%2), loca[1]), (locb[0]-(1-(c%2)), locb[1])
        else: sys.exit('bad input')

if __name__ == '__main__':
    for line in fileinput.input():
        print(process(line.strip()))
