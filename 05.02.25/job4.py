class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes = 0

    def marquer_un_but(self):
        self.__buts += 1

    def effectuer_une_passe_decisive(self):
        self.__passes += 1

    def afficher_statistiques(self):
        print(f"{self.__nom} (#{self.__numero}, {self.__position}) - Buts: {self.__buts}, Passes: {self.__passes}")

class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def ajouter_joueur(self, joueur):
        self.__joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        for joueur in self.__joueurs:
            joueur.afficher_statistiques()


joueur1 = Joueur("Mbappé", 7, "Attaquant")
joueur2 = Joueur("Kanté", 6, "Milieu")


equipe = Equipe("France")
equipe.ajouter_joueur(joueur1)
equipe.ajouter_joueur(joueur2)


joueur1.marquer_un_but()
joueur2.effectuer_une_passe_decisive()


print("Statistiques après le match:")
equipe.afficher_statistiques_joueurs()
