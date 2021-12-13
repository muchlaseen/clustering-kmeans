# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:41:54 2021

@author: Native-Muchlas
"""

"""
Ok I decided to move from VSCode to Spyder hehe

"""

import pandas as pd
# from learningkmeans import ClusteringKmeans

df = pd.read_excel('dummy_data.xlsx')
df = pd.DataFrame(df, columns=(['x','y']))
data = df.values.tolist()
print("data = ", data)
