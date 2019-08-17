# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:48:31 2019

@author: Anurag
"""
#Q. wap to get the average/mean of one dimenssion array and show values which is greater than average from same array 

import statistics as s
from operator import eq, ge ,le ,ne ,gt


a=[1,3,2,6,7,5,8]
a.sort()

avg1=s.mean(a)

print(avg1)
print(a)

for i in a:
    if ge(i,avg1):
        print(i)
