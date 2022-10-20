#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro:
# @Capítulo: 9 - Albaricoques, cerezas y clustering
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   SCIKIT-LEARN : 0.21.0
#   MATPLOTLIB : 3.0.3
#   JOBLIB : 0.13.2
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------



import pandas as pnd
import matplotlib.pyplot as plt


#Caraga de datos
frutas = pnd.read_csv("datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)

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

#Guardar el modelo (eliminar marca de comentario # si es necesario)
#from joblib import dump
#dump(modelo,'modelos/kmean.joblib')

#--- Realización de las clasificaciones --
#CEREZA: 26,98 mm de diametro ,8,75 gramos
#ALBARICOQUE: 55,7  mm de diámetro , 102,16 gramos


cereza = [[26.98,8.75]]
numCluster = modelo.predict(cereza)
print("Número de clúster de las cerezas: "+ str(numCluster))


albaricoque = [[55.7,102.16]]
numCluster = modelo.predict(albaricoque)
print("Número de clúster de los albaricoques: " + str(numCluster))

#Instrucciones a adaptar en función de los números de clústeres
#determinados con anterioridad:

cereza = [[26.98,8.75]]
numCluster = modelo.predict(cereza)
if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza! ")


albaricoque = [[55.7,102.16]]
numCluster = modelo.predict(albaricoque)
if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza!")


#---- Modelo de mezclas Gaussianas (GMM) -----------
from sklearn import mixture

#Determinación de los clústeres (encontrar 2)
gmm = mixture.GaussianMixture(n_components=2)

#Aprendizaje
gmm.fit(frutas)

#Clasificación
clusteres = gmm.predict(frutas)

#Visualización de los clústeres
plt.scatter(frutas.DIAMETRO, frutas.PESO, c=clusteres, s=40, cmap='viridis');
plt.xlabel("DIAMETRO")
plt.ylabel("PESO")
plt.show()

