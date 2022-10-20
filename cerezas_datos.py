import numpy as np

class datos_cerezas:

    def __init__(self,cantidadObservaciones):
        self.cantidadObservaciones = cantidadObservaciones

    def set_albaricoques(self, cereza):
        self.cereza=cereza

    def get_albaricoques(self):
        print('Medidas de cerezas: '+self.cereza)

    def generar_cerezas(self):
        #GENERACION DE LOS DATOS
        # [DIAMETRO, PESO]
        #cantidadObservaciones = 200

        #Generación de las cerezas
        caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
        cerezas_lista = []
        np.random.seed()
        for iteration in range(self.cantidadObservaciones):
            #elección al azar de una característica
            cereza = np.random.choice(caracteristicasCerezas)
            #Generación de un diámetro
            diametro = np.round(np.random.uniform(cereza[0], cereza[1]),2)
            #Generación de un peso
            peso = np.round(np.random.uniform(cereza[2], cereza[3]),2)
            print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
            cerezas_lista.append([diametro,peso])

        return cerezas_lista
