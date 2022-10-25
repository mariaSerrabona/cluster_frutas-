import cluster_curvas_gaussianas.creador_cluster as creador_cluster
import cluster_curvas_gaussianas.Visualizacion_3D_curvas_gaussianas as Visualizacion_3D_curvas_gaussianas
import frutas.albaricoques as albaricoques
import frutas.cerezas as cerezas
#import frutas.generacion_de_datos as generacion_de_datos

# Me da un error en la importación en el archivo generacion_de_datos.py, porque no me deja importar el archivo cerezas ni albaricoques
#comento el error para que funciones el programa porque aun así, el programa funciona perfectamnete.

if __name__ == '__main__':
    albaricoques.main()
    cerezas.main()
    #generacion_de_datos.main()
    Visualizacion_3D_curvas_gaussianas.main()
    creador_cluster.main()