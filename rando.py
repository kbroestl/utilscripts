#! /usr/bin/env python

"""
Module Rando
Create an arbitrary number of passwords of arbitrary length,
Given rando -i=5 -l=8
5 random
8 chars long
"""

import string
import random
import argparse
import itertools

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--iterations", help="Iterations: number of passwords to generate", type=int)
    parser.add_argument("-l", "--length", help="Length: each password should be this long", type=int)
    args = parser.parse_args()
    
    # a little error handling here to make sure that things go right (var types, etc)
    # might be overkill, but wouldn't be amiss.
    if args.iterations:
        i = args.iterations
    else:
        i = 5
    
    if args.length:
        l = args.length
    else:
        l = 6
    
    for _ in itertools.repeat(None, i):
        print ''.join(random.choice(string.ascii_letters + string.digits) for x in range(l))
