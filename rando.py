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
import re

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
        i = 10
    
    if args.length:
        l = args.length
    else:
        l = 8
    
    # for _ in itertools.repeat(None, i):
    #     print ''.join(random.choice(string.ascii_letters + string.digits) for x in range(l))
# passwords must have at least one uppercase
# and at least one digit

cap_re = re.compile('[A-Z]*')
num_re = re.compile('\d')

c = 1
while c < i:
    pwd = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(l))
    if (re.search(cap_re, pwd) and re.search(num_re, pwd)):
        print pwd
        c += 1
