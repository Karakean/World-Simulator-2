from app.Organisms.animal import *


class Wolf(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(9, 5, positionX, positionY, "a wolf", "W", pygame.image.load('app\\icons\\wolf.png'), world)

