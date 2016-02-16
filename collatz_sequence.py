# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:44:53 2016

@author: ASU_CUDA_LAPTOP
"""

def collatz(value):
    if(value & 1 == 0):
        return value // 2
    else:
        return 3 * value + 1

def stub(value):
    while True:
        value = collatz(value);
        print value    
        if value == 1:
            break

value = input()

try:
    int(value)
except ValueError:
    print "value error"
    exit()
stub(value)