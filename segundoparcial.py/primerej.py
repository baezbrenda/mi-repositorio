class nodoArbol(object):
    """Clase nodo árbol"""

    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0
        self.otro_dato = None


def insertar_nodo(raiz, dato, pokemon=None):
    """Inserta un dato al árbol."""
    if raiz is None:
        raiz = nodoArbol(dato)
        raiz.otro_dato = pokemon
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato, pokemon)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, pokemon)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz


def altura(raiz):
    """Devuelve la altura de un nodo."""
    if raiz is None:
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    """Actualiza la altura de un nodo."""
    if raiz is not None:
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(raiz, control):
    """Realiza una rotación simple de nodos a la derecha o a la izquierda."""
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz


def rotar_doble(raiz, control):
    """Realiza una rotación doble de nodos a la derecha o a la izquierda."""
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    """Determina la rotación hay que hacer para balancear el árbol."""
    if raiz is not None:
        if altura(raiz.izq) - altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif altura(raiz.der) - altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz


def inorden(raiz):
    """Realiza el barrido inorden del árbol."""
    if raiz is not None:
        inorden(raiz.izq)
        if raiz.otro_dato:
            print(raiz.otro_dato)
        else:
            print(raiz.info)
        inorden(raiz.der)


def buscar(raiz, clave):
    """Devuelve la dirección del elemento buscado."""
    pos = None
    if raiz is not None:
        if raiz.info == clave:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos


class Cola(object):
    def __init__(self):
        self.elementos = []


def arribo(cola, dato):
    cola.elementos.append(dato)


def atencion(cola):
    return cola.elementos.pop(0)


def cola_vacia(cola):
    return len(cola.elementos) == 0


def por_nivel(raiz):
    """Realiza el barrido por nivel del árbol."""
    pendientes = Cola()
    arribo(pendientes, raiz)
    while not cola_vacia(pendientes):
        nodo = atencion(pendientes)
        if nodo.otro_dato:
            print(nodo.otro_dato)
        else:
            print(nodo.info)
        if nodo.izq is not None:
            arribo(pendientes, nodo.izq)
        if nodo.der is not None:
            arribo(pendientes, nodo.der)


class Pokemon:
    def __init__(self, nombre, numero, tipos, debilidades, tiene_mega=False, tiene_gigamax=False):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos
        self.debilidades = debilidades
        self.tiene_mega = tiene_mega
        self.tiene_gigamax = tiene_gigamax

    def __str__(self):
        tipos_str = ", ".join(self.tipos)
        return (f"Nº{self.numero:03d} - {self.nombre:15s} | Tipos: {tipos_str:25s} | "
                f"Mega: {'Sí' if self.tiene_mega else 'No':2s} | Gigamax: {'Sí' if self.tiene_gigamax else 'No'}")


# Inicialización de los tres árboles
arbol_nombre = None
arbol_numero = None
arbol_tipo = None

# Lista de pokémons
lista_pokemones = [
    Pokemon("Bulbasaur", 1, ["Planta", "Veneno"], [
            "Fuego", "Psíquico", "Volador", "Hielo"]),
    Pokemon("Charmander", 4, ["Fuego"], ["Agua", "Tierra", "Roca"]),
    Pokemon("Charizard", 6, ["Fuego", "Volador"], [
            "Agua", "Eléctrico", "Roca"], True, True),
    Pokemon("Squirtle", 7, ["Agua"], ["Planta", "Eléctrico"]),
    Pokemon("Pikachu", 25, ["Eléctrico"], ["Tierra"], False, True),
    Pokemon("Gengar", 94, ["Fantasma", "Veneno"], [
            "Fantasma", "Siniestro", "Psíquico", "Tierra"], True),
    Pokemon("Jolteon", 135, ["Eléctrico"], ["Tierra"]),
    Pokemon("Steelix", 208, ["Acero", "Tierra"], [
            "Fuego", "Agua", "Lucha", "Tierra"], True),
    Pokemon("Metagross", 376, ["Acero", "Psíquico"], [
            "Fuego", "Tierra", "Fantasma", "Siniestro"], True),
    Pokemon("Lucario", 448, ["Lucha", "Acero"],
            ["Fuego", "Lucha", "Tierra"], True),
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"], [
            "Lucha", "Tierra", "Acero", "Hielo", "Dragón", "Hada"]),
    Pokemon("Lycanroc", 745, ["Roca"], [
            "Agua", "Planta", "Lucha", "Tierra", "Acero"]),
    Pokemon("Corviknight", 823, ["Acero", "Volador"], [
            "Fuego", "Eléctrico"], False, True),
    Pokemon("Toxtricity", 849, ["Eléctrico", "Veneno"], [
            "Tierra", "Psíquico"], False, True),
    Pokemon("Dragapult", 887, ["Dragón", "Fantasma"], [
            "Fantasma", "Siniestro", "Hada", "Hielo", "Dragón"]),
]

