class nodoCola(object):
    """Clase nodo de una cola."""

    def __init__(self, info=None):
        self.info = info
        self.sig = None


class Cola(object):
    """Clase Cola."""

    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, dato):
    """Agrega un elemento al final de la cola."""
    nodo = nodoCola(dato)
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def atencion(cola):
    """Atiende el elemento del frente de la cola y lo devuelve."""
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    """Devuelve True si la cola está vacía."""
    return cola.frente is None


class nodoPila(object):
    """Clase nodo de una pila."""

    def __init__(self, info=None):
        self.info = info
        self.sig = None


class Pila(object):
    """Clase Pila."""

    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    """Agrega un elemento a la pila."""
    nodo = nodoPila(dato)
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    """Elimina el elemento de la cima de la pila y lo devuelve."""
    dato = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return dato


def pila_vacia(pila):
    """Devuelve True si la pila está vacía."""
    return pila.cima is None


def tamanio_pila(pila):
    """Devuelve la cantidad de elementos en la pila."""
    return pila.tamanio


def eliminar_facebook(cola):
    """Elimina todas las notificaciones de Facebook de la cola."""
    caux = Cola()
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["app"] != "Facebook":
            arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def mostrar_twitter_python(cola):
    """Muestra notificaciones de Twitter que contienen 'Python', sin perder datos."""
    caux = Cola()
    while not cola_vacia(cola):
        dato = atencion(cola)
        if dato["app"] == "Twitter" and "Python" in dato["mensaje"]:
            print(dato)
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))


def contar_notificaciones_entre_horas(cola):
    """Guarda en una pila las notificaciones entre las 11:43 y las 15:57 y muestra cuántas son."""
    pila = Pila()
    caux = Cola()
    while not cola_vacia(cola):
        dato = atencion(cola)
        if "11:43" <= dato["hora"] <= "15:57":
            apilar(pila, dato)
        arribo(caux, dato)
    while not cola_vacia(caux):
        arribo(cola, atencion(caux))
    print("Cantidad de notificaciones entre 11:43 y 15:57:", tamanio_pila(pila))


notificaciones = Cola()
arribo(notificaciones, {"hora": "11:00", "app": "Facebook",
       "mensaje": "Tienes una nueva sugerencia de amistad"})
arribo(notificaciones, {"hora": "12:30", "app": "Twitter",
       "mensaje": "Nuevo tweet sobre Python"})
arribo(notificaciones, {"hora": "14:15", "app": "Instagram",
       "mensaje": "Tienes un nuevo seguidor"})
arribo(notificaciones, {"hora": "15:45", "app": "Twitter",
       "mensaje": "Python es tendencia hoy"})
arribo(notificaciones, {"hora": "16:00", "app": "Facebook",
       "mensaje": "Nueva reacción a tu publicación"})

print("\n---- a) Eliminar notificaciones de Facebook ----")
eliminar_facebook(notificaciones)

print("\n---- b) Mostrar notificaciones de Twitter con 'Python' ----")
mostrar_twitter_python(notificaciones)

print("\n---- c) Contar notificaciones entre 11:43 y 15:57 ----")
contar_notificaciones_entre_horas(notificaciones)
