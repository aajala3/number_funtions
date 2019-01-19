# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:18:27 2019

@author: Adeyemi
"""

#%%
# Afis Ajala
# Department of Phyhsics
# University of Houston, Houston, TX
# This function generates the nth Fibonacci numbers using a numpy array
def fibocalc(n):
    import numpy as np
    fibNum = np.zeros(n+1,dtype=np.int64)
    fibNum[1] = 1
    #count = i + 2
    if (n==1):
        #fibNum.append(fibNum[0] + fibNum[1])        
        #fibNum = fibNum[n]
        result = fibNum[1]
    else:
        for i in range(2,n+1):
            fibNum[i] = fibNum[i-2] + fibNum[i-1]
        result = fibNum[n]      
    return result




