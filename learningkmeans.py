# %%
from kmeans import kmeans
import matplotlib.pyplot as plt
import numpy as np

class ClusteringKmeans(kmeans):
    error=[]
    
    def __init__(self,data,ncluster):
        kmeans.data=data
        kmeans.nCluster=ncluster
        kmeans.initCentroid(self)
        
    def learning(self):
        errorLama=-1
        errorBaru=0
        
        while errorLama!=errorBaru:
            errorLama=errorBaru
            kmeans.getAllJarak(self)
            kmeans.getAnggota(self)
            kmeans.getSumOfDistance(self) 
            kmeans.getCentroid(self)
            errorBaru=kmeans.error
            ClusteringKmeans.error.append(errorBaru)
        
    def plottingError(self):
        plt.plot(self.error)
        plt.title("Sum of Distance")
        plt.xlabel("Iterasi")
        plt.ylabel("Error")
        plt.show()
    
    def scatterDataCentroid(self):
        fig, ax = plt.subplots()
        x = self.kumpulAnggotaPercluster()
        tes = []
        for i in range (len(x)):
            tes.append(i)
            temp=np.array(x[i])
            ax.scatter(temp[:,0], temp[:,1])
        cent=np.array(kmeans.centroid)
        plt.legend(tes)
        ax.scatter(cent[:,0], cent[:,1], marker='x')
        plt.title("Scatter")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
    
    def kumpulAnggotaPercluster(self):
        n=len(kmeans.data)
        m=kmeans.nCluster
        Datacluster=[]
        for i in range (m):
            temp=[]
            for j in range (n):
                if (i==kmeans.index[j]):
                    temp.append(kmeans.data[j])
            Datacluster.append(temp)
        return Datacluster
        
#Main Program
data=[[1,2],[3,4],[2,3],[9,2],[8,9],[2,6],[8,1],[9,5],[8,9],[5,8],[8,8]]
ncluster=2

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

# %%
