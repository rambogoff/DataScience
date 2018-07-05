# -*- coding: utf-8 -*-
import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik


#%% Loop Data Structures

#i = 0 
#while i != 5:
#    print('i  :', i)
#    i += 1
#print(i, '= 5 ')

#%%
#lis = [1, 2, 3, 4, 5]
#for i in lis:
#    print('i:', i)
#print(' ')

#%% 
#dictionary = {'Turkey' : 'Ankara', 'Osmanlı' : 'Bursa', 'Pakistan' : 'Islamabad'}
#for key, value in dictionary.items():
#    print (key, 'Başkenti:', value)
#print('')

#%%

for index, value in data[['Attack']][0:5].iterrows():
    print(index, ': ', value)