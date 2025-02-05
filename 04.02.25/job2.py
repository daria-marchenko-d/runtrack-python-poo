class Livre:
    def __init__(self, titre, auteur, pages):
        # Définition des attributs privés
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages if isinstance(pages, int) and pages > 0 else 0

    # Accesseur pour le titre
    def get_titre(self):
        return self.__titre

    # Mutateur pour le titre
    def set_titre(self, titre):
        self.__titre = titre

    # Accesseur pour l'auteur
    def get_auteur(self):
        return self.__auteur

    # Mutateur pour l'auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    # Accesseur pour le nombre de pages
    def get_pages(self):
        return self.__pages

    # Mutateur pour le nombre de pages (validation)
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif!")

# Création d'un objet Livre
livre = Livre("Les Misérables", "Victor Hugo", 500)

# Vérification des valeurs initiales
print("Titre:", livre.get_titre())  
print("Auteur:", livre.get_auteur())
print("Pages:", livre.get_pages())  

# Modification correcte du nombre de pages
livre.set_pages(600)
print("Nouveau nombre de pages:", livre.get_pages()) 

# Tentative de modification incorrecte
livre.set_pages(-50)  # Erreur: Le nombre de pages doit être un entier positif!
print("Pages après tentative incorrecte:", livre.get_pages())