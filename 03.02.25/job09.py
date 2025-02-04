class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Produit : {self.nom}\nPrix HT : {self.prixHT}€\nTVA : {self.TVA}%\nPrix TTC : {self.calculerPrixTTC():.2f}€"

    def changeNom(self, new_nom):
        self.nom = new_nom

    def changePrix(self, new_prix):
        self.prixHT = new_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.calculerPrixTTC()


# Creation of multiple products
product1 = Produit("Leptop", 1000, 20)
product2 = Produit("Smartphone", 800, 20)
product3 = Produit("Chair", 150, 5)


print(product1.afficher())
print(product2.afficher())
print(product3.afficher())

product1.changeNom("Laptop Gamer")
product1.changePrix(1200)

product2.changeNom("Smartphone Ultra")
product2.changePrix(850)

product3.changeNom("Ergonomic chair")
product3.changePrix(200)

print("\nAfter products modification :")
print(product1.afficher())
print(product2.afficher())
print(product3.afficher())