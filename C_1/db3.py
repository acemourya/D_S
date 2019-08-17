# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:38:54 2019

@author: Anurag
"""
import os
import numpy as np

# =============================================================================
# files=os.listdir(r"C:\Users\Anurag\Desktop\D_S\class_1\Chatper-01 DataScience Modules-stats-Example")
# print(files)
# for f in files:
#     
#     if f.endswith(".txt"):
#         r=open(r"C:\Users\Anurag\Desktop\D_S\class_1\Chatper-01 DataScience Modules-stats-Example\\"+f)
#         r.read()
#         
#         b=np.where(r=="is")
#         
#         print(b)
#     else:
#         pass
# 
# =============================================================================
    
##

files=os.listdir(r"C:\Users\Anurag\Desktop\D_S\C_1\Chatper-01 DataScience Modules-stats-Example")
print(files)
for f in files:
    
    if f.endswith(".txt"):
        r=open(r"C:\Users\Anurag\Desktop\D_S\C_1\Chatper-01 DataScience Modules-stats-Example\\"+f)
        data =r.readlines()
        print(data)

        for i in range(0,len(data)):
              word = data[i].split()
              print(word)
              for j in range(0,len(word)):
                  if word[j] =='is':
                      print('row no ',i,' position of word ',j)

            
        
        
