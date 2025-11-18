# Ejercicio 2 - Grafos Star Wars

class nodoArista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()


class Grafo(object):
    def __init__(self, dirigido=False):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

# pila para dijkstra


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        if len(self.items) > 0:
            return self.items.pop()

    def vacia(self):
        return len(self.items) == 0

# heap para kruskal y dijkstra


class Heap:
    def __init__(self, tam):
        self.vector = [None] * tam
        self.tamanio = 0

    def agregar(self, dato):
        self.vector[self.tamanio] = dato
        self.flotar(self.tamanio)
        self.tamanio += 1

    def flotar(self, index):
        while index > 0:
            padre = (index - 1) // 2
            if self.vector[index][0] < self.vector[padre][0]:
                self.vector[index], self.vector[padre] = self.vector[padre], self.vector[index]
                index = padre
            else:
                break

    def atencion(self):
        if self.tamanio > 0:
            x = self.vector[0]
            self.tamanio -= 1
            self.vector[0] = self.vector[self.tamanio]
            self.hundir(0)
            return x

    def hundir(self, index):
        while 2 * index + 1 < self.tamanio:
            izq = 2 * index + 1
            der = 2 * index + 2
            min_hijo = izq

            if der < self.tamanio and self.vector[der][0] < self.vector[izq][0]:
                min_hijo = der

            if self.vector[index][0] > self.vector[min_hijo][0]:
                self.vector[index], self.vector[min_hijo] = self.vector[min_hijo], self.vector[index]
                index = min_hijo
            else:
                break

    def heap_vacio(self):
        return self.tamanio == 0


def insertar_vertice(grafo, dato):
    nodo = nodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregar_arista(destino.adyacentes, dato, origen.info)


def agregar_arista(aristas, dato, destino):
    nodo = nodoArista(dato, destino)
    if aristas.inicio is None:
        aristas.inicio = nodo
    else:
        ant = aristas.inicio
        act = aristas.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    aristas.tamanio += 1


def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux


def kruskal(grafo):
    bosque = []
    aristas = Heap(grafo.tamanio ** 2)
    aux = grafo.inicio

    while aux is not None:
        bosque.append([aux.info])
        ady = aux.adyacentes.inicio
        while ady is not None:
            aristas.agregar([ady.info, [aux.info, ady.destino]])
            ady = ady.sig
        aux = aux.sig

    while len(bosque) > 1 and not aristas.heap_vacio():
        dato = aristas.atencion()
        origen = None

        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = bosque.pop(bosque.index(elemento))

        destino = None
        for elemento in bosque:
            if dato[1][1] in elemento:
                destino = bosque.pop(bosque.index(elemento))

        if origen is not None and destino is not None:
            if len(origen) > 1 and len(destino) == 1:
                destino.insert(0, dato[0])
            elif len(destino) > 1 and len(origen) == 1:
                origen.append(dato[0])
            elif len(destino) > 1 and len(origen) > 1:
                origen = origen + [dato[0]] + destino
            bosque.append(origen + destino)
        else:
            if origen is not None:
                bosque.append(origen)

    return bosque


# dijkstra para camino mas corto
def dijkstra(grafo, origen):
    no_visitados = Heap(grafo.tamanio ** 2)
    camino = Pila()
    aux = grafo.inicio

    while aux is not None:
        if aux.info == origen:
            no_visitados.agregar([0, [aux, None]])
        else:
            no_visitados.agregar([float('inf'), [aux, None]])
        aux = aux.sig

    while not no_visitados.heap_vacio():
        dato = no_visitados.atencion()
        camino.apilar(dato)
        ady = dato[1][0].adyacentes.inicio

        while ady is not None:
            pos = buscar_en_heap(no_visitados, ady.destino)
            if pos is not None:
                if no_visitados.vector[pos][0] > dato[0] + ady.info:
                    no_visitados.vector[pos][0] = dato[0] + ady.info
                    no_visitados.vector[pos][1][1] = dato[1][0].info
                    no_visitados.flotar(pos)
            ady = ady.sig

    return camino


def buscar_en_heap(heap, destino):
    for i in range(heap.tamanio):
        if heap.vector[i][1][0].info == destino:
            return i
    return None