print("=" * 90)
print("EJERCICIO 1 - SISTEMA DE POKÉMONS")
print("=" * 90)

# a) Cargar los tres árboles
print("\na) Cargando árboles...")
for pokemon in lista_pokemones:
    # Árbol por nombre - info guarda el nombre, otro_dato guarda el pokemon
    arbol_nombre = insertar_nodo(arbol_nombre, pokemon.nombre, pokemon)

    # Árbol por número - info guarda el número, otro_dato guarda el pokemon
    arbol_numero = insertar_nodo(arbol_numero, pokemon.numero, pokemon)

    # Árbol por tipo - info guarda el tipo, otro_dato guarda lista de pokémons
    for tipo in pokemon.tipos:
        nodo_tipo = buscar(arbol_tipo, tipo)
        if nodo_tipo:
            # El tipo ya existe, agregar pokemon a la lista
            nodo_tipo.otro_dato.append(pokemon)
        else:
            # Crear nuevo nodo para este tipo
            arbol_tipo = insertar_nodo(arbol_tipo, tipo, [pokemon])

print("✓ Árboles cargados exitosamente!")
print(f"✓ Total de pokémons: {len(lista_pokemones)}")

# b) Búsqueda por número y nombre (con proximidad)
print("\n" + "=" * 90)
print("b) BÚSQUEDA DE POKÉMON")
print("=" * 90)

# Búsqueda por número
print("\n→ Búsqueda por número 25:")
nodo_numero = buscar(arbol_numero, 25)
if nodo_numero:
    print(f"  {nodo_numero.otro_dato}")
else:
    print("  No encontrado")

# Búsqueda por nombre exacto
print("\n→ Búsqueda por nombre exacto 'Jolteon':")
nodo_nombre = buscar(arbol_nombre, "Jolteon")
if nodo_nombre:
    print(f"  {nodo_nombre.otro_dato}")
else:
    print("  No encontrado")

# Búsqueda por proximidad


def buscar_proximidad(raiz, texto):
    """Busca pokémons cuyo nombre contenga el texto dado"""
    resultados = []

    def buscar_rec(nodo):
        if nodo is not None:
            buscar_rec(nodo.izq)
            if texto.lower() in nodo.info.lower():
                resultados.append(nodo.otro_dato)
            buscar_rec(nodo.der)

    buscar_rec(raiz)
    return resultados


print(f"\n→ Búsqueda por proximidad 'bul':")
resultados = buscar_proximidad(arbol_nombre, "bul")
if resultados:
    for poke in resultados:
        print(f"  {poke}")
else:
    print("  No se encontraron coincidencias")

print(f"\n→ Búsqueda por proximidad 'char':")
resultados = buscar_proximidad(arbol_nombre, "char")
if resultados:
    for poke in resultados:
        print(f"  {poke}")
else:
    print("  No se encontraron coincidencias")

# c) Pokémons por tipo específico
print("\n" + "=" * 90)
print("c) MOSTRAR NOMBRES DE POKÉMONS DE TIPOS ESPECÍFICOS")
print("=" * 90)

tipos_buscar = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos_buscar:
    print(f"\n→ Pokémons de tipo {tipo}:")
    nodo_tipo = buscar(arbol_tipo, tipo)
    if nodo_tipo:
        for poke in nodo_tipo.otro_dato:
            print(f"  • {poke.nombre}")
    else:
        print("  No hay pokémons de este tipo")

# d) Listados ordenados
print("\n" + "=" * 90)
print("d) LISTADOS ORDENADOS")
print("=" * 90)

print("\n→ Listado ascendente por número:")
inorden(arbol_numero)

print("\n→ Listado ascendente por nombre:")
inorden(arbol_nombre)

print("\n→ Listado por nivel por nombre:")
por_nivel(arbol_nombre)

# e) Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum
print("\n" + "=" * 90)
print("e) POKÉMONS DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM")
print("=" * 90)

# Obtener tipos de ataque de los tres pokémons
tipos_ataque = []
atacantes = ["Jolteon", "Lycanroc", "Tyrantrum"]

print("\n→ Tipos de ataque de cada pokémon:")
for nombre_atacante in atacantes:
    nodo_atacante = buscar(arbol_nombre, nombre_atacante)
    if nodo_atacante:
        pokemon_atacante = nodo_atacante.otro_dato
        print(f"  • {nombre_atacante}: {', '.join(pokemon_atacante.tipos)}")
        for tipo in pokemon_atacante.tipos:
            if tipo not in tipos_ataque:
                tipos_ataque.append(tipo)

print(f"\n→ Tipos de ataque combinados: {', '.join(sorted(tipos_ataque))}")


