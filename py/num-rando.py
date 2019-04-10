#! /usr/bin/env python

"""
Module Rando-number
Create an arbitrary number of random phone-numbers,
Given rando -i=5
5 random numbers, formatted as (123) 456-7890

"""

import string
import random
import argparse
import itertools

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--iterations", help="Iterations: number of passwords to generate", type=int)
    # parser.add_argument("-l", "--length", help="Length: each password should be this long", type=int)
    args = parser.parse_args()
    
    # a little error handling here to make sure that things go right (var types, etc)
    # might be overkill, but wouldn't be amiss.
    if args.iterations:
        i = args.iterations
    else:
        i = 5
       
    for _ in itertools.repeat(None, i):
        phnum = '(%s) %s-%s' % ( ''.join(random.choice( string.digits ) for x in range(3)), ''.join(random.choice( string.digits ) for x in range(3)), ''.join(random.choice( string.digits ) for x in range(4)))
        print phnum
