class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__numero}: {self.__nom} {self.__prenom}, Solde: {self.__solde}€")

    def afficher_solde(self):
        print(f"Solde actuel: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
        else:
            print("Fonds insuffisants.")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué.")
        else:
            print("Fonds insuffisants pour le virement.")


compte1 = CompteBancaire(123, "Doe", "John", 500)
compte2 = CompteBancaire(456, "Smith", "Alice", -100, True)


compte1.afficher()
compte1.versement(200)
compte1.afficher_solde()
compte1.retrait(100)
compte1.afficher_solde()
compte1.virement(compte2, 600)
compte1.afficher_solde()
compte2.afficher_solde()

