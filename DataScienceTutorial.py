import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool


data = pd.read_csv("pokemon.csv")

a = data.head() # head shows first 5 rows
print(a)

b = data.tail() # tail shows last 5 rows

print(b) 

data.columns # column names

data.shape # (row, column)

data.info() # info gives data

#%% ##Nested Function
def square():
    def add():
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())
#%%  # Flexible


def f(*args):
    for i in args:
        print(i)
f(1, 2, 3, 4, 5)


def f(**kwargs):
    for key, value in kwargs.items():
        print(key, ' ', value)
f(country = 'Spain', capital = 'madrid', populatin = 1231231)

#%%     #Lambda Function


square = lambda x: x**2
print(square(4))

tıt = lambda x, y, z : x*x*y*z
print(tıt(1, 2, 3))
#%%
# Anonymous Function
 # map(func,seq)

number_list = [1, 2, 3]
y = map (lambda x : x * 2, number_list)
print(list(y))

#%%   #Iterators 


name = "Dimaria"
it = iter(name)
print(next(it)) # D
print(*it) # imaria
#%%  Zip Example

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
z = zip(list1, list2)
print(z)
z_list = list(z) #<zip object at 0x000001AA21C20288>
print(z_list) # [(1, 5), (2, 6), (3, 7), (4, 8)]

un_zip = zip(*z_list)
un_list1, un_list2 = list(un_zip)
print(un_list1)   #(1, 2, 3, 4)
print(un_list2)     #(5, 6, 7, 8)

print(type(un_list2)) # <class 'tuple'>
print(type(list(un_list2))) # <class 'list'>


#%% List Comphrehension

num1 = [1, 2, 3, 4]
num2 = [i+1 for i in num1]
print(num2)
#♠ [2, 3, 4, 5]


num3 = [4, 12, 14]
num4 = [i**2 if i == 10 else i - 5 if i < 7 else i + 5 for i in num3]
print(num4)

#♣ [-1, 17, 19]


#%% Loop Data Structures

i = 0 
while i != 5:
    print('i  :', i)
    i += 1
print(i, '= 5 ')

#%%
lis = [1, 2, 3, 4, 5]
for i in lis:
    print('i:', i)
print(' ')

#%% 
dictionary = {'Turkey' : 'Ankara', 'Osmanlı' : 'Bursa', 'Pakistan' : 'Islamabad'}
for key, value in dictionary.items():
    print (key, 'Başkenti:', value)
print('')

#%%

for index, value in data[['Attack']][0:5].iterrows(): # Attack ilk beş al
    print(index, ': ', value)
dictionary = {"Turkey" : "Ankara", "Spain" : "Madrid"}
print(dictionary.keys())
print(dictionary.values())

dictionary['Turkey'] = "Kirikkale" # Update
dictionary['France'] = 'Paris' #Add new entry
del dictionary ['Spain'] #remove entry
print ('France' in dictionary) # Search results:(True/False)
dictionary.clear() # remove all
print(dictionary)

#%% Pandas CSV (Comma- separated values)
#data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

#seriler vektör şeklinde tek boyutlu
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


#%% Cleanin Data
import numpy as np # linear algebra
import pandas as pd # data processing


a = data.head() # head shows first 5 rows
print(a)
#
b = data.tail() # tail shows last 5 rows
#
print(b) 
#
data.columns # column names
#
data.shape() # (row, column)
#
data.info() # info gives data


#%% Exploratory Data Analysis (EDA)
# outlier (ayrık)
 # 1,4,5,6,8,9,11,12,13,14,15,16,17
 # Median %50 IQR(ortadaki sayı 11) # IQR = (Q3-Q1)
 # Lower quartile %25 Q1(1-11 arasındaki sayının median 6)
 # Upper quartile %75  Q3(11-17 arasındali sayının median 14)
 # MİNUMUM = Q1 -1.5IQR
 # MAXİMUM =1.5IQR + Q3


#print(data['Type 1'].value_counts(dropna =False))
 
