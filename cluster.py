import pandas as pnd
import matplotlib.pyplot as plt

#Carga de los datos
frutas = pnd.read_csv("datas/frutas.csv",
names=['DIAMETRO','PESO'], header=None)

#Visualización gráfica de los datos
frutas.plot.scatter(x="DIAMETRO",y="PESO")
plt.show()
