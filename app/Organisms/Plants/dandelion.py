from app.Organisms.plant import *


class Dandelion(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(0, 0, positionX, positionY, "a dandelion", "D", pygame.image.load('app\\icons\\dandelion.png'), world)

    def action(self):
        for i in range(3):
            spread = randint(1, 100)
            if spread <= SPREADING_CHANCES:
                self.spread()