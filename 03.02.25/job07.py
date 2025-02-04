class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self, nomb=1):
        self.x -= nomb

    def droite(self, nomb=1):
        self.x += nomb

    def haut(self, nomb=1):
        self.y -= nomb

    def bas(self, nomb=1):
        self.y += nomb

    def position(self):
        return (self.x, self.y)

# Instanciation du personnage
personnage = Personnage()


print("Position initiale :", personnage.position())

dep_gauche = 2
dep_droite = 3
dep_haut = 4
dep_bas = 5


personnage.gauche(dep_gauche)
personnage.droite(dep_droite)
personnage.haut(dep_haut)
personnage.bas(dep_bas)

print("Nouvelle position :", personnage.position())