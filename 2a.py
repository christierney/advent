#!/usr/bin/env python3
# usage:
# echo $input | ./2a.py
# OR
# ./2a.py input.txt
#
# test with:
# python3 -m doctest 2a.py

import fileinput
import itertools
import sys

def process(i):
    return sum((paper(line) for line in i))

def paper(line):
    """Calculate the surface area of a box with dimensions axbxc,
    plus the area of the smallest side.

    >>> paper('2x3x4')
    58
    >>> paper('1x1x10')
    43
    """
    a = areas(line)
    return sum(a * 2 + [min(a)])

def areas(dim):
    """Returns a list of areas for a dimension string.

    >>> areas('2x3x4')
    [6, 8, 12]
    >>> areas('1x1x10')
    [1, 10, 10]
    """
    return [ x*y for x,y in
        itertools.combinations(
            (int(x) for x in dim.split("x")), 2
        )
    ]

if __name__ == '__main__':
    print(process(fileinput.input()))
