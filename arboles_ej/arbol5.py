class nodoArbol(object):

    def __init__(self, info, es_heroe):
        self.izq = None
        self.der = None
        self.info = info
        self.es_heroe = es_heroe


def insertar_nodo(raiz, dato, es_heroe):
    if (raiz is None):
        raiz = nodoArbol(dato, es_heroe)
    elif (dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato, es_heroe)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, es_heroe)
    return raiz


def inorden(raiz):
    if (raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

# b. LISTAR LOS VILLANOS ORDENADOS ALFABÉTICAMENTE


def inorden_villanos(raiz):
    if (raiz is not None):
        inorden_villanos(raiz.izq)
        if (not raiz.es_heroe):
            print(raiz.info)
        inorden_villanos(raiz.der)

# c. MOSTRAR TODOS LOS SUPERHÉROES QUE EMPIEZAN CON C


def heroes_con_C(raiz):
    """Muestra superhéroes que empiezan con C."""
    if (raiz is not None):
        heroes_con_C(raiz.izq)
        if (raiz.es_heroe and raiz.info[0] == 'C'):
            print(raiz.info)
        heroes_con_C(raiz.der)

# d. DETERMINAR CUÁNTOS SUPERHÉROES HAY EN EL ÁRBOL


def contar_heroes(raiz):
    """Determina cuántos superhéroes hay."""
    if (raiz is None):
        return 0
    else:
        cont = 1 if raiz.es_heroe else 0
        cont += contar_heroes(raiz.izq)
        cont += contar_heroes(raiz.der)
        return cont

# e. BUSQUEDA POR PROXIMIDAD - DOCTOR STRANGE


def buscar_proximidad(raiz, clave):
    """Busca por proximidad."""
    pos = None
    if (raiz is not None):
        if ('strange' in raiz.info.lower()):
            pos = raiz
        elif (clave < raiz.info):
            pos = buscar_proximidad(raiz.izq, clave)
        else:
            pos = buscar_proximidad(raiz.der, clave)
    return pos

# f. LISTAR LOS SUPERHÉROES ORDENADOS DE MANERA DESCENDENTE


def inorden_descendente_heroes(raiz):
    """Barrido inorden descendente de héroes."""
    if (raiz is not None):
        inorden_descendente_heroes(raiz.der)
        if (raiz.es_heroe):
            print(raiz.info)
        inorden_descendente_heroes(raiz.izq)

# g. GENERAR BOSQUE


def generar_bosque(raiz):
    """Genera un bosque con héroes y villanos."""
    arbol_heroes = None
    arbol_villanos = None

    def _separar(raiz_actual):
        nonlocal arbol_heroes, arbol_villanos
        if (raiz_actual is not None):
            if (raiz_actual.es_heroe):
                arbol_heroes = insertar_nodo(
                    arbol_heroes, raiz_actual.info, True)
            else:
                arbol_villanos = insertar_nodo(
                    arbol_villanos, raiz_actual.info, False)
            _separar(raiz_actual.izq)
            _separar(raiz_actual.der)

    _separar(raiz)
    return arbol_heroes, arbol_villanos


def contar_nodos(raiz):
    """Determina cuántos nodos tiene el árbol."""
    if (raiz is None):
        return 0
    else:
        return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)


# PROGRAMA PRINCIPAL
raiz = None

# a. CARGO EL ARBOL
raiz = insertar_nodo(raiz, "Iron Man", True)
raiz = insertar_nodo(raiz, "Captain America", True)
raiz = insertar_nodo(raiz, "Thor", True)
raiz = insertar_nodo(raiz, "Black Widow", True)
raiz = insertar_nodo(raiz, "Hulk", True)
raiz = insertar_nodo(raiz, "Hawkeye", True)
raiz = insertar_nodo(raiz, "Captain Marvel", True)
raiz = insertar_nodo(raiz, "Doctor Strange", True)  # mal cargado
raiz = insertar_nodo(raiz, "Spider-Man", True)
raiz = insertar_nodo(raiz, "Black Panther", True)
raiz = insertar_nodo(raiz, "Thanos", False)
raiz = insertar_nodo(raiz, "Loki", False)
raiz = insertar_nodo(raiz, "Red Skull", False)
raiz = insertar_nodo(raiz, "Ultron", False)
raiz = insertar_nodo(raiz, "Winter Soldier", True)
raiz = insertar_nodo(raiz, "Carnage", False)
raiz = insertar_nodo(raiz, "Cable", True)

print("b. Villanos ordenados alfabeticamente:")
inorden_villanos(raiz)

print("\nc. Superheroes que empiezan con C:")
heroes_con_C(raiz)

print(f"\nd. Cantidad de superheroes: {contar_heroes(raiz)}")

print("\ne. Buscar y corregir Doctor Strange:")
nodo = buscar_proximidad(raiz, "Doctor Strange")
if (nodo is not None):
    nodo.info = "Doctor Strange"
    print("Doctor Strange corregido")

print("\nf. Superheroes orden descendente:")
inorden_descendente_heroes(raiz)

print("\ng. Generar bosque:")
arbol_heroes, arbol_villanos = generar_bosque(raiz)

print(f"g.I. Nodos arbol heroes: {contar_nodos(arbol_heroes)}")
print(f"g.I. Nodos arbol villanos: {contar_nodos(arbol_villanos)}")

print("\ng.II. Barrido ordenado arbol heroes:")
inorden(arbol_heroes)

print("\ng.II. Barrido ordenado arbol villanos:")
inorden(arbol_villanos)
