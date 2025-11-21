from tda_grafo import *
from tda_pila import *

grafo = Grafo(False)

tipos_equipos = {}

# a. Insertar vértices con nombre y tipo
print("Cargando la red de computadoras...")

insertar_vertice(grafo, 'Manjaro')
tipos_equipos['Manjaro'] = 'pc'
insertar_vertice(grafo, 'Ubuntu')
tipos_equipos['Ubuntu'] = 'pc'
insertar_vertice(grafo, 'Mint')
tipos_equipos['Mint'] = 'pc'
insertar_vertice(grafo, 'Fedora')
tipos_equipos['Fedora'] = 'pc'
insertar_vertice(grafo, 'Parrot')
tipos_equipos['Parrot'] = 'pc'

insertar_vertice(grafo, 'Red Hat')
tipos_equipos['Red Hat'] = 'notebook'
insertar_vertice(grafo, 'Debian')
tipos_equipos['Debian'] = 'notebook'
insertar_vertice(grafo, 'Arch')
tipos_equipos['Arch'] = 'notebook'

insertar_vertice(grafo, 'Guaraní')
tipos_equipos['Guaraní'] = 'servidor'
insertar_vertice(grafo, 'MongoDB')
tipos_equipos['MongoDB'] = 'servidor'

insertar_vertice(grafo, 'Switch 1')
tipos_equipos['Switch 1'] = 'switch'
insertar_vertice(grafo, 'Switch 2')
tipos_equipos['Switch 2'] = 'switch'

insertar_vertice(grafo, 'Router 1')
tipos_equipos['Router 1'] = 'router'
insertar_vertice(grafo, 'Router 2')
tipos_equipos['Router 2'] = 'router'
insertar_vertice(grafo, 'Router 3')
tipos_equipos['Router 3'] = 'router'

insertar_vertice(grafo, 'Impresora')
tipos_equipos['Impresora'] = 'impresora'

print("Conectando equipos...\n")

origen = buscar_vertice(grafo, 'Red Hat')
destino = buscar_vertice(grafo, 'Router 2')
insertar_arista(grafo, 25, origen, destino)

Origen = buscar_vertice(grafo, 'Router 2')
destino = buscar_vertice(grafo, 'Guaraní')
insertar_arista(grafo, 9, origen, destino)

origen = buscar_vertice(grafo, 'Router 2')
destino = buscar_vertice(grafo, 'Router 3')
insertar_arista(grafo, 50, origen, destino)

origen = buscar_vertice(grafo, 'Router 2')
destino = buscar_vertice(grafo, 'Router 1')
insertar_arista(grafo, 37, origen, destino)

origen = buscar_vertice(grafo, 'Router 3')
destino = buscar_vertice(grafo, 'Router 1')
insertar_arista(grafo, 43, origen, destino)

origen = buscar_vertice(grafo, 'Router 3')
destino = buscar_vertice(grafo, 'Switch 2')
insertar_arista(grafo, 61, origen, destino)

origen = buscar_vertice(grafo, 'Router 1')
destino = buscar_vertice(grafo, 'Switch 1')
insertar_arista(grafo, 29, origen, destino)

origen = buscar_vertice(grafo, 'Switch 1')
destino = buscar_vertice(grafo, 'Debian')
insertar_arista(grafo, 17, origen, destino)

origen = buscar_vertice(grafo, 'Switch 1')
destino = buscar_vertice(grafo, 'Ubuntu')
insertar_arista(grafo, 18, origen, destino)

origen = buscar_vertice(grafo, 'Switch 1')
destino = buscar_vertice(grafo, 'Impresora')
insertar_arista(grafo, 22, origen, destino)

origen = buscar_vertice(grafo, 'Switch 1')
destino = buscar_vertice(grafo, 'Mint')
insertar_arista(grafo, 80, origen, destino)

origen = buscar_vertice(grafo, 'Switch 2')
destino = buscar_vertice(grafo, 'Manjaro')
insertar_arista(grafo, 40, origen, destino)

origen = buscar_vertice(grafo, 'Switch 2')
destino = buscar_vertice(grafo, 'Fedora')
insertar_arista(grafo, 3, origen, destino)

origen = buscar_vertice(grafo, 'Switch 2')
destino = buscar_vertice(grafo, 'Arch')
insertar_arista(grafo, 56, origen, destino)

origen = buscar_vertice(grafo, 'Switch 2')
destino = buscar_vertice(grafo, 'MongoDB')
insertar_arista(grafo, 5, origen, destino)

origen = buscar_vertice(grafo, 'Switch 2')
destino = buscar_vertice(grafo, 'Parrot')
insertar_arista(grafo, 12, origen, destino)

print("Red cargada correctamente!\n")
print(f"Total de equipos: {tamanio(grafo)}")
print(f"Equipos por tipo:")
for nombre, tipo in sorted(tipos_equipos.items()):
    print(f"  {nombre}: {tipo}")

# b. Barridos desde las tres notebooks: Red Hat, Debian, Arch
print("\n" + "="*60)
print("b. BARRIDOS DESDE NOTEBOOKS")
print("="*60)

notebooks = ['Red Hat', 'Debian', 'Arch']

