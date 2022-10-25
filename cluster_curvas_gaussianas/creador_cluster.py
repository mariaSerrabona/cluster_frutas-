import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import mixture


class cluster():

    #constructor de la clase
    def __init__(self,datos_frutas, num_cluster):
        self.datos_frutas = datos_frutas
        self.num_cluster=num_cluster


    #leemos los datos
    # def leer_datos(self):
    #     self.datos_frutas=pd.read_csv('datas/frutas.csv',names=['DIAMETRO','PESO'], header=None )

    def generar_guardar_plot(self):
        #Visualización gráfica de los datos
        self.datos_frutas.plot.scatter(x='DIAMETRO',y='PESO')
        #gaurdamos el plot en un archivo
        plt.show()
        plt.savefig('fotos/scatter_frutas.png')

    def generar_cluster(self):
        #Aprendizaje con el algoritmo K-Mean
        modelo=KMeans(self.num_cluster)
        modelo.fit(self.datos_frutas)
        #Predicciones
        predicciones_kmeans = modelo.predict(self.datos_frutas)

        #Visualización de la clusterización
        plt.scatter(self.datos_frutas.DIAMETRO, self.datos_frutas.PESO, c=predicciones_kmeans, s=50, cmap='viridis')
        plt.xlabel("DIAMETRO")
        plt.ylabel("PESO")

        #Visualización de los centroides
        centers = modelo.cluster_centers_
        plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
        plt.show()
        plt.savefig('fotos/KMeans_frutas.png')


    def predicciones_kmeans(self):
        modelo=KMeans(self.num_cluster)
        modelo.fit(self.datos_frutas)
        cereza = [[26.98,8.75]]
        self.numCluster = modelo.predict(cereza)
        print("Número de clúster de las cerezas: "+ str(self.numCluster))


        albaricoque = [[55.7,102.16]]
        self.numCluster = modelo.predict(albaricoque)
        print("Número de clúster de los albaricoques: " + str(self.numCluster))


        #Instrucciones a adaptar en función de los números de clústeres
        #determinados con anterioridad:

        if int(self.numCluster)==0:
            print("¡Es un albaricoque!")
        else:
            print("¡Es una cereza! ")


        if int(self.numCluster)==0:
            print("¡Es un albaricoque!")
        else:
            print("¡Es una cereza!")

    def mezclas_gaussianas(self):
        #---- Modelo de mezclas Gaussianas (GMM) -----------

        #Determinación de los clústeres (encontrar 2)
        gmm = mixture.GaussianMixture(n_components=2)

        #Aprendizaje
        gmm.fit(self.datos_frutas)

        #Clasificación
        clusteres = gmm.predict(self.datos_frutas)

        #Visualización de los clústeres
        plt.scatter(self.datos_frutas.DIAMETRO, self.datos_frutas.PESO, c=clusteres, s=40, cmap='viridis');
        plt.xlabel("DIAMETRO")
        plt.ylabel("PESO")
        plt.show()
        plt.savefig('fotos/Modelo_mezclas_gaussianas.png')





def main():
    datos_frutas=pd.read_csv('datas/frutas.csv',names=['DIAMETRO','PESO'], header=None )
    cluster_prueba=cluster(datos_frutas, 2)
    cluster_prueba.generar_cluster()
    cluster_prueba.predicciones_kmeans()
    cluster_prueba.mezclas_gaussianas()



