# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:18:27 2019

@author: Adeyemi
"""


#%%
# Afis Ajala
# Department of Phyhsics
# University of Houston, Houston, TX
# Fibonacci number using a list
def fibocalc_v1(n):
import pandas as pd
import numpy as np
    fibNum = []
    #fibNum.append(0)
    #fibNum.append(1)
    fibNum.append(0)
    fibNum.append(1)    
    #count = i + 2
    if (n==1):
        #fibNum.append(fibNum[0] + fibNum[1])        
        #fibNum = fibNum[n]
        result = fibNum[n]
    else:
        for i in range(2,n+1):
            fibNum.append(fibNum[i-2] + fibNum[i-1])
        result = fibNum[-1]      
    return result

#%%
# Afis Ajala
# Department of Phyhsics
# University of Houston, Houston, TX
# Fibonacci number using a numpy array
def fibocalc_v2(n):
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

#%%
fiboNumStore = fibocalc_v2(100)
fiboNumStore




