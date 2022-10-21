import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class cluster():

    #constructor de la clase
    def __init__(self,datos_frutas, num_cluster):
        self.datos_frutas = datos_frutas
        self.num_cluster=num_cluster


    #leemos los datos
    def leer_datos(self):
        self.datos_frutas=pd.read_csv('datas/frutas.csv',names=['DIAMETRO','PESO'], header=None )

    def generar_guardar_plot(self):
        #Visualización gráfica de los datos
        self.datos_frutas.plot.scatter(x='DIAMETRO',y='PESO')
        #gaurdamos el plot en un archivo
        plt.savefig('scatter_frutas.png')

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
        plt.savefig('KMeans_frutas.png')

