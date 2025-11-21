from tda_grafo import *
from tda_pila import *


def main():
    casa = Grafo(False)

    # a. Cargar los ambientes como vertices
    print("a. Cargando ambientes de la casa...")
    ambientes = [
        'cocina', 'comedor', 'cochera', 'quincho',
        'baño1', 'baño2', 'habitacion1', 'habitacion2',
        'sala_estar', 'terraza', 'patio'
    ]

    for amb in ambientes:
        insertar_vertice(casa, amb)

    print(f"Se cargaron {tamanio(casa)} ambientes\n")

    # b. Cargar aristas con distancias en metros
    print("b. Conectando ambientes con distancias...")

    insertar_arista(casa, 4, buscar_vertice(casa, 'cocina'),
                    buscar_vertice(casa, 'comedor'))
    insertar_arista(casa, 7, buscar_vertice(casa, 'cocina'),
                    buscar_vertice(casa, 'patio'))
    insertar_arista(casa, 10, buscar_vertice(
        casa, 'cocina'), buscar_vertice(casa, 'baño1'))

    insertar_arista(casa, 5, buscar_vertice(casa, 'comedor'),
                    buscar_vertice(casa, 'sala_estar'))
    insertar_arista(casa, 3, buscar_vertice(casa, 'comedor'),
                    buscar_vertice(casa, 'habitacion1'))
    insertar_arista(casa, 8, buscar_vertice(casa, 'comedor'),
                    buscar_vertice(casa, 'terraza'))
    insertar_arista(casa, 6, buscar_vertice(casa, 'comedor'),
                    buscar_vertice(casa, 'patio'))

    insertar_arista(casa, 2, buscar_vertice(casa, 'cochera'),
                    buscar_vertice(casa, 'patio'))
    insertar_arista(casa, 12, buscar_vertice(casa, 'cochera'),
                    buscar_vertice(casa, 'quincho'))
    insertar_arista(casa, 9, buscar_vertice(casa, 'cochera'),
                    buscar_vertice(casa, 'habitacion2'))

    insertar_arista(casa, 8, buscar_vertice(casa, 'quincho'),
                    buscar_vertice(casa, 'patio'))
    insertar_arista(casa, 5, buscar_vertice(casa, 'quincho'),
                    buscar_vertice(casa, 'terraza'))
    insertar_arista(casa, 11, buscar_vertice(
        casa, 'quincho'), buscar_vertice(casa, 'baño2'))
    insertar_arista(casa, 13, buscar_vertice(casa, 'quincho'),
                    buscar_vertice(casa, 'habitacion2'))

    insertar_arista(casa, 4, buscar_vertice(casa, 'baño1'),
                    buscar_vertice(casa, 'habitacion1'))
    insertar_arista(casa, 7, buscar_vertice(casa, 'baño1'),
                    buscar_vertice(casa, 'sala_estar'))

    insertar_arista(casa, 6, buscar_vertice(casa, 'baño2'),
                    buscar_vertice(casa, 'habitacion2'))
    insertar_arista(casa, 8, buscar_vertice(casa, 'baño2'),
                    buscar_vertice(casa, 'terraza'))

    insertar_arista(casa, 5, buscar_vertice(casa, 'habitacion1'),
                    buscar_vertice(casa, 'sala_estar'))

    insertar_arista(casa, 3, buscar_vertice(casa, 'sala_estar'),
                    buscar_vertice(casa, 'terraza'))
    insertar_arista(casa, 8, buscar_vertice(
        casa, 'sala_estar'), buscar_vertice(casa, 'patio'))

    insertar_arista(casa, 4, buscar_vertice(casa, 'terraza'),
                    buscar_vertice(casa, 'patio'))

    print("Conexiones cargadas correctamente\n")

    print("Verificando conexiones por ambiente:")
    aux = casa.inicio
    while aux is not None:
        cont = 0
        ady = aux.adyacentes.inicio
        while ady is not None:
            cont += 1
            ady = ady.sig
        print(f"  {aux.info}: {cont} conexiones")
        aux = aux.sig

    # c. Arbol de expansion minima
    print("\nc. CALCULANDO ARBOL DE EXPANSION MINIMA...")
    marcar_no_visitado(casa)
    arbol = kruskal(casa)

    if arbol:
        total_metros = 0
        print("\nAristas del arbol de expansion minima:")
        for origen, destino, metros in arbol:
            print(f"  {origen} - {destino} : {metros}m")
            total_metros += metros

        print(f"\n** Total de metros de cable necesarios: {total_metros}m **")
    else:
        print("No se pudo calcular el arbol")

    # d. Camino mas corto para cable de red
    print("\nd. CAMINO MAS CORTO HABITACION1 -> SALA_ESTAR")
    print("   (Para conectar router con Smart TV)")

    marcar_no_visitado(casa)
    camino, distancia = dijkstra(casa, 'habitacion1', 'sala_estar')

    if camino and not camino.vacia():
        print(f"\nCamino encontrado: {distancia}m")
        print("Recorrido:")
        recorrido = []
        while not camino.vacia():
            recorrido.append(camino.desapilar())

        recorrido.reverse()
        for i in range(len(recorrido)):
            if i < len(recorrido) - 1:
                nodo_actual = buscar_vertice(casa, recorrido[i])
                sig_nodo = recorrido[i+1]
                arista_camino = buscar_arista(nodo_actual, sig_nodo)
                if arista_camino:
                    print(
                        f"  {recorrido[i]} --({arista_camino.info}m)--> ", end="")
            else:
                print(f"{recorrido[i]}")

        print(f"\n** Se necesitan {distancia}m de cable de red **")
    else:
        print("No hay camino disponible")


if __name__ == "__main__":
    main()
