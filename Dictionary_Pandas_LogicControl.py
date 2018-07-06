# -*- coding: utf-8 -*-

import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool


dictionary = {"Turkey" : "Ankara", "Spain" : "Madrid"}
print(dictionary.keys())
print(dictionary.values())
#
dictionary['Turkey'] = "Kirikkale" # Update
dictionary['France'] = 'Paris' #Add new entry
del dictionary ['Spain'] #remove entry
print ('France' in dictionary) # Search results:(True/False)
dictionary.clear() # remove all
print(dictionary)



#%% Pandas CSV (Comma- separated values)
data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

# seriler vektör şeklinde tek boyutlu
#dataFrameler iki boyutlu
#
series = data['Defense']  #series [""] = Series
print(type(series))
data_frame = data[['Defense']]  #data[[""]] = dataFrame
print(type(data_frame))


# ==, <, >, <=, >=
# boolean and, or, not result (T/F)

#%% Filtering

x = data['Defense'] > 200
data[x]


#1.Path
data[np.logical_and(data['Defense'] >200,
                   data['Attack'] > 100)]
#2.path
data[(data['Defense'] > 200) &(data['Attack'] > 100) ]



























