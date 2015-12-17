#!/usr/bin/env python3
# usage:
# echo $input | ./3a.py
# OR
# ./3a.py input.txt
#
# test with:
# python3 -m doctest 3a.py

import fileinput
from collections import defaultdict

def process(line, loc=(0,0)):
    """Calculate the number of houses visited.

    >>> process('>')
    2
    >>> process('^>v<')
    4
    >>> process('^v^v^v^v^v')
    2
    """
    visits=defaultdict(lambda: 0)
    while True:
        visits[loc] += 1
        if len(line) == 0: return len(visits.keys())
        elif (line[0] == '^'): line, loc = line[1:], (loc[0], loc[1]+1)
        elif (line[0] == 'v'): line, loc = line[1:], (loc[0], loc[1]-1)
        elif (line[0] == '>'): line, loc = line[1:], (loc[0]+1, loc[1])
        elif (line[0] == '<'): line, loc = line[1:], (loc[0]-1, loc[1])
        else: sys.exit('bad input')

if __name__ == '__main__':
    for line in fileinput.input():
        print(process(line.strip()))
