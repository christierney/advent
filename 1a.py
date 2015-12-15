#!/usr/bin/env python3
# usage:
# echo $input | ./1a.py
# OR
# ./1a.py input.txt
#
# test with:
# python3 -m doctest 1a.py

import fileinput
import sys

# recursive version blows out the stack
def process1(line, floor=0):
    """Return the final floor number after processing all instructions in floor.

    >>> process1('(())')
    0
    >>> process('()()')
    0
    >>> process('(((')
    3
    >>> process('(()(()(')
    3
    >>> process('))(((((')
    3
    >>> process('())')
    -1
    >>> process('))(')
    -1
    >>> process(')))')
    -3
    >>> process(')())())')
    -3
    """
    if (len(line) == 0): return floor
    elif (line[0] == '('): return process(line[1:], floor+1)
    elif (line[0] == ')'): return process(line[1:], floor-1)
    else: 
        sys.exit('bad input')

# rewritten to avoid recursion
def process(line, floor=0):
    """Return the final floor number after processing all instructions in floor.

    >>> process1('(())')
    0
    >>> process('()()')
    0
    >>> process('(((')
    3
    >>> process('(()(()(')
    3
    >>> process('))(((((')
    3
    >>> process('())')
    -1
    >>> process('))(')
    -1
    >>> process(')))')
    -3
    >>> process(')())())')
    -3
    """
    while True:
        if len(line) == 0: return floor
        elif (line[0] == '('): line, floor = line[1:], floor+1
        elif (line[0] == ')'): line, floor = line[1:], floor-1
        else: sys.exit('bad input')

if __name__ == '__main__':
    for line in fileinput.input():
        print(process(line.strip()))
