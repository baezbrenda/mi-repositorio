class NodoPila:
    def __init__(self):
        self.info = None
        self.sig = None


class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    nodo = NodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    if pila.cima:
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x
    return None


def pila_vacia(pila):
    return pila.cima is None


def encontrar_posicion(pila, nombres):
    paux = Pila()
    posiciones = {}
    posicion = 1

    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["nombre"] in nombres:
            posiciones[dato["nombre"]] = posicion
        apilar(paux, dato)
        posicion += 1

    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

    return posiciones


def mas_de_cinco_peliculas(pila):
    paux = Pila()
    personajes = []

    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["peliculas"] > 5:
            personajes.append((dato["nombre"], dato["peliculas"]))
        apilar(paux, dato)

    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

    return personajes


def peliculas_viuda_negra(pila):
    paux = Pila()
    cantidad = 0

    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["nombre"] == "Black Widow":
            cantidad = dato["peliculas"]
        apilar(paux, dato)

    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

    return cantidad


def personajes_por_letra(pila):
    paux = Pila()
    nombres_filtrados = []

    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["nombre"][0] in ["C", "D", "G"]:
            nombres_filtrados.append(dato["nombre"])
        apilar(paux, dato)

    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))

    return nombres_filtrados


pila_personajes = Pila()
apilar(pila_personajes, {"nombre": "Iron Man", "peliculas": 10})
apilar(pila_personajes, {"nombre": "Captain America", "peliculas": 9})
apilar(pila_personajes, {"nombre": "Black Widow", "peliculas": 7})
apilar(pila_personajes, {"nombre": "Rocket Raccoon", "peliculas": 4})
apilar(pila_personajes, {"nombre": "Groot", "peliculas": 3})
apilar(pila_personajes, {"nombre": "Doctor Strange", "peliculas": 2})
apilar(pila_personajes, {"nombre": "Gamora", "peliculas": 6})

print(encontrar_posicion(pila_personajes, ["Rocket Raccoon", "Groot"]))
print(mas_de_cinco_peliculas(pila_personajes))
print(peliculas_viuda_negra(pila_personajes))
print(personajes_por_letra(pila_personajes))
