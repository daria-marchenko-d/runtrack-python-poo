import random

class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom 
        self.__vie = vie 

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)  
        adversaire.__vie -= degats
        print(f"{self.__nom} attaque {adversaire.__nom} et inflige {degats} points de dégâts!")

    def est_vivant(self):
        return self.__vie > 0

    def afficher_vie(self):
        print(f"{self.__nom} a {self.__vie} points de vie restants.")

class Jeu:
    def __init__(self):
        self.__niveau = None

    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté:")
        print("1. Facile (100 PV)")
        print("2. Moyen (80 PV)")
        print("3. Difficile (60 PV)")
        
        choix = input("Votre choix (1/2/3): ")
        if choix == "1":
            self.__niveau = 100
        elif choix == "2":
            self.__niveau = 80
        elif choix == "3":
            self.__niveau = 60
        else:
            print("Choix invalide, niveau par défaut: Moyen (80 PV)")
            self.__niveau = 80

    def lancerJeu(self):
        self.choisirNiveau() 

        joueur = Personnage("Héros", self.__niveau)
        ennemi = Personnage("Monstre", self.__niveau)

        print("\n--- Début du combat! ---")
        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi) 
            if ennemi.est_vivant():
                ennemi.attaquer(joueur) 

            joueur.afficher_vie()
            ennemi.afficher_vie()
            print("-" * 30)

        
        if joueur.est_vivant():
            print("Félicitations! Vous avez vaincu le monstre! 🎉")
        else:
            print("Vous avez perdu... Le monstre vous a terrassé. 💀")


jeu = Jeu()
jeu.lancerJeu()
