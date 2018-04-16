# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:12:45 2018

@author: Luna
"""

#Лоренц Джинни

import numpy as np
import matplotlib.pyplot as plt
N = 10
x = np.arange(0,N+1,1)
x = x/N
y = np.array( [2,2,2,2,2,5,5,5,5,   5])
y2 = np.array([1,1,1,1,1,1,1,1,13.5,13.5])
y3 = np.array([1,1,2,3,4,4,4,5,5,   6])
y_max = y.sum()


def cum(y):
    a = 0
    y_cum = np.zeros(N+1)

    for (y_next,i) in zip(y, np.arange(1,N+1)):
        a = a + y_next
        y_cum[i]= a/y_max
    return y_cum
#Gini=[]
#Gini.append(1 - np.sum((X_k - X_k_1) * (Y_k + Y_k_1)))    

def ginny(y):
    y2 = np.zeros(N)
    for i in np.arange(1,N):
        y2[i] = y[i]
    print(list(zip(y,y2)))
    return 1- np.sum((y2+y))
    
plt.plot(x, cum(y), label =ginny(y))
plt.plot(x, cum(y2),label =ginny(y2))
plt.plot(x, cum(y3),label =ginny(y3))
plt.plot(x,x)   
plt.legend(loc = 'best')


    