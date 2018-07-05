# DATA SCIENTIST

MATPLOTLIB

import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

data = pd.read_csv("pokemon.csv") # pandas kütüphanesini kullanarak pokemon.csv import ettik

data.info() # data ile ilgili bilgiler
Out :

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 800 entries, 0 to 799
Data columns (total 12 columns):
#             800 non-null int64
Name          799 non-null object
Type 1        800 non-null object
Type 2        414 non-null object
HP            800 non-null int64
Attack        800 non-null int64
Defense       800 non-null int64
Sp. Atk       800 non-null int64
Sp. Def       800 non-null int64
Speed         800 non-null int64
Generation    800 non-null int64
Legendary     800 non-null bool
dtypes: bool(1), int64(8), object(3)
memory usage: 69.6+ KB


data.corr() # data'yı matrisleştirdik
Out: 
                   #        HP    ...      Generation  Legendary
#           1.000000  0.097712    ...        0.983428   0.154336
HP          0.097712  1.000000    ...        0.058683   0.273620
Attack      0.102664  0.422386    ...        0.051451   0.345408
Defense     0.094691  0.239622    ...        0.042419   0.246377
Sp. Atk     0.089199  0.362380    ...        0.036437   0.448907
Sp. Def     0.085596  0.378718    ...        0.028486   0.363937
Speed       0.012181  0.175952    ...       -0.023121   0.326715
Generation  0.983428  0.058683    ...        1.000000   0.079794
Legendary   0.154336  0.273620    ...        0.079794   1.000000

[9 rows x 9 columns]

