class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def left(self, numb=1):
        self.x -= numb

    def right(self, numb=1):
        self.x += numb

    def up(self, numb=1):
        self.y -= numb

    def down(self, numb=1):
        self.y += numb

    def position(self):
        return (self.x, self.y)

# Character instantiation
personnage = Personnage()


print("Initial position :", personnage.position())

dep_left = 2
dep_right = 3
dep_up = 4
dep_down = 5


personnage.left(dep_left)
personnage.right(dep_right)
personnage.up(dep_up)
personnage.down(dep_down)

print("New position :", personnage.position())