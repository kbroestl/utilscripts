#! /usr/bin/env python

import re
import string
import random

to_test = ['pgBwnVae',
'5vpk5M4H',
'rj0ZFNOo',
'7P4hKyj2',
'R811gZpW',
'4QubLOdG',
'JKDANZbL',
'Z2TFrOso',
'QqGm4VHe',
'ozFAdVQm']

cap_re = re.compile('[A-Z]*')
num_re = re.compile('\d')

for entry in to_test:
  if ( re.search(cap_re, entry) and re.search(num_re, entry) ):
    print "%s passes both tests" % entry