for notebook_nombre in notebooks:
    notebook = buscar_vertice(grafo, notebook_nombre)
    print(
        f"\n--- Desde {notebook_nombre} ({tipos_equipos[notebook_nombre]}) ---")

    print(f"Barrido en PROFUNDIDAD desde {notebook_nombre}:")
    marcar_no_visitado(grafo)
    barrido_profundidad(grafo, notebook)

    print(f"Barrido en AMPLITUD desde {notebook_nombre}:")
    marcar_no_visitado(grafo)
    barrido_amplitud(grafo, notebook)

# c. Camino más corto desde Manjaro, Red Hat, Fedora hasta la impresora
print("\n" + "="*60)
print("c. CAMINO MÁS CORTO A LA IMPRESORA")
print("="*60)

origenes = ['Manjaro', 'Red Hat', 'Fedora']

for origen_nombre in origenes:
    print(f"\nDesde {origen_nombre} a Impresora:")
    marcar_no_visitado(grafo)
    camino, peso_total = dijkstra(grafo, origen_nombre, 'Impresora')

    if camino is not None and not camino.vacia():
        print(f"Camino encontrado (peso total: {peso_total}):")
        while not camino.vacia():
            nodo = camino.desapilar()
            print(f"  -> {nodo}")
    else:
        print("  No hay camino disponible")

# d. Árbol de expansión mínima
print("\n" + "="*60)
print("d. ÁRBOL DE EXPANSIÓN MÍNIMA (Kruskal)")
print("="*60)

marcar_no_visitado(grafo)
arbol_minimo = kruskal(grafo)

print("\nÁrbol de expansión mínima:")
if arbol_minimo:
    peso_total = 0
    for origen, destino, peso in arbol_minimo:
        print(f"  {origen} -- {destino} (peso: {peso})")
        peso_total += peso
    print(f"Peso total del árbol: {peso_total}")
    print(f"Número de aristas: {len(arbol_minimo)}")
else:
    print("No se pudo calcular el árbol")

# e. PC con camino más corto al servidor Guaraní
print("\n" + "="*60)
print("e. CAMINO MÁS CORTO DESDE PCs AL SERVIDOR GUARANÍ")
print("="*60)

pcs = ['Manjaro', 'Ubuntu', 'Mint', 'Fedora', 'Parrot']

mejor_pc = None
menor_peso = float('inf')

for pc_nombre in pcs:
    marcar_no_visitado(grafo)
    camino, peso = dijkstra(grafo, pc_nombre, 'Guaraní')

    if camino is not None and not camino.vacia():
        print(f"{pc_nombre} -> Guaraní: peso {peso}")
        if peso < menor_peso:
            menor_peso = peso
            mejor_pc = pc_nombre
    else:
        print(f"{pc_nombre} -> Guaraní: No hay camino")

if mejor_pc:
    print(
        f"\n** La PC con camino más corto es: {mejor_pc} (peso: {menor_peso}) **")

# f. Computadora del Switch 1 con camino más corto a MongoDB
print("\n" + "="*60)
print("f. CAMINO MÁS CORTO DESDE EQUIPOS DEL SWITCH 1 A MONGODB")
print("="*60)

equipos_switch1 = ['Debian', 'Ubuntu', 'Mint']

mejor_equipo = None
menor_peso_mongo = float('inf')

for equipo_nombre in equipos_switch1:
    marcar_no_visitado(grafo)
    camino, peso = dijkstra(grafo, equipo_nombre, 'MongoDB')

    if camino is not None and not camino.vacia():
        print(f"{equipo_nombre} -> MongoDB: peso {peso}")
        if peso < menor_peso_mongo:
            menor_peso_mongo = peso
            mejor_equipo = equipo_nombre
    else:
        print(f"{equipo_nombre} -> MongoDB: No hay camino")

if mejor_equipo:
    print(
        f"\n** El equipo del Switch 1 con camino más corto es: {mejor_equipo} (peso: {menor_peso_mongo}) **")

# g. Cambiar impresora al Router 2 y repetir barridos
print("\n" + "="*60)
print("g. CAMBIANDO IMPRESORA AL ROUTER 2")
print("="*60)

print("\nEliminando conexión Impresora - Switch 1...")
switch1 = buscar_vertice(grafo, 'Switch 1')
impresora = buscar_vertice(grafo, 'Impresora')
if switch1 and impresora:
    arista_a_eliminar = buscar_arista(switch1, 'Impresora')
    if arista_a_eliminar:
        print("Conexión eliminada")

print("Conectando Impresora - Router 2 con peso 22...")
impresora = buscar_vertice(grafo, 'Impresora')
router2 = buscar_vertice(grafo, 'Router 2')
if impresora and router2:
    insertar_arista(grafo, 22, impresora, router2)

print("\nRepitiendo barridos desde notebooks:\n")

for notebook_nombre in notebooks:
    notebook = buscar_vertice(grafo, notebook_nombre)
    print(
        f"\n--- Desde {notebook_nombre} ({tipos_equipos[notebook_nombre]}) ---")

    print(f"Barrido en PROFUNDIDAD desde {notebook_nombre}:")
    marcar_no_visitado(grafo)
    barrido_profundidad(grafo, notebook)

    print(f"Barrido en AMPLITUD desde {notebook_nombre}:")
    marcar_no_visitado(grafo)
    barrido_amplitud(grafo, notebook)
