#! /usr/bin/env python

import re

print 'running...'

str = 'obrien@bobs_pharmacy.com'

print str

replacements = re.compile([\\\&\#\$\%\~\_\^\{\}])

replacements
#	{'\\':"\\\\",
#                  '&':"\&",
#                  '#':"\#",
#                  '$':"\$",
#                   '%':"\%",
#                   '~':'\~',
#                   '_':'\_',
#                   '^':"\^",
#                   '{':'\{',
#                   '}':'\}'
#                   }