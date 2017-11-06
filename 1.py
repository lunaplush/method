# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 16:34:30 2017

@author: Inspiron
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as skl

#%%
max_d = 565676666
file =  "data.xlsx"
xfile = pd.ExcelFile(file)

rosstat = xfile.parse(sheetname = "Росстат", skiprows = [0,1], parse_cols = "B:E" ,skip_footer = 40, names = ['a','b','c','d'])
row_index = rosstat.index == 7 
rosstat.loc[row_index,'a'] = 45000
rosstat.loc[row_index,'b'] = max_d #np.nan
rosstat.loc[row_index,'c'] = np.nan

#%%
plt.figure()
rosstat_x = np.array([])
rosstat_y = np.array([])
j = 0
integral = 0
for i in np.arange(len(rosstat['a'])):
    rosstat_x.resize(len(rosstat_x) + 2)
    rosstat_x.put(j,rosstat['a'].iloc[i] / max_d)
    
    rosstat_x.put(j+1,rosstat['b'].iloc[i] / max_d)
    rosstat_y.resize(len(rosstat_y) + 2)
    dif = rosstat['b'].iloc[i] - rosstat['a'].iloc[i]
    rosstat_y.put(j,rosstat['d'].iloc[i]/ dif)
    rosstat_y.put(j+1,rosstat['d'].iloc[i]/dif)
    integral =  integral + rosstat['d'].iloc[i]
    j = j+2
plt.title("Функция плотности распределени для данных Росстат ") 
#plt.xlim(0,0.00002)   
plt.ylabel("Доля населения")
plt.xlabel("Относительный доход населения (в долях от максимального)")  
#plt.xlabel("Доход населения (рос.руб.)")      
plt.plot(rosstat_x,rosstat_y)
plt.savefig("rosstat_max_otnositeln.jpg")
#%%
plt.figure()
forbs = xfile.parse(sheetname = "Форбс", skiprows = [0,1,2], parse_cols = "C:E",skip_footer = 1, names = ['a','b','c'])
bins = [132500, 862500, 3032500, 7215000, 10692500, 17345000,30220000, 53225000, 565676667] 
n, b,p = plt.hist(forbs['c'],bins,alpha = 0.7   )
forbs_sum =  forbs['c'].sum()
#%%

base_procent = 0.01

rosstat_forbs = rosstat.copy()
for i in np.arange(len(bins)-1):
    s = pd.Series({'a':bins[i], 'b':bins[i+1],'c':bins[i+1]- bins[i], 'd':base_procent*n[i]})
    rosstat_forbs = rosstat_forbs.append(s, ignore_index=True)
row_index_f = rosstat_forbs.index == 7 
rosstat_forbs.loc[row_index_f,'b']  = bins[0]
rosstat_forbs.loc[row_index_f,'c']  = bins[0] - rosstat_forbs.iloc[7]['a'] 

rosstat_forbs.loc[row_index_f,'d']  = rosstat_forbs.iloc[7]['d']-  rosstat_forbs.iloc[8:15]['d'].sum()

#%%
plt.figure()
rosstat_f_x = np.array([])
rosstat_f_y = np.array([])
max_f_d = rosstat_forbs.iloc[15]['b']
j = 0
integral = 0 
for i in np.arange(len(rosstat_forbs['a'])):
    rosstat_f_x.resize(len(rosstat_f_x) + 2)
    rosstat_f_x.put(j,rosstat_forbs['a'].iloc[i] / max_f_d)
    
    rosstat_f_x.put(j+1,rosstat_forbs['b'].iloc[i] / max_f_d)
    rosstat_f_y.resize(len(rosstat_f_y) + 2)
    dif = rosstat_forbs['b'].iloc[i] - rosstat_forbs['a'].iloc[i]
    rosstat_f_y.put(j,rosstat_forbs['d'].iloc[i] /dif)
    rosstat_f_y.put(j+1,rosstat_forbs['d'].iloc[i]/dif)
    integral =  integral + rosstat_forbs['d'].iloc[i]
    j = j+2
plt.xlim(0,0.0005)
plt.title("Функция плотности распределения")
plt.figtext(.15,.85, integral, fontsize=11, ha='left')
plt.ylabel("Доля населения")
plt.xlabel("Относительный доход населения (в долях от максимального)")
#plt.xlabel("Доход населения (рос.руб.)")  

plt.plot(rosstat_f_x,rosstat_f_y, color = "blue")
plt.savefig("rossta_forbs_base0.01.jpg")
#%%