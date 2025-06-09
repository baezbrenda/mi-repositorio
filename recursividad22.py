def usar_la_fuerza(mochila):
    if not mochila:
        return False, 0
    if mochila[0] == "sable de luz":
        return True, 1
    encontrado, cantidad = usar_la_fuerza(mochila[1:])
    return encontrado, cantidad + 1


mochila = ["comunicador", "comida", "botiquín", "sable de luz", "manto"]

encontrado, sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"Sable de luz encontrado tras sacar {sacados} objetos.")
else:
    print("No se encontró ningún sable de luz en la mochila.")
