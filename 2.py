# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:40:21 2017

@author: Inspiron
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
x = np.arange(30)-1
plt.plot(x, np.log2(x))
plt.xticks(list(plt.xticks()[0][2:]) + [1])
plt.yticks(list(plt.yticks()[0]) + [1])
plt.xlim(0,10)
