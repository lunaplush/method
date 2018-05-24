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
y = np.array( [2,2,2,2,2,2,5,5,9,   13])
y2 = np.array([1,1,1,1,1,1,1,1,13.5,13.5])
y3 = np.array([0.1,0.3,0.3,2.5,2.9,4.2,4,5,6,   6])


def cum(y):
    y_max = y.sum()
    a = 0
    y_cum = np.zeros(N+1)

    for (y_next,i) in zip(y, np.arange(1,N+1)):
        a = a + y_next
        y_cum[i]= a/y_max
    return y_cum
#Gini=[]
#Gini.append(1 - np.sum((X_k - X_k_1) * (Y_k + Y_k_1)))    

def ginny(y):
    
    h = x[1]
    S= h*y[N]/2 + h*y[1:N].sum()
        
    
    return (0.5-S)/0.5

def ginny2(x,y):
    
   
    S = 0
    for i in np.arange(len(x)-1):
        dx = x[i+1]-x[i]
        s = 0.5*dx*(y[i+1]-y[i])+(y[i]*dx)
        S +=s
       
     
    return (0.5-S)/0.5
    
plt.plot(x, cum(y), label ="1, {:.3f}".format(ginny(cum(y))))
#plt.plot(x, cum(y2),label = "1, {}".format(ginny(cum(y2))))
plt.plot(x, cum(y3),label = "1, {:.3f}".format(ginny(cum(y3))))
plt.plot(x,x)   
plt.legend(loc = 'best')

print("Ginny",ginny2(x, cum(y3)))    