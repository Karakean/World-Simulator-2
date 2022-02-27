from app.Organisms.plant import *


class Grass(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(0, 0, positionX, positionY, "grass", "G", pygame.image.load('app\\icons\\grass.png'), world)
