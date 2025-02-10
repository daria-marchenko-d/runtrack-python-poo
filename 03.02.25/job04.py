class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def sePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"
    
pers1 = Personne("Dupond", "Jean")
pers2 = Personne("Doe", "John")
pers3 = Personne("Trin", "Katty")

print(pers1.sePresenter())
print(pers2.sePresenter())
print(pers3.sePresenter())


