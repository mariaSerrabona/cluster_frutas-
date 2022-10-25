import numpy as np
import random

class Albaricoque():
    def __init__(self, diametro, peso, albaricoques_lista):
        self.diametro = diametro
        self.peso = peso
        self.albaricoques_lista=albaricoques_lista

    def __str__(self):
        return f"({self.diametro}) {self.peso}"

class datos_albaricoques(Albaricoque):

    def __init__(self, diametro, peso,albaricoques_lista, cantidadObservaciones):
        super().__init__(diametro, peso, albaricoques_lista)
        self.cantidadObservaciones=cantidadObservaciones



    def set_albaricoques(self, albaricoques_lista):
        self.albaricoques_lista=albaricoques_lista

    def get_albaricoques(self):
        print('Medidas de albaricoques: '+self.albaricoques_lista)


    def generar_albaricoques(self):
        caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
        self.cantidadObservaciones=4
        #Generación de los albaricoques
        self.albaricoques_lista = []
        random.seed()
        for iteration in range(self.cantidadObservaciones):
            #elección al azar de una característica
            albaricoque = random.choice(caracteristicasAlbaricoques)
            #Generación de un diámetro
            diametro = np.round(random.uniform(albaricoque[0], albaricoque[1]),2)
            #Generación de un peso
            limiteMinPeso = albaricoque[2] / 1.10
            limiteMaxPeso = albaricoque[2] * 1.10
            peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
            print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
            self.albaricoques_lista.append([diametro,peso])

        return self.albaricoques_lista




def main():
    lista_albaricoque=[[22.4,6.42],[58.09,106.06],[20.46,5.98],[28.63,10.85],[17.59,3.58]]
    info_albaricoques=datos_albaricoques(40,44, lista_albaricoque, 4)

    return info_albaricoques.generar_albaricoques()



