# DATA SCIENTIST

MATPLOTLIB

import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

data.info() # data ile ilgili bilgiler
Out :
![screenshot_1](https://user-images.githubusercontent.com/11053905/42327852-748e8600-8075-11e8-90b7-b71cc2912a2d.png)




data.corr() # data'yı matrisleştirdik
Out: 

