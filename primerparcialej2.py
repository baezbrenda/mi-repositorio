from lista_superheroes import superheroes

print(f"Total de personajes en la lista: {len(superheroes)}")
print(f"Primer personaje: {superheroes[0]}")


def search_hero(value, key):
    for index, hero in enumerate(superheroes):
        if hero[key] == value:
            return index
    return None


pos_thing = search_hero("The Thing", "name")
pos_raccoon = search_hero("Rocket Raccoon", "name")

print(f"The Thing está en la posición: {pos_thing}")
print(f"Rocket Raccoon está en la posición: {pos_raccoon}")


def order_by_name(hero):
    return str(hero["name"])


def order_by_real_name(hero):
    return str(hero["real_name"])


def order_by_year(hero):
    return str(hero["first_appearance"])


class Superhero:
    def __init__(self, data):
        self.name = data["name"]
        self.real_name = data["real_name"]
        self.first_appearance = data["first_appearance"]
        self.is_villain = data["is_villain"]
        self.short_bio = data["short_bio"]

    def __str__(self):
        return f"{self.name}, {self.real_name} - {'Villano' if self.is_villain else 'Héroe'}"


class SuperheroList:
    def __init__(self):
        self.list = superheroes

    def sort_by_criterion(self, key):
        self.list.sort(key=lambda hero: str(hero[key]))

    def show(self):
        for hero in self.list:
            print(hero["name"], "-", hero["real_name"])

    def search(self, value, key):
        for hero in self.list:
            if hero[key] == value:
                return hero
        return None

    def delete_value(self, value, key):
        hero = self.search(value, key)
        if hero:
            self.list.remove(hero)
            return f"Se eliminó {hero['name']}"
        return "No encontrado"


hero_list = SuperheroList()

hero_list.sort_by_criterion("name")
hero_list.show()

pos_thing = hero_list.search("The Thing", "name")
pos_raccoon = hero_list.search("Rocket Raccoon", "name")
print(f"The Thing está en la posición: {pos_thing}")
print(f"Rocket Raccoon está en la posición: {pos_raccoon}")

print("\nLista de villanos:")
for hero in hero_list.list:
    if hero["is_villain"]:
        print(hero["name"])

print("\nVillanos anteriores a 1980:")
for hero in hero_list.list:
    if hero["is_villain"] and int(hero["first_appearance"]) < 1980:
        print(hero["name"])

print("\nSuperhéroes con Bl, G, My, W:")
for hero in hero_list.list:
    if hero["name"].startswith(("Bl", "G", "My", "W")):
        print(hero["name"])

hero_list.sort_by_criterion("real_name")
hero_list.show()

hero_list.sort_by_criterion("first_appearance")
hero_list.show()

ant_man = hero_list.search("Ant-Man", "name")
if ant_man:
    ant_man["real_name"] = "Scott Lang"
    print(f"Nuevo nombre real de Ant-Man: {ant_man['real_name']}")

print("\nPersonajes con 'time-traveling' o 'suit':")
for hero in hero_list.list:
    if "time-traveling" in hero["short_bio"] or "suit" in hero["short_bio"]:
        print(hero["name"])

print("\nEliminando personajes:")
print(hero_list.delete_value("Electro", "name"))
print(hero_list.delete_value("Baron Zemo", "name"))