def encontrar_debiles(raiz, tipos_ataque):
    """Encuentra pokémons débiles a los tipos de ataque dados"""
    debiles = []

    def buscar_rec(nodo):
        if nodo is not None:
            buscar_rec(nodo.izq)
            pokemon = nodo.otro_dato
            # Verificar si alguna debilidad coincide con tipos de ataque
            for debilidad in pokemon.debilidades:
                encontrado = False
                for tipo in tipos_ataque:
                    if debilidad == tipo:
                        encontrado = True
                        break
                if encontrado:
                    debiles.append(pokemon)
                    break
            buscar_rec(nodo.der)

    buscar_rec(raiz)
    return debiles


pokemones_debiles = encontrar_debiles(arbol_numero, tipos_ataque)
print(f"\n→ Pokémons débiles encontrados: {len(pokemones_debiles)}")
for poke in pokemones_debiles:
    debilidades_comunes = []
    for d in poke.debilidades:
        for t in tipos_ataque:
            if d == t:
                debilidades_comunes.append(d)
    print(f"  • {poke.nombre:15s} → Débil a: {', '.join(debilidades_comunes)}")

# f) Mostrar todos los tipos y cantidad de cada uno
print("\n" + "=" * 90)
print("f) TODOS LOS TIPOS DE POKÉMONS Y CANTIDAD")
print("=" * 90)

conteo = {}


def contar_tipos_arbol(raiz):
    """Cuenta cuántos pokémons hay de cada tipo"""
    if raiz is not None:
        contar_tipos_arbol(raiz.izq)
        pokemon = raiz.otro_dato
        for tipo in pokemon.tipos:
            if tipo in conteo:
                conteo[tipo] = conteo[tipo] + 1
            else:
                conteo[tipo] = 1
        contar_tipos_arbol(raiz.der)


contar_tipos_arbol(arbol_numero)

# Ordenar el diccionario
tipos_ordenados = sorted(conteo.items())

print("\n→ Conteo por tipo:")
for tipo, cantidad in tipos_ordenados:
    print(f"  • {tipo:15s}: {cantidad} pokémon(s)")

print(f"\n→ Total de tipos diferentes: {len(conteo)}")

# g) Determinar cuántos pokémons tienen megaevolución
print("\n" + "=" * 90)
print("g) POKÉMONS CON MEGAEVOLUCIÓN")
print("=" * 90)


def contar_mega(raiz):
    """Cuenta pokémons con megaevolución"""
    contador = 0
    lista_mega = []

    def contar_rec(nodo):
        if nodo is not None:
            resultado_izq = contar_rec(nodo.izq)
            contador_izq = resultado_izq[0]
            lista_izq = resultado_izq[1]

            pokemon = nodo.otro_dato
            contador_actual = 0
            lista_actual = []
            if pokemon.tiene_mega:
                contador_actual = 1
                lista_actual = [pokemon.nombre]

            resultado_der = contar_rec(nodo.der)
            contador_der = resultado_der[0]
            lista_der = resultado_der[1]

            total = contador_izq + contador_actual + contador_der
            lista_total = lista_izq + lista_actual + lista_der
            return [total, lista_total]
        else:
            return [0, []]

    resultado = contar_rec(raiz)
    return resultado[0], resultado[1]


total_mega, lista_mega = contar_mega(arbol_numero)
print(f"\n→ Total de pokémons con megaevolución: {total_mega}")
print(f"→ Pokémons: {', '.join(lista_mega)}")

# h) Determinar cuántos pokémons tienen forma Gigamax
print("\n" + "=" * 90)
print("h) POKÉMONS CON FORMA GIGAMAX")
print("=" * 90)


def contar_gigamax(raiz):
    """Cuenta pokémons con forma Gigamax"""
    contador = 0
    lista_gigamax = []

    def contar_rec(nodo):
        if nodo is not None:
            resultado_izq = contar_rec(nodo.izq)
            contador_izq = resultado_izq[0]
            lista_izq = resultado_izq[1]

            pokemon = nodo.otro_dato
            contador_actual = 0
            lista_actual = []
            if pokemon.tiene_gigamax:
                contador_actual = 1
                lista_actual = [pokemon.nombre]

            resultado_der = contar_rec(nodo.der)
            contador_der = resultado_der[0]
            lista_der = resultado_der[1]

            total = contador_izq + contador_actual + contador_der
            lista_total = lista_izq + lista_actual + lista_der
            return [total, lista_total]
        else:
            return [0, []]

    resultado = contar_rec(raiz)
    return resultado[0], resultado[1]


total_gigamax, lista_gigamax = contar_gigamax(arbol_numero)
print(f"\n→ Total de pokémons con forma Gigamax: {total_gigamax}")
print(f"→ Pokémons: {', '.join(lista_gigamax)}")

print("\n" + "=" * 90)
print("✓ EJERCICIO COMPLETADO")
print("=" * 90)
