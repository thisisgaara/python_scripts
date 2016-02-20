# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:26:47 2016

@author: ASU_CUDA_LAPTOP
"""

import re

Test_String = raw_input()
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.
match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)