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

# from cerezas_datos import datos_cerezas
# from albaricoques_datos import datos_albaricoques

import cerezas
import albaricoques



#---- CARACTERÍSTICAS------

class Datos(cerezas.datos_cerezas, albaricoques.datos_albaricoques):

#PREGUNTAAAA!!!

#DE DONDE TENGO QUE HEREDAR PARA PODER ACCEDER A LA FUNCIÓN GENERAR_CEREZAS/ALBARICOQUES


    def __init__(self, cerezas_lista, albaricoques_lista):
        super().__init__(self,2, cerezas_lista, albaricoques_lista)



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
    conjunto_cerezas= cerezas.main()
    conjunto_albaricoques= albaricoques.main()
    conjunto_frutas=Datos(conjunto_cerezas, conjunto_albaricoques)
    conjunto_frutas.generar_frutas()

