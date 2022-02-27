from app.Organisms.plant import *


class Guarana(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(0, 0, positionX, positionY, "a guarana", "GU", pygame.image.load('app\\icons\\guarana.png'), world)

    def collision(self, eating_organism):
        eating_organism.set_back()
        self.eating(eating_organism)
        eating_organism.set_strength(eating_organism.get_strength() + 3)
