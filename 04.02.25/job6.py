class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}  
        self.__statut = "en cours" 

    # Ajouter un plat à la commande
    def ajouter_plat(self, nom, prix):
        if prix > 0:
            self.__plats[nom] = prix
        else:
            print("Erreur: Le prix du plat doit être positif.")

    # Annuler la commande
    def annuler_commande(self):
        self.__statut = "annulée"
        print("Commande annulée.")

    # Méthode privée pour calculer le total
    def __calculer_total(self):
        return sum(self.__plats.values())

    # Afficher la commande avec son total
    def afficher_commande(self):
        print(f"Commande n {self.__num_commande} - Statut: {self.__statut}")
        for plat, prix in self.__plats.items():
            print(f" - {plat}: {prix}€")
        print(f"Total: {self.__calculer_total()}€")

    # Calculer la TVA
    def calculer_TVA(self, taux):
        total = self.__calculer_total()
        tva = total * (taux / 100)
        return round(total + tva, 2)

# Test
commande1 = Commande(101)

# Ajouter des plats
commande1.ajouter_plat("Pizza", 12)
commande1.ajouter_plat("Pâtes", 9)
commande1.ajouter_plat("Salade", 7)

# Afficher la commande
commande1.afficher_commande()

# Calculer la TVA à 20%
print(f"Total avec TVA (20%): {commande1.calculer_TVA(20)}€")

# Annuler la commande
commande1.annuler_commande()
commande1.afficher_commande()