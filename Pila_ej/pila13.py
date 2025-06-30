class nodoPila:
    def __init__(self):
        self.info = None
        self.sig = None


class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x


def pila_vacia(pila):
    return pila.cima is None


def tamanio(pila):
    return pila.tamanio


def punto_a(pila):
    paux = Pila()
    peliculas = []
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["modelo"] == "Mark XLIV":
            peliculas.append(dato["pelicula"])
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    return peliculas


def punto_b(pila):
    paux = Pila()
    daniados = []
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["estado"] == "Dañado":
            daniados.append(dato["modelo"])
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    return daniados


def punto_c(pila):
    paux = Pila()
    destruidos = []
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["estado"] == "Destruido":
            destruidos.append(dato["modelo"])
        else:
            apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    return destruidos


def punto_e(pila):
    paux = Pila()
    existe = False
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["modelo"] == "Mark LXXXV" and dato["pelicula"] == "Avengers: Endgame":
            existe = True
        apilar(paux, dato)
    if not existe:
        nuevo = {"modelo": "Mark LXXXV",
                 "pelicula": "Avengers: Endgame", "estado": "Impecable"}
        apilar(pila, nuevo)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))


def punto_f(pila):
    paux = Pila()
    modelos = []
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if dato["pelicula"] in ["Spider-Man: Homecoming", "Capitan America: Civil War"]:
            modelos.append(dato["modelo"])
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))
    return modelos


pila_trajes = Pila()
apilar(pila_trajes, {"modelo": "Mark III",
       "pelicula": "Iron Man", "estado": "Dañado"})
apilar(pila_trajes, {"modelo": "Mark XLIV",
       "pelicula": "Avengers: Age of Ultron", "estado": "Destruido"})
apilar(pila_trajes, {"modelo": "Mark XLVI",
       "pelicula": "Capitan America: Civil War", "estado": "Dañado"})
apilar(pila_trajes, {"modelo": "Mark XLVII",
       "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"})
apilar(pila_trajes, {"modelo": "Mark L",
       "pelicula": "Avengers: Infinity War", "estado": "Destruido"})
apilar(pila_trajes, {"modelo": "Mark LXXXV",
       "pelicula": "Avengers: Endgame", "estado": "Destruido"})

print(punto_a(pila_trajes))
print(punto_b(pila_trajes))
print(punto_c(pila_trajes))
punto_e(pila_trajes)
print(punto_f(pila_trajes))
