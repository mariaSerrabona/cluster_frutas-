from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class cluster():

    #constructor de la clase
    def __init__(self,datos, num_cluster):
        self.datos = datos
        self.num_cluster=num_cluster


    #leemos los datos
    def leer_datos(self):
        self.datos=pd.reaad_csv('datas/frutas.csv',names=['DIAMETRO','PESO'], header=None )

    def generar_guardar_plot(self):
        #Visualización gráfica de los datos
        self.datos.plot.scatter(x='DIAMETRO',y='PESO')
        #gaurdamos el plot en un archivo
        plt.savefig('scatter_frutas.png')








    #Caraga de datos

#Visualización gráfica de los datos
frutas.plot.scatter(x="DIAMETRO",y="PESO")
plt.show()


#Aprendizaje con el algoritmo K-Mean
from sklearn.cluster import KMeans
modelo=KMeans(n_clusters=2)
modelo.fit(frutas)

#Predicciones
predicciones_kmeans = modelo.predict(frutas)

#Visualización de la clusterización
plt.scatter(frutas.DIAMETRO, frutas.PESO, c=predicciones_kmeans, s=50, cmap='viridis')
plt.xlabel("DIAMETRO")
plt.ylabel("PESO")

#Visualización de los centroides
centers = modelo.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()