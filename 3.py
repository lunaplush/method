# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:07:52 2017

@author: Inspiron
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
import mpl_toolkits as mpl_tl
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


#%%
#data prepare
os.chdir("c:\\Luna\\Work\\python\\methodology\\")
file  = "data.xlsx"
dataf = pd.ExcelFile(file)
auto1 = dataf.parse(sheetname = "авто", skiprows = [0,1], parse_cols = "A:D", skip_footer = 17, names = ["left","right","weight","num"])
auto2 = dataf.parse(sheetname = "авто", skiprows = np.arange(28), parse_cols ="A:D", skip_footer = 0, names = ["left","right","weight","num"])
#%%
def calculate_data(df):
    df["middle"]=0.5*(df.left+df.right)
    #df["cena"] = df.num*df.middle
    #sum_cena = np.sum(df.cena)
    max_cena= df.right.iloc[-1]
    df["cena_relative_right"] = df.right/max_cena*100
    df["cena_relative"] = df.middle/max_cena*100
    sum_num = np.sum(df.num)   
    df["num_relative"] = df.num/sum_num*100
    return df
#%%

_ = calculate_data(auto1)
_ = calculate_data(auto2)
#%%
fig, ax = plt.subplots()

#plt.scatter(auto1.cena_relative, auto1.num_relative, marker = "v", color="k" )
ax.plot(auto1.cena_relative, auto1.num_relative, marker = "*", color="k" )

ax.plot(auto2.cena_relative, auto2.num_relative, marker = "o", color="k" )

ax.set_xlim(0,100)
ax.set_ylim(0,40)
#ax.set_xticks([0]+auto1.cena_relative_right)
ax.set_xticks(np.arange(101,step = 20))
#plt.ticks_params

#vals = ax.get_xticks()
#ax.set_xticklabels(['{:3.2f}%'.format(x*100) for x in list([vals[0]])+vals[-3]])
ax.set_xticklabels(['{:3.0f}%'.format(x) for x in np.arange(101,step = 20)])

#ax.set_xticklabels(['' for x in vals[1:-3]])
#plt.show()

ax2 = mpl_il.inset_axes(plt.gca(), width='80%', height='80%', loc=1)
ax2.plot(auto1.cena_relative, auto1.num_relative, marker = "*", color="k" )

ax2.plot(auto2.cena_relative, auto2.num_relative, marker = "o", color="k" )


ax2.set_xlim(0,2)
ax2.set_ylim(0,40)
#ax2.set_xticks(np.arange(2.1,step = 0.1 ))
#ax2.set_xticklabels(['{:3.0f}%'.format(x) for x in np.arange(2.1,step = 0.1)])
for l in ax2.get_xticklabels():
    print(l)
#ax2.set_xticks([0]+auto1.cena_relative_right)
#ax2.margins(x=0.5)

mark_inset(ax,ax2,loc1 = 2, loc2 = 3, fc = "none")
plt.show()
#%%
#plt.figure()
#plt.bar(np.arange(10), height = np.arange(10))