import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

data.info() # data ile ilgili bilgiler
data.corr() # Matris formatında yazıyoruz

Correlation Map : İki feature arasında corration 1 ise doğru orantılıdır
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
#heatmap data.corr u içine alıyor 
annot sayıların gözükmesi 
linewidths çizgilerin kalınlığı
#fmt .'dan sonra kaç basamak yazacağımız
#figsize figuremüzün kaça kaç olduğu
plt.show()
#
#
data.head(10) # ilk 10 satır
data.columns # sütunların adları

#%% MATPLOTLIB dataya görselleştirmeye yarar
 
# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
data.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper left')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show()

#%% Scatter plot
# plt.scatter(data.Attack, data.Defense, color = "r", alpha = 0.5) 
data.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')   # title = title of plot
##
#%% Histogram
## bins barların sayısı
data.Speed.plot(kind = "hist", bins = 50, figsize = (15, 15))
#plt.hist(data.Speed, bins = 50, color = "r", figsize = (15, 15))
plt.show()
plt.clf() # Histogramı Temizler 

#%% 




















