#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = 0
flag = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            flag = 0
            break
    if flag == 1: # most important 
        print '%-4d' % m
        num = num +1
    flag = 1
print 'The total is %d' % num
