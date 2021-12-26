#!/usr/bin/env python3
# -*- coding: uft-8 -*-

"""my testing module"""

__author__ = 'Bruce'

import sys


def greet():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('Too many arguments')


if __name__ == '__main__':
    greet()
