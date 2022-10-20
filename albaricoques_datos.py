import numpy as np

class datos_albaricoques:

    def __init__(self,cantidadObservaciones):
        self.cantidadObservaciones = cantidadObservaciones


    def set_albaricoques(self, albaricoques):
        self.albaricoques=albaricoques

    def get_albaricoques(self):
        print('Medidas de albaricoques: '+self.albaricoques)


    def generar_albaricoques(self):
        caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
        #Generación de los albaricoques
        albaricoques_lista = []
        np.random.seed()
        for iteration in range(self.cantidadObservaciones):
            #elección al azar de una característica
            albaricoque = np.random.choice(caracteristicasAlbaricoques)
            #Generación de un diámetro
            diametro = np.round(np.random.uniform(albaricoque[0], albaricoque[1]),2)
            #Generación de un peso
            limiteMinPeso = albaricoque[2] / 1.10
            limiteMaxPeso = albaricoque[2] * 1.10
            peso = round(np.random.uniform(limiteMinPeso, limiteMaxPeso),2)
            print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
            albaricoques_lista.append([diametro,peso])

        return albaricoques_lista