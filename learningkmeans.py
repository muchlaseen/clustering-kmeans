from kmeans import kmeans
import matplotlib.pyplot as plt
import numpy as np

class ClusteringKmeans(kmeans):
    error=[]

    def __init__(self, data, ncluster):
        kmeans.data=data
        kmeans.nCluster=ncluster
        kmeans.initCentroidStatic(self)

    def learning(self):
        oldError = -1
        newError = 0

        while oldError != newError:
            oldError = newError
            kmeans.getAllJarak(self)
            kmeans.getAnggota(self)
            kmeans.getSumOfDistance(self)
            kmeans.initCentroidStatic(self)
            newError=kmeans.error
            self.error.append(newError)

    def plottingError(self):
        plt.plot(self.error)
        plt.show

    def scatterDataCentroid(self):
        x=self.kumpulAnggotaPercluster()
        for i in range (len(x)):
            temp=np.array(x[i])
            plt.scatter(temp[:,0],temp[:,1])
            cent=np.array(kmeans.centroid)
            plt.scatter(cent[:,0], cent[:,1], marker='x')
            plt.show()
    
    def kumpulAnggotaPercluster(self):
        n=len(kmeans.data)
        m=kmeans.nCluster
        Datacluster=[]

        for i in range (m):
            temp=[]
            for j in range (n):
                if(i == kmeans.index[j]):
                    temp.append(kmeans.data[j])
                    Datacluster.append(temp)
            
            return Datacluster
        
# Main Program
data = [[1, 2], [3, 4], [2, 3], [9, 2], [8, 9], [2, 6], [8, 1], [9, 5], [8, 9], [5, 8], [8, 8]]
ncluster = 3

# Pembuatan objek dan testing
objek=ClusteringKmeans(data,ncluster)
objek.learning()
objek.plottingError()
objek.scatterDataCentroid()

# # Printing
# print("Centroid : ", objek.centroid)
# print("\nIndex anggota : ", objek.index)
# print("\nSum of Distance semua iterasi: ", objek.error)
# print("\nSum of Distance akhir: ", objek.error[len(objek.error)-1])
# %%
