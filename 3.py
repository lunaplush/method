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
#os.chdir("c:\\Luna\\Work\\python\\method\\")
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
    df["cena_relative_left"] = df.left/max_cena*100
    df["cena_relative_weight"] =   df["cena_relative_right"]-  df["cena_relative_left"]
    df["cena_relative"] = df.middle/max_cena*100
    sum_num = np.sum(df.num)   
    df["num_relative"] = df.num/sum_num*100
    return df
#%%

_ = calculate_data(auto1)
_ = calculate_data(auto2)
#%%
#plt.style.use("seaborn-pastel")
#plt.style.use("grayscale")


fig, ax = plt.subplots()

fig.set_facecolor("w")
fig.set_frameon(True)

#plt.scatter(auto1.cena_relative, auto1.num_relative, marker = "v", color="k" )
ax.plot(auto1.cena_relative, auto1.num_relative, marker = "*", color="k" )

ax.plot(auto2.cena_relative, auto2.num_relative, marker = "o", color="k" )

ax.set_xlim(0,100)
ax.set_ylim(0,40)
#ax.set_xticks([0]+auto1.cena_relative_right)
ax.set_xticks(np.arange(101,step = 20))
#plt.ticks_params

y_vals = ax.get_yticks()
ax.set_yticklabels(['{:3.0f}%'.format(x) for x in y_vals])

x_vals = ax.get_xticks()
ax.set_xticklabels(['{:3.0f}%'.format(x) for x in x_vals])
ax.tick_params(axis = 'both', bottom = "on")
ax.grid(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)
ax.axhline()
ax.axvline()

plt.xlabel("Относительная цена автомобиля")
plt.ylabel("Доля автомобилей с данной ценой")
#ax.set_xticklabels(['' for x in vals[1:-3]])
#plt.show()

ax2 = mpl_il.inset_axes(plt.gca(), width='80%', height='80%', loc=1, borderpad = 1)

ax2.plot(auto2.cena_relative, auto2.num_relative, marker = "o", color="k", label ="15 когорт" )
ax2.plot(auto1.cena_relative, auto1.num_relative, marker = "*", color="k" , ms =8, label = "24 когорты")


ax2.set_xlim(0,2.02)
ax2.set_ylim(0,40)
ax2.grid(b="on",axis ="both", linestyle='dashed', linewidth = 1, color = "grey")

bar2 = ax2.bar(left = auto2.cena_relative_left, width = auto2.cena_relative_weight, height = auto2.num_relative, color = (0.5,0.5,0.5))
bar1 = ax2.bar(left = auto1.cena_relative_left, width = auto1.cena_relative_weight, height = auto1.num_relative,color = (0.75,0.75,0.75), alpha=0.5)


y_vals = ax2.get_yticks()
ax2.set_yticklabels(['{:3.0f}%'.format(x) for x in y_vals])

x_vals = ax2.get_xticks()
ax2.set_xticklabels(['{:3.1f}%'.format(x) for x in x_vals])
ax2.legend()
#ax2.set_xticks([0]+auto1.cena_relative_right)
#ax2.margins(x=0.5)

#mark_inset(ax,ax2,loc1 = 2, loc2 = 3, fc = "none", linestyle = ":")
#ax.semilogx()
#plt.xscale("log")

#.xscale("log")


plt.savefig("5.jpg")
plt.savefig("5.png")
#%%
#plt.figure()
#plt.bar(np.arange(10), height = np.arange(10))

#tty = np.random.rand(10)
#ttx =  np.linspace(0,10,10)
#fig1, ax1 = plt.subplots()
#plt.plot(ttx,tty)
#fig1.set_facecolor("w")
#fig1.set_frameon(False)
#ax1.set_axis_on()
#ax1.grid(False)
#ax1.spines["left"].set_position('center')
#ax1.spines["left"].set_visible(True)
