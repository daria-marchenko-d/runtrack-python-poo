class Personne:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def self_present(self):
        return f"I am {self.surname} {self.name}."

# Instantiating multiple persons with chosen values
person1 = Personne("Dupont", "Jean")
person2 = Personne("Santi", "Anna")
person3 = Personne("Cristo", "Paolo")


print(person1.self_present())
print(person2.self_present())
print(person3.self_present())


