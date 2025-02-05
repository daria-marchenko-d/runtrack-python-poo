class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Démarrer la voiture si le réservoir est suffisant
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Carburant insuffisant!")

    # Arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir

# Test
voiture = Voiture("Toyota", "Corolla", 2020, 25000)
voiture.demarrer()  
voiture.arreter() 