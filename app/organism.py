import pygame
from random import randint
from abc import ABC, abstractmethod


class Organism(ABC):
    def __init__(self, strength, initiative, positionX, positionY, name, ID, image, world):
        self._strength = strength
        self._initiative = initiative
        self._age = 0
        self._positionX = positionX
        self._positionY = positionY
        self._prev_positionX = 0
        self._prev_positionY = 0
        self._name = name
        self._ID = ID
        self._is_alive = True
        self._image = image
        self._world = world
        world.add_organism(self, self._positionX, self._positionY)

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, attacking_organism):
        pass

    def get_positionX(self):
        return self._positionX

    def get_positionY(self):
        return self._positionY

    def get_prev_positionX(self):
        return self._prev_positionX

    def get_prev_positionY(self):
        return self._prev_positionY

    def get_strength(self):
        return self._strength

    def get_initiative(self):
        return self._initiative

    def get_is_alive(self):
        return self._is_alive

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def get_ID(self):
        return self._ID

    def get_image(self):
        return self._image

    def escaped(self):
        return False

    def set_positionX(self, x):
        self._prev_positionX = self._positionX
        self._positionX = x

    def set_positionY(self, y):
        self._prev_positionY = self._positionY
        self._positionY = y

    def set_back(self):
        self._positionX = self._prev_positionX
        self._positionY = self._prev_positionY

    def set_strength(self, strength):
        self._strength = strength

    def set_age(self, age):
        self._age = age

    def move(self, x, y):
        self.set_positionX(x)
        self.set_positionY(y)
        self._world.delete_from_map(self._prev_positionX, self._prev_positionY)
        self._world.add_to_map(self, self._positionX, self._positionY)

    def kill(self):
        self._is_alive = False

    def compare_strength(self, attacking):  # returns true if attacking organism win
        if self.get_strength() > attacking.get_strength() or (self.get_strength() == attacking.get_strength() and self.get_age() > attacking.get_age()):
            return False
        return True

    def set_prev_position(self, x, y):
        self._prev_positionX = x
        self._prev_positionY = y
