import copy


def criterio(dato, campo=None):
    """Retorna el valor del campo especificado para la comparación."""
    if campo is None:
        return dato
    if hasattr(dato, '__dict__') and campo in dato.__dict__:
        return dato.__dict__[campo]
    return dato


class nodoLista(object):
    """Clase nodo lista."""

    def __init__(self, info, sig=None):
        self.info = info
        self.sig = sig


class Lista(object):
    """Clase lista simplemente enlazada."""

    def __init__(self):
        self.inicio = None
        self.tamano = 0


class Jedi:
    """Clase para representar a un Jedi."""

    def __init__(self, nombre, especie, maestros, colores_sable):
        self.nombre = nombre
        self.especie = especie
        self.maestros = maestros
        self.colores_sable = colores_sable

    def __str__(self):
        maestros_str = ", ".join(
            self.maestros) if self.maestros else "Ninguno/Desconocido"
        sables_str = ", ".join(self.colores_sable)
        return (f"Jedi: {self.nombre} (Especie: {self.especie}) | "
                f"Maestros: [{maestros_str}] | Sables: [{sables_str}]")


def insertar(lista, dato, campo=None):
    """Inserta un dato en la lista ordenado por el campo especificado."""
    nodo = nodoLista(dato)
    if lista.inicio is None or criterio(lista.inicio.info, campo) > criterio(dato, campo):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and criterio(act.info, campo) < criterio(dato, campo):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1


def buscar(lista, clave, campo=None):
    """Devuelve el nodo que contiene el elemento buscado por clave y campo."""
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != criterio(clave, campo):
        aux = aux.sig
    return aux


def barrido(lista):
    """Realiza un recorrido de la lista mostrando sus valores."""
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


def copiar_lista_y_ordenar(lista_original, campo_orden):
    """Crea una nueva lista ordenada a partir de los elementos de la lista original."""
    nueva_lista = Lista()
    aux = lista_original.inicio
    while aux is not None:
        insertar(nueva_lista, copy.copy(aux.info), campo=campo_orden)
        aux = aux.sig
    return nueva_lista


jedi_data = [
    ("Yoda", "Desconocida", ["Desconocido"], ["Verde"]),
    ("Luke Skywalker", "Humana", [
     "Obi-Wan Kenobi", "Yoda"], ["Azul", "Verde"]),
    ("Ahsoka Tano", "Togruta", ["Anakin Skywalker"], ["Blanco", "Amarillo"]),
    ("Kit Fisto", "Nautolan", ["Desconocido"], ["Verde"]),
    ("Mace Windu", "Humana", ["Yoda"], ["Púrpura"]),
    ("Qui-Gon Jinn", "Humana", ["Dooku"], ["Verde"]),
    ("Aayla Secura", "Twi'lek", ["Quinlan Vos"], ["Azul"]),
    ("Shaak Ti", "Togruta", ["Desconocido"], ["Azul", "Verde"]),
    ("Dooku", "Humana", ["Yoda"], ["Azul", "Rojo"]),
    ("Obi-Wan Kenobi", "Humana", ["Qui-Gon Jinn"], ["Azul"]),
    ("Anakin Skywalker", "Humana", ["Obi-Wan Kenobi"], ["Azul"])
]

lista_jedi = Lista()

for nombre, especie, maestros, sables in jedi_data:
    jedi = Jedi(nombre, especie, maestros, sables)
    insertar(lista_jedi, jedi, campo='nombre')

print("--- EJECUCIÓN DE ACTIVIDADES REQUERIDAS (Jedi) ---")

print("\na. Listado ordenado por Nombre:")
barrido(lista_jedi)

print("\n   Listado ordenado por Especie:")
lista_por_especie = copiar_lista_y_ordenar(lista_jedi, 'especie')
barrido(lista_por_especie)

print("\nb. Información completa de Ahsoka Tano y Kit Fisto:")
jedi_b = ["Ahsoka Tano", "Kit Fisto"]
for nombre_jedi in jedi_b:
    nodo = buscar(lista_jedi, nombre_jedi, campo='nombre')
    if nodo:
        print(f"   -> {nodo.info}")

print("\nc. Padawans de Yoda y Luke Skywalker:")
maestros_c = ["Yoda", "Luke Skywalker"]
aux = lista_jedi.inicio
padawans_c = []
while aux is not None:
    if any(m in aux.info.maestros for m in maestros_c):
        padawans_c.append(aux.info.nombre)
    aux = aux.sig
print(f"   -> {', '.join(padawans_c)}")

print("\nd. Jedi de especie Humana y Twi'lek:")
especies_d = ["Humana", "Twi'lek"]
aux = lista_jedi.inicio
jedi_d = []
while aux is not None:
    if aux.info.especie in especies_d:
        jedi_d.append(f"{aux.info.nombre} ({aux.info.especie})")
    aux = aux.sig
print(f"   -> {', '.join(jedi_d)}")


print("\ne. Jedi que comienzan con 'A':")
aux = lista_jedi.inicio
jedi_e = []
while aux is not None:
    if aux.info.nombre.startswith('A'):
        jedi_e.append(aux.info.nombre)
    aux = aux.sig
print(f"   -> {', '.join(jedi_e)}")

print("\nf. Jedi que usaron sable de más de un color:")
aux = lista_jedi.inicio
jedi_f = []
while aux is not None:
    if len(aux.info.colores_sable) > 1:
        jedi_f.append(
            f"{aux.info.nombre} ({', '.join(aux.info.colores_sable)})")
    aux = aux.sig
print(f"   -> {'; '.join(jedi_f)}")

print("\ng. Jedi con sable Amarillo o Púrpura/Violeta:")
colores_g = ["Amarillo", "Púrpura", "Violeta"]
aux = lista_jedi.inicio
jedi_g = []
while aux is not None:
    if any(color in aux.info.colores_sable for color in colores_g):
        jedi_g.append(aux.info.nombre)
    aux = aux.sig
print(f"   -> {', '.join(jedi_g)}")

print("\nh. Padawans de Qui-Gon Jinn y Mace Windu:")
maestros_h = ["Qui-Gon Jinn", "Mace Windu"]
aux = lista_jedi.inicio
padawans_h = []
while aux is not None:
    if any(m in aux.info.maestros for m in maestros_h):
        padawans_h.append(aux.info.nombre)
    aux = aux.sig
print(f"   -> {', '.join(padawans_h)}")
