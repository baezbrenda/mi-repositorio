class nodoArbol(object):

    def __init__(self, criatura, derrotado_por):
        self.izq = None
        self.der = None
        self.criatura = criatura
        self.derrotado_por = derrotado_por
        self.descripcion = ""
        self.capturada = ""


def insertar_nodo(raiz, dato, derrotado_por):
    if (raiz is None):
        raiz = nodoArbol(dato, derrotado_por)
    elif (dato < raiz.criatura):
        raiz.izq = insertar_nodo(raiz.izq, dato, derrotado_por)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, derrotado_por)
    return raiz


def buscar(raiz, clave):
    pos = None
    if (raiz is not None):
        if (raiz.criatura == clave):
            pos = raiz
        elif clave < raiz.criatura:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos


def remplazar(raiz):
    aux = None
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    x = None
    if (raiz is not None):
        if (clave < raiz.criatura):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.criatura):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.criatura
            if (raiz.izq is None):
                raiz = raiz.der
            elif (raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.criatura = aux.criatura
                raiz.derrotado_por = aux.derrotado_por
                raiz.descripcion = aux.descripcion
                raiz.capturada = aux.capturada
    return raiz, x


def por_nivel(raiz):

    from collections import deque
    pendientes = deque()
    pendientes.append(raiz)
    while (pendientes):
        nodo = pendientes.popleft()
        if (nodo is not None):
            print(nodo.criatura)
            if (nodo.izq is not None):
                pendientes.append(nodo.izq)
            if (nodo.der is not None):
                pendientes.append(nodo.der)

# a. listado inorden de las criaturas y quienes la derrotaron


def inorden_derrotadores(raiz):
    if (raiz is not None):
        inorden_derrotadores(raiz.izq)
        print(raiz.criatura, "- Derrotado por:", raiz.derrotado_por)
        inorden_derrotadores(raiz.der)

# b. cargar descripcion sobre cada criatura


def cargar_descripcion(raiz, criatura, descripcion):
    nodo = buscar(raiz, criatura)
    if (nodo is not None):
        nodo.descripcion = descripcion
        return True
    return False

# c. mostrar toda la informacion de la criatura Talos


def mostrar_talos(raiz):
    nodo = buscar(raiz, "Talos")
    if (nodo is not None):
        print("Criatura:", nodo.criatura)
        print("Derrotado por:", nodo.derrotado_por)
        print("Descripcion:", nodo.descripcion)
        print("Capturada por:", nodo.capturada)

# d. determinar los 3 heroes o dioses que derrotaron mayor cantidad de criaturas


def top_tres_derrotadores(raiz):
    contador = {}

    def contar(raiz_actual):
        if (raiz_actual is not None):
            if (raiz_actual.derrotado_por != "-"):
                if (raiz_actual.derrotado_por in contador):
                    contador[raiz_actual.derrotado_por] += 1
                else:
                    contador[raiz_actual.derrotado_por] = 1
            contar(raiz_actual.izq)
            contar(raiz_actual.der)
    contar(raiz)
    sorted_contador = sorted(
        contador.items(), key=lambda x: x[1], reverse=True)
    print("Top 3 derrotadores:")
    for i in range(min(3, len(sorted_contador))):
        print(f"{i+1}. {sorted_contador[i][0]}: {sorted_contador[i][1]}")

# e. listar las criaturas derrotadas por Heracles


def derrotadas_heracles(raiz):
    if (raiz is not None):
        derrotadas_heracles(raiz.izq)
        if (raiz.derrotado_por == "Heracles"):
            print(raiz.criatura)
        derrotadas_heracles(raiz.der)

# f. listar las criaturas que no han sido derrotadas


def no_derrotadas(raiz):
    if (raiz is not None):
        no_derrotadas(raiz.izq)
        if (raiz.derrotado_por == "-"):
            print(raiz.criatura)
        no_derrotadas(raiz.der)

# h. modificar capturadas por Heracles - CORREGIDO


def cargar_capturas_heracles(raiz):
    criaturas = ["Cerbero", "Toro de Creta",
                 "Cierva de Cerinea", "Jabali de Erimanto"]
    for criatura in criaturas:
        nodo = buscar(raiz, criatura)
        if (nodo is not None):
            nodo.capturada = "Heracles"
            print(f"{criatura} - capturada por Heracles")

# i. busquedas por coincidencia


def buscar_coincidencia(raiz, texto):
    if (raiz is not None):
        buscar_coincidencia(raiz.izq, texto)
        if (texto.lower() in raiz.criatura.lower()):
            print(raiz.criatura)
        buscar_coincidencia(raiz.der, texto)

# j. eliminar Basilisco y Sirenas


def eliminar_criaturas(raiz):
    raiz, _ = eliminar_nodo(raiz, "Basilisco")
    raiz, _ = eliminar_nodo(raiz, "Sirenas")
    return raiz

# k. modificar Aves del Estinfalo


def modificar_aves(raiz):
    nodo = buscar(raiz, "Aves del Estinfalo")
    if (nodo is not None):
        nodo.derrotado_por = "Heracles"

# l. modificar Ladon por Dragon Ladon - CORREGIDO


def modificar_ladon(raiz):
    nodo = buscar(raiz, "Ladon")
    if (nodo is not None):
        nodo.criatura = "Dragon Ladon"
    return raiz

# n. mostrar criaturas capturadas por Heracles


def capturadas_heracles(raiz):
    if (raiz is not None):
        capturadas_heracles(raiz.izq)
        if (raiz.capturada == "Heracles"):
            print(raiz.criatura)
        capturadas_heracles(raiz.der)


# PROGRAMA PRINCIPAL
raiz = None

# Cargar arbol
datos = [
    ("Ceto", "-"), ("Tifon", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", "-"), ("Pefredo", "-"), ("Enio", "-"), ("Escila", "-"),
    ("Caribdis", "-"), ("Euriale", "-"), ("Esteno", "-"), ("Medusa", "Perseo"),
    ("Ladon", "Heracles"), ("Aguila del Caucaso", "-"), ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"), ("Leon de Nemea",
                                     "Heracles"), ("Esfinge", "Edipo"),
    ("Dragon de la Colquida", "-"), ("Cerbero", "-"), ("Cerda de Cromion", "Teseo"),
    ("Ortro", "Heracles"), ("Toro de Creta",
                            "Teseo"), ("Jabali de Calidon", "Atalanta"),
    ("Carcinos", "-"), ("Gerion", "Heracles"), ("Cloto", "-"), ("Laquesis", "-"),
    ("Atropos", "-"), ("Minotauro de Creta", "Teseo"), ("Harpias", "-"),
    ("Argos Panoptes", "Hermes"), ("Aves del Estinfalo", "-"), ("Talos", "Medea"),
    ("Sirenas", "-"), ("Python", "Apolo"), ("Cierva de Cerinea", "-"),
    ("Basilisco", "-"), ("Jabali de Erimanto", "-")
]

for criatura, derrotado_por in datos:
    raiz = insertar_nodo(raiz, criatura, derrotado_por)

print("=== a. listado inorden de las criaturas y quienes la derrotaron ===")
inorden_derrotadores(raiz)

print("\n=== b. cargar descripcion sobre cada criatura ===")
cargar_descripcion(raiz, "Talos", "Gigante de bronce que protegia Creta")
print("Descripcion de Talos cargada")

print("\n=== c. mostrar toda la informacion de la criatura Talos ===")
mostrar_talos(raiz)

print("\n=== d. determinar los 3 heroes o dioses que derrotaron mayor cantidad de criaturas ===")
top_tres_derrotadores(raiz)

print("\n=== e. listar las criaturas derrotadas por Heracles ===")
derrotadas_heracles(raiz)

print("\n=== f. listar las criaturas que no han sido derrotadas ===")
no_derrotadas(raiz)

print("\n=== h. modificar capturadas por Heracles ===")
cargar_capturas_heracles(raiz)

print("\n=== i. busquedas por coincidencia 'Dragon' ===")
buscar_coincidencia(raiz, "Dragon")

print("\n=== j. eliminar Basilisco y Sirenas ===")
raiz = eliminar_criaturas(raiz)
print("Basilisco y Sirenas eliminados")

print("\n=== k. modificar Aves del Estinfalo ===")
modificar_aves(raiz)
print("Aves del Estinfalo modificadas")

print("\n=== l. modificar Ladon por Dragon Ladon ===")
raiz = modificar_ladon(raiz)
print("Ladon modificado a Dragon Ladon")

print("\n=== m. realizar un listado por nivel del arbol ===")
por_nivel(raiz)

print("\n=== n. mostrar las criaturas capturadas por Heracles ===")
capturadas_heracles(raiz)
