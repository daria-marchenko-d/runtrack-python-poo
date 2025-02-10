class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "À faire"

    def marquer_comme_finie(self):
        self.__statut = "Terminé"

    def get_tache(self):
        return f"{self.__titre}: {self.__description} [{self.__statut}]"

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouter_tache(self, tache):
        self.__taches.append(tache)

    def supprimer_tache(self, titre):
        self.__taches = [t for t in self.__taches if t.get_tache().split(":")[0] != titre]

    def afficher_liste(self):
        for tache in self.__taches:
            print(tache.get_tache())


tache1 = Tache("Étudier Python", "Apprendre la POO")
tache2 = Tache("Faire du sport", "Aller à la salle de sport")


liste = ListeDeTaches()
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)


print("Liste de tâches initiale:")
liste.afficher_liste()


tache1.marquer_comme_finie()


print("Liste de tâches après modification:")
liste.afficher_liste()

