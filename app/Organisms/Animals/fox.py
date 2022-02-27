from app.Organisms.animal import *


class Fox(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(3, 7, positionX, positionY, "a fox", "F", pygame.image.load('app\\icons\\fox.png'), world)

    def action(self):
        self._prev_positionX = self._positionX
        self._prev_positionY = self._positionY
        result, pos_x, pos_y = self._world.find_place(self, True)
        if result:
            self._positionX = pos_x
            self._positionY = pos_y
