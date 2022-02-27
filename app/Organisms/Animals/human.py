from app.Organisms.animal import *


class Human(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(5, 4, positionX, positionY, "the human", "H", pygame.image.load('app\\icons\\human.png'), world)
        self.__direction = 0
        self.__special_ability = False
        self.__cooldown = 0

    def set_direction(self, direction):
        self.__direction = direction

    def action(self):
        self._prev_positionX = self._positionX
        self._prev_positionY = self._positionY
        if self.__direction == 1:
            if self._positionY > 0:
                self._positionY -= 1
            else:
                self._world.add_comment("You have reached the world's edge, none but devils play past here.")
        elif self.__direction == 2:
            if self._positionY < (self._world.get_height() - 1):
                self._positionY += 1
            else:
                self._world.add_comment("You have reached the world's edge, none but devils play past here.")
        elif self.__direction == 3:
            if self._positionX > 0:
                self._positionX -= 1
            else:
                self._world.add_comment("You have reached the world's edge, none but devils play past here.")
        elif self.__direction == 4:
            if self._positionX < (self._world.get_width() - 1):
                self._positionX += 1
            else:
                self._world.add_comment("You have reached the world's edge, none but devils play past here.")
        if self.__cooldown > 0:
            self.__cooldown -= 1
        if self.__special_ability and self.__cooldown == 0:
            self.__special_ability = False
            self.__cooldown = 5

    def collision(self, attacking_organism):
        attacking_organism.set_back()
        moved = False
        if self.compare_strength(attacking_organism):
            if self.__special_ability:
                result, x, y = self._world.find_place(self, 0)
                if result:
                    self.move(x, y)
                    attacking_organism.move(self.get_prev_positionX(), self.get_prev_positionY())
                self._world.add_comment("the human avoided a fight with a stronger enemy")
            else:
                moved = True
                self.fight(attacking_organism, self, moved)
        elif attacking_organism.escaped():
            self._world.add_comment(attacking_organism.get_name() + " avoided a fight")
        else:
            moved = False
            self.fight(self, attacking_organism, moved)

    def escaped(self):
        if self.__special_ability:
            return True
        return False

    def get_special_ability(self):
        return self.__special_ability

    def get_cooldown(self):
        return self.__cooldown

    def set_special_ability(self, ability):
        self.__special_ability = ability

    def set_cooldown(self, cooldown):
        self.__cooldown = cooldown