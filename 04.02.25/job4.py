class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    # Ajouter des crédits
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Erreur: Les crédits doivent être positifs!")

    # Méthode privée pour évaluer l'étudiant
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Affichage des informations de l'étudiant
    def student_info(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Numéro d'étudiant: {self.__num_etudiant}")
        print(f"Niveau: {self.__level}")

# Test
etudiant = Student("Doe", "John", 145)

# Ajout de crédits
etudiant.add_credits(30)
etudiant.add_credits(20)
etudiant.add_credits(50)

# Affichage des informations
etudiant.student_info()