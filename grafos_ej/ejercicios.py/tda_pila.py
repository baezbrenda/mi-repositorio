class Pila:
    """Clase Pila para almacenar elementos."""

    def __init__(self):
        self.__elementos = []

    def apilar(self, dato):
        """Agrega un elemento a la pila."""
        self.__elementos.append(dato)

    def desapilar(self):
        """Elimina y devuelve el elemento en la cima."""
        if not self.vacia():
            return self.__elementos.pop()
        return None

    def vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.__elementos) == 0

    def cima(self):
        """Devuelve el elemento en la cima sin eliminarlo."""
        if not self.vacia():
            return self.__elementos[-1]
        return None

    def tamanio(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.__elementos)


def pila_vacia(pila):
    """Devuelve True si la pila está vacía."""
    return pila.vacia() if pila else True


def desapilar(pila):
    """Desapila y devuelve el elemento."""
    return pila.desapilar() if pila else None


def apilar(pila, dato):
    """Apila un elemento."""
    if pila:
        pila.apilar(dato)
