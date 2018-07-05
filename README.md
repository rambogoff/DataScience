# DATA SCIENTIST

MATPLOTLIB

import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

data.info() # data ile ilgili bilgiler
Out :
![screenshot_1](https://user-images.githubusercontent.com/11053905/42327736-23764d7a-8075-11e8-8d29-e57288f2980d.png)



data.corr() # data'yı matrisleştirdik
Out: 

