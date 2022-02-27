from app.Organisms.animal import *


class CyberSheep(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(11, 4, positionX, positionY, "a cyber-sheep", "C", pygame.image.load('app\\icons\\cyber-sheep.png'), world)

    def action(self):
        self._prev_positionX = self._positionX
        self._prev_positionY = self._positionY
        hogweed = self._world.get_closest_hogweed(self._positionX, self._positionY)
        if hogweed:
            if hogweed.get_positionX() < self._positionX:
                self._positionX -= 1
            elif hogweed.get_positionX() > self._positionX:
                self._positionX += 1
            elif hogweed.get_positionY() < self._positionY:
                self._positionY -= 1
            elif hogweed.get_positionY() > self._positionY:
                self._positionY += 1
        else:
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