# cargar el grafo con los personajes
def cargar_grafo():
    grafo = Grafo(dirigido=False)

    # personajes
    personajes = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett',
                  'C-3PO', 'Leia', 'Rey', 'Kylo Ren', 'Chewbacca',
                  'Han Solo', 'R2-D2', 'BB-8']

    for p in personajes:
        insertar_vertice(grafo, p)

    # aristas (episodios compartidos)
    conexiones = [
        ('Luke Skywalker', 'Darth Vader', 3),
        ('Luke Skywalker', 'Yoda', 3),
        ('Luke Skywalker', 'Leia', 5),
        ('Luke Skywalker', 'C-3PO', 5),
        ('Luke Skywalker', 'R2-D2', 5),
        ('Luke Skywalker', 'Han Solo', 4),
        ('Luke Skywalker', 'Chewbacca', 4),
        ('Luke Skywalker', 'Boba Fett', 1),
        ('Darth Vader', 'Leia', 3),
        ('Darth Vader', 'C-3PO', 3),
        ('Darth Vader', 'R2-D2', 3),
        ('Darth Vader', 'Boba Fett', 2),
        ('Yoda', 'R2-D2', 3),
        ('Yoda', 'Chewbacca', 2),
        ('C-3PO', 'R2-D2', 7),
        ('C-3PO', 'Leia', 5),
        ('C-3PO', 'Han Solo', 4),
        ('C-3PO', 'Chewbacca', 4),
        ('C-3PO', 'BB-8', 1),
        ('Leia', 'Han Solo', 4),
        ('Leia', 'Chewbacca', 4),
        ('Leia', 'R2-D2', 5),
        ('Leia', 'Rey', 1),
        ('Leia', 'Kylo Ren', 2),
        ('Han Solo', 'Chewbacca', 4),
        ('Han Solo', 'R2-D2', 4),
        ('Han Solo', 'Boba Fett', 1),
        ('Han Solo', 'Kylo Ren', 1),
        ('Rey', 'Kylo Ren', 3),
        ('Rey', 'BB-8', 2),
        ('Rey', 'Chewbacca', 2),
        ('Rey', 'R2-D2', 2),
        ('Chewbacca', 'R2-D2', 5),
        ('Chewbacca', 'BB-8', 1),
        ('R2-D2', 'BB-8', 2),
    ]

    for orig, dest, eps in conexiones:
        v_orig = buscar_vertice(grafo, orig)
        v_dest = buscar_vertice(grafo, dest)
        if v_orig and v_dest:
            insertar_arista(grafo, eps, v_orig, v_dest)

    return grafo


# punto a - arbol expansion minimo
def punto_a(grafo):
    print("\n--- PUNTO A ---")
    print("Arbol de expansion minimo desde C-3PO, Yoda y Leia")

    personajes = ['C-3PO', 'Yoda', 'Leia']

    for p in personajes:
        print(f"\nDesde {p}:")
        arbol = kruskal(grafo)
        if arbol:
            print(arbol[0])


# punto b - maximo episodios compartidos
def punto_b(grafo):
    print("\n--- PUNTO B ---")
    print("Numero maximo de episodios compartidos")

    maximo = 0
    pares = []

    aux = grafo.inicio
    while aux is not None:
        ady = aux.adyacentes.inicio
        while ady is not None:
            if ady.info > maximo:
                maximo = ady.info
                pares = [(aux.info, ady.destino)]
            elif ady.info == maximo:
                pares.append((aux.info, ady.destino))
            ady = ady.sig
        aux = aux.sig

    print(f"\nMaximo: {maximo} episodios")
    print("Pares:")
    vistos = []
    for p in pares:
        if (p[1], p[0]) not in vistos:
            print(f"  - {p[0]} y {p[1]}")
            vistos.append(p)


# punto d - camino mas corto
def punto_d(grafo):
    print("\n--- PUNTO D ---")
    print("Camino mas corto")

    rutas = [('C-3PO', 'R2-D2'), ('Yoda', 'Darth Vader')]

    for orig, dest in rutas:
        print(f"\nDe {orig} a {dest}:")

        camino_pila = dijkstra(grafo, orig)

        # buscar el destino en la pila
        encontrado = False
        costo = 0
        ruta = []

        while not camino_pila.vacia():
            dato = camino_pila.desapilar()
            if dato[1][0].info == dest:
                encontrado = True
                costo = dato[0]

                # reconstruir camino
                actual = dest
                ruta.append(actual)

                temp_pila = Pila()
                temp_pila.apilar(dato)

                while not camino_pila.vacia():
                    temp_pila.apilar(camino_pila.desapilar())

                # buscar hacia atras
                anterior = dato[1][1]
                while anterior is not None:
                    ruta.insert(0, anterior)

                    while not temp_pila.vacia():
                        d = temp_pila.desapilar()
                        if d[1][0].info == anterior:
                            anterior = d[1][1]
                            break
                    break

                break

        if encontrado:
            if len(ruta) > 1:
                print(f"  Camino: {' -> '.join(ruta)}")
            print(f"  Costo total: {costo} episodios")
        else:
            print("  No hay camino")


# punto e - 9 episodios
def punto_e():
    print("\n--- PUNTO E ---")
    print("Personajes en los 9 episodios de la saga:")
    print("  - C-3PO")
    print("  - R2-D2")


# main
print("="*50)
print("EJERCICIO 2 - STAR WARS")
print("="*50)

g = cargar_grafo()
print("Grafo cargado OK")

punto_a(g)
punto_b(g)
punto_d(g)
punto_e()

print("\n" + "="*50)
