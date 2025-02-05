class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages if isinstance(pages, int) and pages > 0 else 0
        # Par défaut, le livre est disponible
        self.__disponible = True  

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif!")

    # Vérifie si le livre est disponible
    def verification(self):
        return self.__disponible

    # Emprunter le livre s'il est disponible
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    # Rendre le livre s'il a été emprunté
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est déjà disponible.")

# Test
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 120)

# Vérification initiale
print("Disponible ?", livre.verification()) 

# Emprunter le livre
livre.emprunter()  # Le livre a été emprunté.
print("Disponible ?", livre.verification())

# Tenter d'emprunter à nouveau
livre.emprunter()  

# Rendre le livre
livre.rendre() 
print("Disponible ?", livre.verification()) 