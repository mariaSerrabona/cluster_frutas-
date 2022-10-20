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



#---- IMPORTAR MÓDULOS --
import random
import pandas as pnd

#---- CARACTERÍSTICAS------

#CEREZAS
caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]



#ALBARICOQUES: ATENCIÓN DOS CASOS DE PRUEBAS EN FUNCIÓN DEL AVANCE DE SU LECTURA

#Caso 1:
caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

#Caso 2:
#caracteristicasAlbaricoques = [[35,39,27],[40,44,41],[45,49,54],[50,54,74],[55,59,100]]


#GENERACION DE LOS DATOS
# [DIAMETRO, PESO]
cantidadObservaciones = 200

#Generación de las cerezas
cerezas = []
random.seed()
for iteration in range(cantidadObservaciones):
    #elección al azar de una característica
    cereza = random.choice(caracteristicasCerezas)
    #Generación de un diámetro
    diametro = round(random.uniform(cereza[0], cereza[1]),2)
    #Generación de un peso
    peso = round(random.uniform(cereza[2], cereza[3]),2)
    print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
    cerezas.append([diametro,peso])


#Generación de los albaricoques
albaricoques = []
random.seed()
for iteration in range(cantidadObservaciones):
    #elección al azar de una característica
    albaricoque = random.choice(caracteristicasAlbaricoques)
    #Generación de un diámetro
    diametro = round(random.uniform(albaricoque[0], albaricoque[1]),2)
    #Generación de un peso
    limiteMinPeso = albaricoque[2] / 1.10
    limiteMaxPeso = albaricoque[2] * 1.10
    peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
    print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
    albaricoques.append([diametro,peso])


#Constitución de las observaciones
frutas = cerezas+albaricoques
print(frutas)

#Mezcla de las observaciones
random.shuffle(frutas)

#Guardado de las observaciones en un archivo
dataFrame = pnd.DataFrame(frutas)
dataFrame.to_csv("datas/frutas.csv", index=False,header=False)






