from app.Organisms.animal import *


class Tortoise(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(2, 1, positionX, positionY, "a tortoise", "T", pygame.image.load('app\\icons\\tortoise.png'), world)

    def action(self):
        self._prev_positionX = self._positionX
        self._prev_positionY = self._positionY
        should_I_stay_or_should_I_go = randint(0, 3)
        if should_I_stay_or_should_I_go == 3:
            direction = randint(0, 3)
            if direction == 0:
                if self._positionY > 0:
                    self._positionY -= 1
            elif direction == 1:
                if self._positionY < (self._world.get_height() - 1):
                    self._positionY += 1
            elif direction == 2:
                if self._positionX > 0:
                    self._positionX -= 1
            else:
                if self._positionX < (self._world.get_width() - 1):
                    self._positionX += 1

    def collision(self, attacking_organism):
        attacking_organism.set_back()
        moved = False
        if self._name == attacking_organism.get_name():
            self.breed(attacking_organism)
        elif self.compare_strength(attacking_organism) and attacking_organism.get_strength() >= 5:
            moved = True
            self.fight(attacking_organism, self, moved)
        elif self.compare_strength(attacking_organism) and attacking_organism.get_strength() < 5:
            self._world.add_comment("a tortoise repelled an attack")
        else:
            if attacking_organism.escaped():
                self._world.add_comment(attacking_organism.get_name() + " avoided a fight")
            else:
                moved = False
                self.fight(self, attacking_organism, moved)
