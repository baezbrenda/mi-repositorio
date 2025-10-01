# 2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista

class nodolista:
    def __init__(self, caracter):
        self.caracter = caracter
        self.siguiente = None


class lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, caracter):
        nuevo_nodo = nodolista(caracter)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.caracter, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar_vocales(self):
        vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while self.cabeza is not None and self.cabeza.caracter in vocales:
            self.cabeza = self.cabeza.siguiente

        actual = self.cabeza
        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.caracter in vocales:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente


# prueba
if __name__ == "__main__":
    mi_lista = lista()

    letras = ['h', 'o', 'l', 'a', 'E', 'm', 'i', 'l', 'i', 'o']
    for letra in letras:
        mi_lista.agregar(letra)

    print("Lista original:")
    mi_lista.imprimir()

    mi_lista.eliminar_vocales()

    print("Lista sin vocales:")
    mi_lista.imprimir()
