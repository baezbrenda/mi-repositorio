def criterio(dato, campo=None):
    if campo is None:
        return dato
    if hasattr(dato, '__dict__') and campo in dato.__dict__:
        return dato.__dict__[campo]
    return dato


class nodoLista(object):
    def __init__(self, info, sig=None):
        self.info = info
        self.sig = sig


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamano = 0


class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return (f"Nombre: {self.nombre} | Aparición: {self.anio_aparicion} | "
                f"Casa: {self.casa_comic} | Biografía: {self.biografia[:40]}...")


def insertar(lista, dato, campo=None):
    nodo = nodoLista(dato)
    if lista.inicio is None or criterio(lista.inicio.info, campo) > criterio(dato, campo):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and criterio(act.info, campo) < criterio(dato, campo):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1


def eliminar(lista, clave, campo=None):
    dato = None
    if lista.inicio is not None and criterio(lista.inicio.info, campo) == criterio(clave, campo):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamano -= 1
        return dato
    anterior = lista.inicio
    actual = lista.inicio.sig
    while actual is not None and criterio(actual.info, campo) != criterio(clave, campo):
        anterior = anterior.sig
        actual = actual.sig
    if actual is not None:
        dato = actual.info
        anterior.sig = actual.sig
        lista.tamano -= 1
    return dato


def buscar(lista, clave, campo=None):
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != criterio(clave, campo):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


superheroes_data = [
    ("Linterna Verde", 1940, "DC",
     "Alan Scott, el primer Linterna Verde, es un ingeniero."),
    ("Wolverine", 1974, "Marvel",
     "Mutante con esqueleto de adamantium y garras. No usa traje."),
    ("Dr. Strange", 1963, "Marvel",
     "El Hechicero Supremo, un ex-cirujano. Utiliza un traje místico."),
    ("Capitana Marvel", 1968, "Marvel",
     "Carol Danvers, una piloto de la Fuerza Aérea."),
    ("Mujer Maravilla", 1941, "DC",
     "Diana, una amazona con gran armadura y lazo de la verdad."),
    ("Flash", 1940, "DC", "El hombre más rápido del mundo. Su traje lo protege."),
    ("Star-Lord", 1976, "Marvel", "Peter Quill, líder de los Guardianes de la Galaxia."),
    ("Batman", 1939, "DC", "El Caballero Oscuro. Lleva un traje avanzado con bat-gadgets."),
    ("Superman", 1938, "DC", "El Hombre de Acero, enviado a la Tierra desde Krypton."),
    ("Iron Man", 1963, "Marvel",
     "Tony Stark, usa una armadura de alta tecnología como traje."),
    ("Spider-Man", 1962, "Marvel",
     "Peter Parker, un joven que usa un traje rojo y azul.")
]

lista_superheroes = Lista()

for nombre, anio, casa, bio in superheroes_data:
    heroe = Superheroe(nombre, anio, casa, bio)
    insertar(lista_superheroes, heroe, campo='nombre')

print("--- EJECUCIÓN DE ACTIVIDADES REQUERIDAS ---")

# a. eliminar el nodo que contiene la información de Linterna Verde;
heroe_eliminado = eliminar(lista_superheroes, "Linterna Verde", campo='nombre')
print(
    f"\na. Eliminado: {heroe_eliminado.nombre}" if heroe_eliminado else "\na. Linterna Verde no encontrado.")

# b. mostrar el año de aparición de Wolverine;
nodo_wolverine = buscar(lista_superheroes, "Wolverine", campo='nombre')
print(
    f"\nb. Wolverine apareció en: {nodo_wolverine.info.anio_aparicion}" if nodo_wolverine else "\nb. Wolverine no encontrado.")

# c. cambiar la casa de Dr. Strange a Marvel;
nodo_strange = buscar(lista_superheroes, "Dr. Strange", campo='nombre')
if nodo_strange:
    nodo_strange.info.casa_comic = "Marvel"
    print(f"\nc. Dr. Strange ahora es: {nodo_strange.info.casa_comic}")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print("\nd. Héroes con 'traje' o 'armadura':")
aux = lista_superheroes.inicio
encontrados_d = []
while aux is not None:
    bio = aux.info.biografia.lower()
    if "traje" in bio or "armadura" in bio:
        encontrados_d.append(aux.info.nombre)
    aux = aux.sig
print(f"   -> {', '.join(encontrados_d)}")

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print("\ne. Héroes con aparición anterior a 1963:")
aux = lista_superheroes.inicio
encontrados_e = []
while aux is not None:
    if aux.info.anio_aparicion < 1963:
        encontrados_e.append(f"{aux.info.nombre} ({aux.info.casa_comic})")
    aux = aux.sig
print(f"   -> {', '.join(encontrados_e)}")

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print("\nf. Casa de Capitana Marvel y Mujer Maravilla:")
heroes_f = ["Capitana Marvel", "Mujer Maravilla"]
resultados_f = []
for nombre_heroe in heroes_f:
    nodo = buscar(lista_superheroes, nombre_heroe, campo='nombre')
    if nodo:
        resultados_f.append(f"{nodo.info.nombre}: {nodo.info.casa_comic}")
print(f"   -> {'; '.join(resultados_f)}")

# g. mostrar toda la información de Flash y Star-Lord;
print("\ng. Información completa de Flash y Star-Lord:")
heroes_g = ["Flash", "Star-Lord"]
for nombre_heroe in heroes_g:
    nodo = buscar(lista_superheroes, nombre_heroe, campo='nombre')
    if nodo:
        print(f"   -> {nodo.info}")

# h. listar los superhéroes que comienzan con la letra B, M y S;
print("\nh. Héroes que comienzan con B, M o S:")
aux = lista_superheroes.inicio
encontrados_h = []
letras_buscadas = ('B', 'M', 'S')
while aux is not None:
    primera_letra = aux.info.nombre[0].upper()
    if primera_letra in letras_buscadas:
        encontrados_h.append(aux.info.nombre)
    aux = aux.sig
print(f"   -> {', '.join(encontrados_h)}")

# i. determinar cuántos superhéroes hay de cada casa de comic.
print("\ni. Conteo de Superhéroes por Casa de Comic:")
conteo_casas = {}
aux = lista_superheroes.inicio
while aux is not None:
    casa = aux.info.casa_comic
    conteo_casas[casa] = conteo_casas.get(casa, 0) + 1
    aux = aux.sig

resultados_i = [f"{casa}: {cantidad}" for casa,
                cantidad in conteo_casas.items()]
print(f"   -> {'; '.join(resultados_i)}")
