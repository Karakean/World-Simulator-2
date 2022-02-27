from app.Organisms.animal import *


class Antelope(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(4, 4, positionX, positionY, "an antelope", "A", pygame.image.load('app\\icons\\antelope.png'), world)

    def escaped(self):
        escape = randint(0, 1)
        if escape == 1:
            return True
        return False

    def action(self):
        self._prev_positionX = self._positionX
        self._prev_positionY = self._positionY
        direction = randint(0, 3)
        if direction == 0:
            if self._positionY > 1:
                self._positionY -= 2
            elif self._positionY > 0:
                self._positionY -= 1
        elif direction == 1:
            if self._positionY < (self._world.get_height() - 2):
                self._positionY += 2
            elif self._positionY < (self._world.get_height() - 1):
                self._positionY += 1
        elif direction == 2:
            if self._positionX > 1:
                self._positionX -= 2
            elif self._positionX > 0:
                self._positionX -= 1
        else:
            if self._positionX < (self._world.get_width() - 2):
                self._positionX += 2
            elif self._positionX < (self._world.get_width() - 1):
                self._prev_positionX += 1

    def collision(self, attacking_organism):
        attacking_organism.set_back()
        moved = False
        if self._name == attacking_organism.get_name():
            self.breed(attacking_organism)
        result, x, y = self._world.find_place(self, False)
        if result and self.escaped():
            self.move(x, y)
            attacking_organism.move(self._prev_positionX, self._prev_positionY)
            self._world.add_comment("an antelope avoided a fight")
        elif self.compare_strength(attacking_organism):
            moved = True
            self.fight(attacking_organism, self, moved)
        else:
            if attacking_organism.escaped():
                self._world.add_comment(attacking_organism.get_name() + " avoided a fight.")
            else:
                moved = False
                self.fight(self, attacking_organism, moved)
