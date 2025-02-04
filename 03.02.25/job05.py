class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displayPoints(self):
        print(f"Point coordinates : ({self.x}, {self.y})")

    def displayX(self):
        print(f"Value of x : {self.x}")

    def displayY(self):
        print(f"Value of y : {self.y}")

    def changeX(self, new_x):
        self.x = new_x

    def changeY(self, new_y):
        self.y = new_y


def create_point():
    x = 2
    y = 3
    return Point(x, y) 

# Instantiating a point with user-entered values
point = create_point()


point.displayPoints()


point.displayX()
point.displayY()

point.changeX(7)
point.changeY(25)

point.displayPoints()