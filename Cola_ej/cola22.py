class nodoCola(object):
    def __init__(self, info=None):
        self.info = info
        self.sig = None


class Cola(object):
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, dato):
    nodo = nodoCola(dato)
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    return cola.frente is None


def personaje_de_capitana_marvel(cola):
    caux = Cola()
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["superheroe"] == "Capitana Marvel":
            print("a) El personaje de Capitana Marvel es:", dato["personaje"])
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def superheroes_femeninos(cola):
    caux = Cola()
    print("b) Superhéroes femeninos:")
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["genero"] == "F":
            print("-", dato["superheroe"])
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def personajes_masculinos(cola):
    caux = Cola()
    print("c) Personajes masculinos:")
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["genero"] == "M":
            print("-", dato["personaje"])
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def superheroe_de_scott_lang(cola):
    caux = Cola()
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["personaje"] == "Scott Lang":
            print("d) El superhéroe de Scott Lang es:", dato["superheroe"])
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def datos_con_s(cola):
    caux = Cola()
    print("e) Datos de personajes o superhéroes que comienzan con 'S':")
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print("-", dato)
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def buscar_carol_danvers(cola):
    caux = Cola()
    encontrado = False
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["personaje"] == "Carol Danvers":
            print("f) Carol Danvers está en la cola. Su superhéroe es:",
                  dato["superheroe"])
            encontrado = True
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))
    if not encontrado:
        print("f) Carol Danvers no está en la cola.")


mcu = Cola()
arribo(mcu, {"personaje": "Tony Stark",
       "superheroe": "Iron Man", "genero": "M"})
arribo(mcu, {"personaje": "Steve Rogers",
       "superheroe": "Capitán América", "genero": "M"})
arribo(mcu, {"personaje": "Natasha Romanoff",
       "superheroe": "Black Widow", "genero": "F"})
arribo(mcu, {"personaje": "Carol Danvers",
       "superheroe": "Capitana Marvel", "genero": "F"})
arribo(mcu, {"personaje": "Scott Lang",
       "superheroe": "Ant-Man", "genero": "M"})
arribo(mcu, {"personaje": "Stephen Strange",
       "superheroe": "Doctor Strange", "genero": "M"})

personaje_de_capitana_marvel(mcu)
superheroes_femeninos(mcu)
personajes_masculinos(mcu)
superheroe_de_scott_lang(mcu)
datos_con_s(mcu)
buscar_carol_danvers(mcu)