aa = data.describe() # sadece nümeric olanları getirir
print(aa)
 
 
 #%% VISUAL EXPLORATORY DATA ANALYSIS
# Box plots: outliers, min/max or quantiles
 
data.boxplot( column = "Attack", by = "Legendary" )
plt.show()


 #%% Tidy and Pivoting Data
# melt() fonksiyonu pandas library
 # melt etmek datadan belli başlı featureları çıkarmak
 
 
data_new = data.head()
#
melted = pd.melt(frame = data_new, id_vars = 'Name', value_vars=['Type 1', 'Type 2'])
#
melted.pivot(index = 'Name', columns = 'variable',values='value') 



#%% CONCATENATING DATA
# iki datayı birleştirir
 
data1 = data.head()
data2 = data.tail()

conc_data_row = pd.concat([data1, data2], axis = 0, ignore_index = True)
# axis = 0 vertical (dikey/ alt alta) bir şekilde 
# ignore_index yeni index ata


data3 = data['Attack'].head()
data4 = data['Defense'].head()
# Horizontal(yatay bir şekile yan-yana)
conc_data_col1 = pd.concat([data3, data4], axis = 1)
#%% DATA TYPES
#☺ 
data.dtypes # data verilerinin tipleri
data ['Type 1'] = data['Type 1'].astype('category') # tipini değiştiriyor
data ['Speed'] = data['Speed'].astype('float')
#%% MISSING DATA and TESTING WITH ASSERT

# Missing data //değeri olmayan yani NaN

data.info()
 # datamızın her farklı değerden kaç tane var onu hesaplıyoruz
 # Nan varsa bunuda say (dropna)
data["Type 2"].value_counts(dropna = False)
#Nan olanları at dropna
data["Type 2"].dropna(inplace = True)

#assert 1 == 1 # hiçbirşey döndürmede doğru demek
assert data['Type 2'].notnull().all()

# column 1 Name mi ?
assert data.columns[1] == 'Name' 
# data.speed tipi int mi ?
assert data.Speed.dtypes == np.int

# data Type 2 yi empty ile doldurmak istiyorum
data["Type 2"].fillna('empty',inplace = True)

#%% MATPLOTLİB

import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt

data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

data.info() # data ile ilgili bilgiler
data.corr() # Matris formatında yazıyoruz

# Correlation Map : İki feature arasında corration 1 ise doğru orantılıdır
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
# heatmap data.corr u içine alıyor 
#annot sayıların gözükmesi 
#linewidths çizgilerin kalınlığı
#fmt .'dan sonra kaç basamak yazacağımız
#figsize figuremüzün kaça kaç olduğu
plt.show()


data.head(10) # ilk 10 satır
data.columns # sütunların adları

#%% MATPLOTLIB dataya görselleştirmeye yarar
 
#Line Plot
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
#
#%% Histogram
# bins barların sayısı
data.Speed.plot(kind = "hist", bins = 50, figsize = (15, 15))
#plt.hist(data.Speed, bins = 50, color = "r", figsize = (15, 15))
plt.show()
plt.clf() # Histogramı Temizler 

#%% #%% Pandas

#single column = series
#NaN = not a number
#dataframe.values = numpy

country = ['Turkey', 'Spain', 'France']
population = ['82', '11', '12']
list_label = ['country', 'population']
list_col =[country, population]
# zip(sıkıştırma)
zipped = list(zip(list_label, list_col))
# Sözlüğe çevirdik
data_dict = dict(zipped)
# DataFrame oluşturmak için
df = pd.DataFrame(data_dict)

# Add new columns
df["Capital"] = ["Ankara", "Kırıkkale", "Corum"]
# Broadcasting yeni bir column ekleyip değeri 0 atadık
df["Income"] = 0



#%%     VISUAL EXPLORATORY DATA ANALYSIS

data = pd.read_csv("pokemon.csv")

data1 = data.loc[:, ["Attack", "Defense", "Speed", "Sp. Atk"]]
data1.plot()
# karmaşıklığı çözmek için subplots
data1.plot(subplots = True)
plt.show()
data1.plot()

