import numpy as np
import random
class Cereza():
    def __init__(self, diametro, peso, cerezas_lista):
        self.cerezas_lista=cerezas_lista
        self.diametro = diametro
        self.peso = peso

    def __str__(self):
        return f"({self.diametro}) {self.peso}"

class datos_cerezas(Cereza):

    def __init__(self, diametro, peso, cantidadObservaciones, cerezas_lista):
        super().__init__(diametro, peso, cerezas_lista)
        self.cantidadObservaciones=cantidadObservaciones

    def set_cerezas(self, cerezas_lista):
        self.cerezas_lista=cerezas_lista

    def get_cerezas(self):
        print('Medidas de cerezas: '+self.cerezas_lista)

    def generar_cerezas(self):
        #GENERACION DE LOS DATOS
        # [DIAMETRO, PESO]
        #cantidadObservaciones = 200
        self.cerezas_lista=[]
        #Generación de las cerezas
        caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
        self.cantidadObservaciones=6
        np.random.seed()
        for iteration in range(self.cantidadObservaciones):
            #elección al azar de una característica
            cereza = random.choice(caracteristicasCerezas)
            #Generación de un diámetro
            diametro = np.round(random.uniform(cereza[0], cereza[1]),2)
            #Generación de un peso
            peso = round(random.uniform(cereza[2], cereza[3]),2)
            print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
            self.cerezas_lista.append([diametro,peso])

        return self.cerezas_lista


def main():
    lista_cerezas=[[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
    info_cerezas=datos_cerezas(40,44, lista_cerezas, 6)
    info_cerezas.generar_cerezas()


