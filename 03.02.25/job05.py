class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        print(f"Les coordonnées des points sont: {self.x} et {self.y}")
    def afficherX(self):
        print(f"X est: {self.x}")
    def afficherY(self):
        print(f"Y est: {self.y}")
    def changerX(self, new_x):
        self.x = new_x
    def changerY(self, new_y):
        self.y = new_y
def creer_points():
    return Point(5,10)    

point = creer_points()


point.afficherLesPoints()


point.afficherX()
point.afficherY()

point.changerX(20)
point.changerY(15)

point.afficherLesPoints()