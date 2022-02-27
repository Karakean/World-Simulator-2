from app.organism import *

SPREADING_CHANCES = 10  # percent


class Plant(Organism):
    def __init__(self, strength, initiative, positionX, positionY, name, ID, image, world):
        super().__init__(strength, initiative, positionX, positionY, name, ID, image, world)

    def spread(self):
        result, x, y = self._world.find_place(self, False)
        if result:
            type(self)(x, y, self._world)
            self._world.add_comment(self._name + " is spreading")

    def eating(self, eating_organism):
        x = self._positionX
        y = self._positionY
        self.kill()
        self._world.delete_from_map(x, y)
        eating_organism.move(x, y)
        self._world.add_comment(eating_organism.get_name() + " has eaten " + self._name)

    def action(self):
        spread = randint(1, 100)
        if spread <= SPREADING_CHANCES:
            self.spread()

    def collision(self, eating_organism):
        eating_organism.set_back()
        self.eating(eating_organism)
