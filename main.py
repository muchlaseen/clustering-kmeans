# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:41:54 2021

@author: Native-Muchlas
"""

"""
Ok I decided to move from VSCode to Spyder hehe

"""

import pandas as pd
from learningkmeans import ClusteringKmeans

df = pd.read_excel(r'dummy_data.xlsx')
df = pd.DataFrame(df, columns=(['x','y']))
data = df.values.tolist()
ncluster = 3

#Pembuatan Objek dan pemanggilan method learning 
objek=ClusteringKmeans(data,ncluster)
objek.learning()
objek.plottingError()
objek.scatterDataCentroid()

#Cetak Hasil Utama
print("centroid =",objek.centroid)
print("\n index anggota data = ", objek.index)
print("\n Sum of Distance Semua Iterasi = ",objek.error)
print("\n Sum Of Distance Akhir =", objek.error[len(objek.error)-1])