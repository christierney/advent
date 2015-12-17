#!/usr/bin/env python3
# usage:
# echo $input | ./2b.py
# OR
# ./2b.py input.txt
#
# test with:
# python3 -m doctest 2b.py

import fileinput
import functools
import itertools
import operator
import sys

def process(i):
    return sum((ribbon(line) for line in i))

def ribbon(line):
    """Calculate the ribbon required for a single present.

    >>> ribbon('2x3x4')
    34
    >>> ribbon('1x1x10')
    14
    """
    sides = [int(x) for x in line.split("x")]
    return sum(sorted(sides)[:-1] * 2) + functools.reduce(operator.mul, sides, 1)

if __name__ == '__main__':
    print(process(fileinput.input()))
