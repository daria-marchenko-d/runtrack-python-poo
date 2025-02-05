class Rectangle:
    def __init__(self, longueur, largeur):
        # Définition des attributs privés
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseur pour la longueur
    def get_longueur(self):
        return self.__longueur

    # Mutateur pour la longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Accesseur pour la largeur
    def get_largeur(self):
        return self.__largeur

    # Mutateur pour la largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un objet Rectangle
rectangle = Rectangle(10, 5)

# Vérification des valeurs initiales
print("Longueur:", rectangle.get_longueur())  
print("Largeur:", rectangle.get_largeur()) 

# Modification des valeurs
rectangle.set_longueur(20)
rectangle.set_largeur(10)

# Vérification après modification
print("Nouvelle Longueur:", rectangle.get_longueur())  
print("Nouvelle Largeur:", rectangle.get_largeur()) 