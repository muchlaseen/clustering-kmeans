from kmeans import kmeans

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

# Main Program
data = [[1, 2], [3, 4], [2, 3], [9, 2], [8, 9], [2, 6], [8, 1], [9, 5], [8, 9], [5, 8], [8, 8]]
ncluster = 3

# Pembuatan objek dan testing
objek=ClusteringKmeans(data,ncluster)
objek.learning()

# Printing
print("Centroid : ", objek.centroid)
print("\nIndex anggota : ", objek.index)
print("\nSum of Distance semua iterasi: ", objek.error)
print("\nSum of Distance akhir: ", objek.error[len(objek.error)-1])