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

from cerezas_datos import datos_cerezas
from albaricoques_datos import datos_albaricoques

# from generacion_datos import albaricoques_datos
# from generacion_datos import cerezas_datos


#---- CARACTERÍSTICAS------

class Datos(datos_cerezas, datos_albaricoques):

#PREGUNTAAAA!!!

#DE DONDE TENGO QUE HEREDAR PARA PODER ACCEDER A LA FUNCIÓN GENERAR_CEREZAS/ALBARICOQUES


    def __init__(self):
        super().__init__(self)

    # def __str__(self):
    #     return f"({self.albaricoque}) {self.cereza}"

    #CEREZAS
    #caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]



    #ALBARICOQUES: ATENCIÓN DOS CASOS DE PRUEBAS EN FUNCIÓN DEL AVANCE DE SU LECTURA

    #Caso 1:
    #caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

    #Caso 2:
    #caracteristicasAlbaricoques = [[35,39,27],[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

    # def __init__(self, name):
    #     self.name = name

    # def generar_cerezas(cantidadObservaciones):
    #     #GENERACION DE LOS DATOS
    #     # [DIAMETRO, PESO]
    #     #cantidadObservaciones = 200

    #     #Generación de las cerezas
    #     caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
    #     cerezas = []
    #     random.seed()
    #     for iteration in range(cantidadObservaciones):
    #         #elección al azar de una característica
    #         cereza = random.choice(caracteristicasCerezas)
    #         #Generación de un diámetro
    #         diametro = round(random.uniform(cereza[0], cereza[1]),2)
    #         #Generación de un peso
    #         peso = round(random.uniform(cereza[2], cereza[3]),2)
    #         print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
    #         cerezas.append([diametro,peso])

    #     return cerezas


    # def generar_albaricoques(cantidadObservaciones):
    #     caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
    #     #Generación de los albaricoques
    #     albaricoques = []
    #     random.seed()
    #     for iteration in range(cantidadObservaciones):
    #         #elección al azar de una característica
    #         albaricoque = random.choice(caracteristicasAlbaricoques)
    #         #Generación de un diámetro
    #         diametro = round(random.uniform(albaricoque[0], albaricoque[1]),2)
    #         #Generación de un peso
    #         limiteMinPeso = albaricoque[2] / 1.10
    #         limiteMaxPeso = albaricoque[2] * 1.10
    #         peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
    #         print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
    #         albaricoques.append([diametro,peso])

    #     return albaricoques

    def generar_frutas(self):
        self.cereza=super().generar_cerezas()
        self.albaricoque=super().generar_albaricoques()
        #Constitución de las observaciones
        frutas = self.cereza+self.albaricoque
        #Mezcla de las observaciones
        random.shuffle(frutas)

        #Guardado de las observaciones en un archivo
        frutas_df = pnd.DataFrame(frutas)
        frutas_df.to_csv("datas/frutas.csv", index=False,header=False)

        return frutas_df




def main():
    curva=curvas_gausianas()
    curva.generar_curvas_gausianas()


if __name__ == '__main__':
    main()