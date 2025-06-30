superheroes = [
    "Iron Man", "Spider-Man", "Hulk", "Thor", "Doctor Strange", "Black Widow", "Scarlet Witch", "Falcon", "Vision", "Ant-Man",
    "Capitan America", "Black Panther", "Star-Lord", "Gamora", "Rocket Raccoon"
]


def buscar_capitan(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return buscar_capitan(lista, indice + 1)


def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return []
    return [lista[indice]] + listar_superheroes(lista, indice + 1)


print(
    f"¿Se encuentra el Capitán América en la lista?) {buscar_capitan(superheroes)}")
print("Lista de superheroes:", listar_superheroes(superheroes))
