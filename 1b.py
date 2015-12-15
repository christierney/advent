#!/usr/bin/env python3
# usage:
# echo $input | ./1b.py
# OR
# ./1b.py input.txt
#
# test with:
# python3 -m doctest 1b.py

import fileinput
import sys

def process(line, floor=0, pos=0):
    """Return the position of the first character ine line that causes floor to become negative.

    >>> process(')')
    1
    >>> process('()())')
    5
    """
    while True:
        if (floor == -1): return pos
        if len(line) == 0: sys.exit('never entered basement')
        elif (line[0] == '('): line, floor, pos = line[1:], floor+1, pos+1
        elif (line[0] == ')'): line, floor, pos = line[1:], floor-1, pos+1
        else: sys.exit('bad input')

if __name__ == '__main__':
    for line in fileinput.input():
        print(process(line.strip()))
