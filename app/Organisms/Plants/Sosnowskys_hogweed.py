from app.Organisms.plant import *
from app.Organisms.animal import Animal
from app.Organisms.Animals.cyber_sheep import CyberSheep
from app.Organisms.Animals.human import Human

class SosnowskysHogweed(Plant):
    def __init__(self, positionX, positionY, world):
        super().__init__(10, 0, positionX, positionY, "a Sosnowsky\'s hogweed", "SH", pygame.image.load('app\\icons\\Sosnowskys_hogweed.png'), world)

    def action(self):
        spread = randint(1, 100)
        if spread <= SPREADING_CHANCES:
            self.spread()
        x = self._positionX
        y = self._positionY
        organisms = [None for i in range(4)]
        if x < (self._world.get_width() - 1):
            organisms[0] = self._world.get_organism(x + 1, y)
        if x > 0:
            organisms[1] = self._world.get_organism(x - 1, y)
        if y < (self._world.get_height() - 1):
            organisms[2] = self._world.get_organism(x, y + 1)
        if y > 0:
            organisms[3] = self._world.get_organism(x, y - 1)
        for i in range(4):
            if organisms[i]:
                if isinstance(organisms[i], CyberSheep):
                    pass
                elif isinstance(organisms[i], Human) and organisms[i].get_special_ability():
                    pass
                elif isinstance(organisms[i], Animal):
                    organisms[i].kill()
                    self._world.delete_from_map(organisms[i].get_positionX(), organisms[i].get_positionY())
                    self._world.add_comment(organisms[i].get_name()+" died by approaching a Sosnowsky\'s hogweed")

    def collision(self, eating_organism):
        eating_organism.set_back()
        self.eating(eating_organism)
        if isinstance(eating_organism, CyberSheep):
            pass
        elif isinstance(eating_organism, Human) and eating_organism.get_special_ability():
            pass
        elif isinstance(eating_organism, Animal):
            eating_organism.kill()
            self._world.delete_from_map(eating_organism.get_positionX(), eating_organism.get_positionY())
            self._world.add_comment(eating_organism.get_name() + " died after eating a Sosnowsky\'s hogweed")