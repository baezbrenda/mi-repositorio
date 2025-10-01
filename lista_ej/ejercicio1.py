class NodoLista:
    """Clase nodo lista"""
    info, sig = None, None


class Lista:
    """Clase lista simplemente enlazada"""

    def _init_(self):
        """Crea una lista vacía"""
        self.inicio = None
        self.tamanio = 0

# funcion principal


def contar_nodos(lista):
    contador = 0
    actual = lista.inicio

# recorro la lista
    while actual is not None:
        contador += 1
        actual = actual.sig

    return contador

# codigo para probar


if __name__ == "__main__":
    mi_lista = Lista()

    nodo1 = NodoLista()
    nodo1.info = "Manzana"

    nodo2 = NodoLista()
    nodo2.info = "Banana"

    nodo3 = NodoLista()
    nodo3.info = "Pera"

    mi_lista.inicio = nodo1
    nodo1.sig = nodo2
    nodo2.sig = nodo3

    resultado = contar_nodos(mi_lista)
    print(f"La lista tiene {resultado} nodos")
