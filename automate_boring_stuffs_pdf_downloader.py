# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:00:01 2016

@author: Vignesh_kannan
Purpose: Download the pages from automate boring stuffs with python and store as pdf book
"""

import pprint
string = "It was a bright cold day in April, and the clocks were striking \
thirteen."
count = {}
for char in string:
    count.setdefault(char, 0);
    count[char] = count[char] + 1;

temp = str(pprint.pformat(count));
print temp