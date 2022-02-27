from app.Organisms.animal import *


class Sheep(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(4, 4, positionX, positionY, "a sheep", "S", pygame.image.load('app\\icons\\sheep.png'), world)
