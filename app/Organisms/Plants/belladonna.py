from app.Organisms.plant import *
from app.Organisms.Animals.human import Human


class Belladonna(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(99, 0, positionX, positionY, "a belladonna", "B", pygame.image.load('app\\icons\\belladonna.png'), world)

    def collision(self, eating_organism):
        eating_organism.set_back()
        self.eating(eating_organism)
        if isinstance(eating_organism, Human) and eating_organism.get_special_ability():
            pass
        else:
            eating_organism.kill()
            self._world.delete_from_map(eating_organism.get_positionX(), eating_organism.get_positionY())
            self._world.add_comment(eating_organism.get_name() + " died after eating a belladonna")