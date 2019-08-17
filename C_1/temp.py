# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from operator import eq

a=[[1,2,3],[4,5,6],[7,5,9]]
#print(a)
arr=np.array(a)
print(arr[1][1])
b=np.where(arr==5)
print(b)
search=int(input('Enter the searching number: '))
print(search)

c = 0
for i in range(0,3):
    
    for j in range(0,3):
       #if eq(arr.all,search):
       if arr[i][j]==search:
                print("find out number",arr[i][j],'at (',i,',',j,')')
                c=c+1
                
                
if c<1:
    print('not found')