#Scatter plot 
data1.plot(kind = "scatter", x = "Attack", y = "Defense")
#Histogram  range: y eksenimiz  normed: data Normalize et yani 0-1 arasında grafik
data1.plot(kind = "hist", y = "Defense", bins = 50, range = (0,250) , normed = True)

fig, axes = plt.subplots(nrows = 2, ncols = 1)
data1.plot(kind = "hist", y = "Defense", bins = 50, range =(0, 250), normed =True, ax = axes[0])

# komulatif histogram ile 
data1.plot(kind = "hist", y = "Defense", bins = 50, range =(0, 250), normed =True, ax = axes[1], cumulative = True)



#%%     STATISTICAL EXPLORATORY DATA ANALYSIS
  # indexlerimiz time series için bazı metotlar
#datatime = object
#parse_dates(boolean) formata çevirir

time_list = ["1992-03-12", "1992-04-12"]
print(type(time_list[1]))
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

data = pd.read_csv("pokemon.csv")
data2 = data.head()
#time listeli oluşturk
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
# pandas ile çevirdik objeye
datetime_object = pd.to_datetime(date_list)
#data2 ye ekledik
data2["date"] = datetime_object
#  indeximiz artık date oldu
data2 = data2.set_index("date")

# bilgeleri getir 
print(data2.loc["1993.03.16"])
# sunlar arasında olan bilgileri getir
print(data2.loc["1992-03-10":"1993-03-16"])
# RESAMPLING PANDAS TIME SERIES
# M ay A yıl

# Yıla göre resample et ve ortalamasını al 
data2.resample("A").mean()

# first data mı interpolate et diyorum. Boş olan değerlerimi linear bir şekilde doldurur
data2.resample("M").first().interpolate("linear")

# mean ları aynı olacak şekilde interpolate et
data2.resample("M").mean().interpolate("linear")
#%%
import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool


data = pd.read_csv("pokemon.csv")
data2 = data.set_index("#")                      
data2.head()
#
##%%
data2["HP"][1]
data2.HP[1]
# using loc accessor
data2.loc[1,["HP"]]
#%%
data ["HP", "Attack"]
#%% Slicing Data Frame

print(type(data2["HP"]))     # series
print(type(data2[["HP"]]))   # data frames


data2.loc[1:10,"HP":"Defense"] 
data2.loc[10:1:-1,"HP":"Defense"]
data2.loc[1:10,"Speed":]  # Speed den en sonuncusuna kadar al :
#
##%% FILTERING DATA FRAMES

boolean = data2.HP > 200
data2[boolean]
#
first_filter = data2.HP > 150
second_filter = data2.Speed > 35
data2[first_filter & second_filter]
#
data2.HP[data.Speed<15]

##%%     TRANSFORMING DATA

# Pokemonlarımın canının ikiye bölmek istiyorum
def div(n):
    return n/2
data2.HP.apply(div)

#lambda function

data2.HP.apply(lambda n : n/2)

# yeni bir column tanımlamak istersek

data2["total_power"] = data2.Attack + data2.Defense
#
##%%     INDEX OBJECTS AND LABELED DATA
#
#
print(data.Index.name)
# lets change it
data.index.name = "index_name"
data.head()


data.head()
data3 = data.copy()
data3.index = range(100,900,1)
data3.head()
#
##&&

data3 = data2.set_index(["Type 1", "Type 2"])

#
dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
## PİVOT
#df.pivot( index = "treatment", columns = "gender", values ="response")
#
df1 = df.set_index(["treatment", "gender"])
df1.unstack(level=0)
df1.unstack(level=1)

# yerdeğiştirme
df2 = df1.swaplevel(0,1)

# melting data Pivotun tam tersi

pd.melt(df,id_vars="treatment",value_vars=["age","response"])

# Group la ortalamasını al
df.groupby("treatment").mean()
# max ını al
df.groupby("treatment").age.max() 
#
df.groupby("treatment")[["age","response"]].min() 

#%%
