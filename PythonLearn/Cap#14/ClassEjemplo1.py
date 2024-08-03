class GrupoAnimal:
    x = 0
    nombre = ''

    def __init__(self, nombre):
        self.nombre = nombre
        print(self.nombre, 'Construido')

    def grupo(self):
        self.x = self.x + 1
        print(self.nombre, "Recuento Grupal", self.x)

# ----- MAIN -----
# an = GrupoAnimal();
# an.grupo()
# an.grupo()
# an.grupo()
# GrupoAnimal.grupo(an)

# ------- MAIN#2 -------
# an = GrupoAnimal()
# print ("Type", type(an))
# print ("Dir ", dir(an))
# print ("Type", type(an.x))
# print ("Type", type(an.grupo))

# ------- MAIN#3 -------
s = GrupoAnimal('Sally')
j = GrupoAnimal('Jim')

s.grupo()
j.grupo()
s.grupo()