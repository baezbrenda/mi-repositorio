from tda_pila import Pila, pila_vacia, desapilar, apilar


class nodoArista(object):
    """Clase nodo arista."""

    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de aristas implementación sobre lista."""

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < dato:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregar_arista(destino.adyacentes, dato, origen.info)


def agregar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def buscar_vertice(grafo, buscado):
    """Devuelve la dirección del elemento buscado."""
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux


def buscar_arista(vertice, buscado):
    """Devuelve la dirección del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while aux is not None:
        if aux.destino == buscado:
            return aux
        aux = aux.sig
    return None


def adyacentes(vertice):
    """Muestra los adyacentes del vértice."""
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, aux.info)
        aux = aux.sig


def es_adyacente(vertice, destino):
    """Determina si el destino es adyacente directo."""
    resultado = False
    aux = vertice.adyacentes.inicio
    while aux is not None and not resultado:
        if aux.destino == destino:
            resultado = True
        aux = aux.sig
    return resultado


def marcar_no_visitado(grafo):
    """Marca todos los vértices del grafo como no visitados."""
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig


def barrido_vertices(grafo):
    """Realiza un barrido de la grafo mostrando sus valores."""
    aux = grafo.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if adyacente is not None and not adyacente.visitado:
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo."""
    from collections import deque
    cola = deque()

    if vertice is not None and not vertice.visitado:
        vertice.visitado = True
        cola.append(vertice)

    while cola:
        nodo = cola.popleft()
        print(nodo.info)

        adyacentes = nodo.adyacentes.inicio
        while adyacentes is not None:
            adyacente = buscar_vertice(grafo, adyacentes.destino)
            if adyacente is not None and not adyacente.visitado:
                adyacente.visitado = True
                cola.append(adyacente)
            adyacentes = adyacentes.sig


def existe_paso(grafo, origen, destino):
    """Barrido en profundidad del grafo."""
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


def dijkstra(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    distancias = {}
    predecesores = {}
    no_visitados = []

    aux = grafo.inicio
    while aux is not None:
        nodo_nombre = aux.info
        if nodo_nombre == origen:
            distancias[nodo_nombre] = 0
            no_visitados.append([aux, 0])
        else:
            distancias[nodo_nombre] = float('inf')
            no_visitados.append([aux, float('inf')])
        predecesores[nodo_nombre] = None
        aux = aux.sig

    while no_visitados:
        no_visitados.sort(key=lambda x: x[1])
        actual, dist_actual = no_visitados.pop(0)
        actual_nombre = actual.info

        if actual_nombre == destino:
            break

        arista_aux = actual.adyacentes.inicio
        while arista_aux is not None:
            vecino_nombre = arista_aux.destino
            nueva_distancia = distancias[actual_nombre] + arista_aux.info

            if nueva_distancia < distancias.get(vecino_nombre, float('inf')):
                distancias[vecino_nombre] = nueva_distancia
                predecesores[vecino_nombre] = actual_nombre

                for i, (nodo, dist) in enumerate(no_visitados):
                    if nodo.info == vecino_nombre:
                        no_visitados[i][1] = nueva_distancia
                        break

            arista_aux = arista_aux.sig

    camino = Pila()
    actual = destino
    while actual is not None:
        camino.apilar(actual)
        actual = predecesores.get(actual)

    return camino, distancias.get(destino, float('inf'))


def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = []

    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        adyacentes = aux.adyacentes.inicio
        while adyacentes is not None:
            arista = (aux.info, adyacentes.destino, adyacentes.info)
            arista_inv = (adyacentes.destino, aux.info, adyacentes.info)
            if arista not in aristas and arista_inv not in aristas:
                aristas.append(arista)
            adyacentes = adyacentes.sig
        aux = aux.sig

    aristas.sort(key=lambda x: x[2])

    arbol = []

    for arista in aristas:
        origen, destino, peso = arista
        comp_origen = None
        comp_destino = None
        for componente in bosque:
            if origen in componente:
                comp_origen = componente
            if destino in componente:
                comp_destino = componente

        if comp_origen is not None and comp_destino is not None and comp_origen != comp_destino:
            arbol.append(arista)

            nuevo_comp = comp_origen + comp_destino
            bosque.remove(comp_origen)
            bosque.remove(comp_destino)
            bosque.append(nuevo_comp)

        if len(bosque) == 1:
            break

    return arbol


def tamanio(grafo):
    """Devuelve el número de vértices en el grafo."""
    return grafo.tamanio


def grafo_vacio(grafo):
    """Devuelve true si el grafo está vacío."""
    return grafo.inicio is None
