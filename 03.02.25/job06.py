class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom
    def vieillir(self):
        self.age +=1
    def nommer (self, nom):
        self.nom = nom

animal = Animal()

print(f"L'age de l'animal {animal.age} ans")

animal.vieillir()
print(f"L'age de l'animal {animal.age} ans")

animal.nommer("Luna")
print(f"Le nom est {animal.nom}")