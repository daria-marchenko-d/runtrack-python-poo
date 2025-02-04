import math

class Circle:
    def __init__(self, radius):
        # Initializing the circle radius
        self.radius = radius

    def changeRadius(self, new_radius):
        self.radius = new_radius

    def displayInfos(self):
        print(f"The circle radius : {self.radius}")
        print(f"Diameter : {self.diameter()}")
        print(f"Circumference : {self.circumference():.2f}")
        print(f"Area : {self.area():.2f}")

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

circle1 = Circle(4)
circle2 = Circle(7)

print("First Circle Information :")
circle1.displayInfos()
print("\nSecond Circle Information :")
circle2.displayInfos()