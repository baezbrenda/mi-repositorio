movimientos = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}


def contar_movimientos(n):
    """Calcula el número de movimientos válidos en n pasos"""
    posibilidades = [1] * 10
    for _ in range(n):
        nuevas_posibilidades = [0] * 10
        for numero in range(10):
            for destino in movimientos[numero]:
                nuevas_posibilidades[destino] += posibilidades[numero]
        posibilidades = nuevas_posibilidades

    return sum(posibilidades)


movimientos_a_probar = [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]

print(f"{'Movimientos':<12} | {'Posibilidades':<12}")
print("-" * 27)
for mov in movimientos_a_probar:
    total = contar_movimientos(mov)
    print(f"{mov:<12} | {total:<12}")
