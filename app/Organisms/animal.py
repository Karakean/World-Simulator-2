from app.organism import *


class Animal(Organism):
    def __init__(self, strength, initiative, positionX, positionY, name, ID, image, world):
        super().__init__(strength, initiative, positionX, positionY, name, ID, image, world)

    def action(self):
        self._prev_positionX = self._positionX
        self._prev_positionY = self._positionY
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

    def fight(self, winner, loser, moved):
        x = loser.get_positionX()
        y = loser.get_positionY()
        loser.kill()
        self._world.delete_from_map(x, y)
        if moved:
            winner.move(x, y)
        self._world.add_comment(winner.get_name() + " kills " + loser.get_name())

    def collision(self, attacking_organism):
        attacking_organism.set_back()
        moved = False
        if self._name == attacking_organism.get_name():
            self.breed(attacking_organism)
        elif self.compare_strength(attacking_organism):
            moved = True
            self.fight(attacking_organism, self, moved)
        else:
            if attacking_organism.escaped():
                self._world.add_comment(attacking_organism.get_name() + " avoided a fight.")
            else:
                moved = False
                self.fight(self, attacking_organism, moved)

    def breed(self, partner):
        if self._age >= 3 and partner.get_age() >= 3:
            result, position_x, position_y = self._world.find_place(self, False)
            if result:
                type(self)(position_x, position_y, self._world)
                self._world.add_comment(self.get_name() + " multiplied")
            else:
                # self._world.add_comment("animal could not multiply due to lack of place")
                pass
        else:
            # self._world.add_comment("animal could not multiply because at least one of the potential parents is too young")
            pass

