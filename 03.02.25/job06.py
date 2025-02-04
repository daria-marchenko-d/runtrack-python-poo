class Animal:
    def __init__(self):
        self.age = 0
        self.surname = ""

    def ages(self):
        self.age += 1

    def name(self, name):
        self.surname = name

# Instanciation de l'objet Animal
animal = Animal()


print("The age of the animal :", animal.age)


animal.ages()
print("The age of the animal as it ages:", animal.age)


animal.name("Trito")
print("The animal is named :", animal.surname)