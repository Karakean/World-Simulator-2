from random import randint
from app.button import *
from app.Organisms.Animals.human import Human
from app.Organisms.Animals.wolf import Wolf
from app.Organisms.Animals.sheep import Sheep
from app.Organisms.Animals.fox import Fox
from app.Organisms.Animals.tortoise import Tortoise
from app.Organisms.Animals.antelope import Antelope
from app.Organisms.Animals.cyber_sheep import CyberSheep
from app.Organisms.Plants.grass import Grass
from app.Organisms.Plants.dandelion import Dandelion
from app.Organisms.Plants.guarana import Guarana
from app.Organisms.Plants.belladonna import Belladonna
from app.Organisms.Plants.Sosnowskys_hogweed import SosnowskysHogweed

FIELD_SIZE = 16
HOW_MANY_ANIMALS_PER_SPECIES = 2
HOW_MANY_PLANTS_PER_SPECIES = 1

image = [None for i in range(12)]
description = [None for i in range(12)]
empty_place_img = pygame.image.load('app\\icons\\empty_place.png')
image[0] = pygame.image.load('app\\icons\\human.png')
description[0] = font3.render("- the human", False, black, white)
image[1] = pygame.image.load('app\\icons\\wolf.png')
description[1] = font3.render("- a wolf", False, black, white)
image[2] = pygame.image.load('app\\icons\\sheep.png')
description[2] = font3.render("- a sheep", False, black, white)
image[3] = pygame.image.load('app\\icons\\fox.png')
description[3] = font3.render("- a fox", False, black, white)
image[4] = pygame.image.load('app\\icons\\tortoise.png')
description[4] = font3.render("- a tortoise", False, black, white)
image[5] = pygame.image.load('app\\icons\\antelope.png')
description[5] = font3.render("- an antelope", False, black, white)
image[6] = pygame.image.load('app\\icons\\cyber-sheep.png')
description[6] = font3.render("- a cyber-sheep", False, black, white)
image[7] = pygame.image.load('app\\icons\\grass.png')
description[7] = font3.render("- grass", False, black, white)
image[8] = pygame.image.load('app\\icons\\dandelion.png')
description[8] = font3.render("- a dandelion", False, black, white)
image[9] = pygame.image.load('app\\icons\\guarana.png')
description[9] = font3.render("- a guarana", False, black, white)
image[10] = pygame.image.load('app\\icons\\belladonna.png')
description[10] = font3.render("- a belladonna", False, black, white)
image[11] = pygame.image.load('app\\icons\\Sosnowskys_hogweed.png')
description[11] = font3.render("- a Sosnowsky's hogweed", False, black, white)


class World:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__map = [[None for x in range(self.__width)]for y in range(self.__height)]
        self.__organisms = list()
        self.__human = None
        self.__comments = list()
        self.__is_started = False

    def find_empty_place(self):
        x = randint(0, self.__width - 1)
        y = randint(0, self.__height - 1)
        while self.__map[y][x]:
            x = randint(0, self.__width - 1)
            y = randint(0, self.__height - 1)
        return x, y

    def generate_world(self):
        self.__human = Human(int(self.__width/2), int(self.__height/2), self)
        for i in range(HOW_MANY_ANIMALS_PER_SPECIES):
            x, y = self.find_empty_place()
            Wolf(x, y, self)
            x, y = self.find_empty_place()
            Sheep(x, y, self)
            x, y = self.find_empty_place()
            Fox(x, y, self)
            x, y = self.find_empty_place()
            Tortoise(x, y, self)
            x, y = self.find_empty_place()
            Antelope(x, y, self)
            x, y = self.find_empty_place()
            CyberSheep(x, y, self)
        for i in range(HOW_MANY_PLANTS_PER_SPECIES):
            x, y = self.find_empty_place()
            Grass(x, y, self)
            x, y = self.find_empty_place()
            Dandelion(x, y, self)
            x, y = self.find_empty_place()
            Guarana(x, y, self)
            x, y = self.find_empty_place()
            Belladonna(x, y, self)
            x, y = self.find_empty_place()
            SosnowskysHogweed(x, y, self)

    def next_turn(self):
        self.delete_comments()
        self.__organisms.sort(key=lambda x: (x.get_initiative(), x.get_age()), reverse=True)
        for organism in self.__organisms:
            organism.set_age(organism.get_age() + 1)
            if (organism.get_age() > 1 and organism.get_is_alive()) or not self.__is_started:
                prev_x = organism.get_positionX()
                prev_y = organism.get_positionY()
                organism.action()
                actual_x = organism.get_positionX()
                actual_y = organism.get_positionY()
                if not self.__map[actual_y][actual_x]:
                    self.__map[actual_y][actual_x] = organism
                    self.__map[prev_y][prev_x] = None
                elif prev_x == actual_x and prev_y == actual_y:
                    continue
                else:
                    self.__map[actual_y][actual_x].collision(organism)
        for organism in self.__organisms:
            if not organism.get_is_alive():
                self.delete_organism(organism)
        self.__is_started = True

    def print_world(self, screen):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__map[i][j]:
                    screen.blit(self.__map[i][j].get_image(), (175 + j * FIELD_SIZE, i * FIELD_SIZE + 1))
        legend = font2.render("Legend:", False, black, white)
        screen.blit(legend, (50, 0))
        for i in range(12):
            screen.blit(image[i], (5, 16*i+25))
            screen.blit(description[i], (23, 16*i+25))
        comments = font2.render("Comments:", False, black, white)
        screen.blit(comments, (self.__width*16 + 450, 0))
        if self.__height > 15:
            max_height = self.__height*FIELD_SIZE - 20
        else:
            max_height = 15*FIELD_SIZE - 20
        comments_height = len(self.__comments)*16 - 20
        if comments_height <= max_height:
            for i, comment in enumerate(self.__comments):
                _comment = font3.render(comment, False, black, white)
                screen.blit(_comment, (310 + self.__width*FIELD_SIZE, i*16+20))
        else:
            skipped = int((comments_height - max_height)/16)
            for i, comment in enumerate(self.__comments):
                if i < skipped:
                    continue
                _comment = font3.render(comment, False, black, white)
                screen.blit(_comment, (310 + self.__width*FIELD_SIZE, (i-skipped)*16+20))

    def save_world(self):
        file = open("text_file.txt", "w")
        file.write(str(self.__width)+" "+str(self.__height)+"\n")
        for organism in self.__organisms:
            if organism.get_is_alive():
                ID = organism.get_ID()
                x = organism.get_positionX()
                y = organism.get_positionY()
                px = organism.get_prev_positionX()
                py = organism.get_prev_positionY()
                strength = organism.get_strength()
                age = organism.get_age()
                parameters = ID+" "+str(x)+" "+str(y)+" "+str(px)+" "+str(py)+" "+str(strength)+" "+str(age)
                if isinstance(organism, Human):
                    ability = organism.get_special_ability()
                    cooldown = organism.get_cooldown()
                    file.write(parameters+" "+str(ability)+" "+str(cooldown)+"\n")
                else:
                    file.write(parameters+"\n")
        file.close()

    def load_world(self):
        file = open("text_file.txt", "r")
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                continue
            arr = line.split()
            ID = arr[0]
            x = int(arr[1])
            y = int(arr[2])
            px = int(arr[3])
            py = int(arr[4])
            strength = int(arr[5])
            age = int(arr[6])
            organism = None
            if ID == "A":
                organism = Antelope(x, y, self)
            elif ID == "B":
                organism = Belladonna(x, y, self)
            elif ID == "C":
                organism = CyberSheep(x, y, self)
            elif ID == "D":
                organism = Dandelion(x, y, self)
            elif ID == "F":
                organism = Fox(x, y, self)
            elif ID == "G":
                organism = Grass(x, y, self)
            elif ID == "GU":
                organism = Guarana(x, y, self)
            elif ID == "H":
                organism = Human(x, y, self)
                ability = bool(arr[7])
                cooldown = int(arr[8])
                organism.set_special_ability(ability)
                organism.set_cooldown(cooldown)
                self.__human = organism
            elif ID == "S":
                organism = Sheep(x, y, self)
            elif ID == "SH":
                organism = SosnowskysHogweed(x, y, self)
            elif ID == "T":
                organism = Tortoise(x, y, self)
            elif ID == "W":
                organism = Wolf(x, y, self)
            organism.set_prev_position(px, py)
            organism.set_strength(strength)
            organism.set_age(age)

        file.close()

    def additional_condition(self, organism, position_x, position_y, good_sense_of_smell):
        if good_sense_of_smell:
            if not self.__map[position_y][position_x]:
                return True
            elif self.__map[position_y][position_x].get_name() == organism.get_name():
                return True
            elif self.__map[position_y][position_x].get_strength() < organism.get_strength():
                return True
            return False
        else:
            if not self.__map[position_y][position_x]:
                return True
            return False

    def find_place(self, organism, good_sense_of_smell):
        x = organism.get_positionX()
        y = organism.get_positionY()
        checked = [False for i in range(4)]
        taken = 0
        while True:
            direction = randint(0, 3)
            if direction == 0:
                if y > 0 and self.additional_condition(organism, x, y-1, good_sense_of_smell):
                    position_x = x
                    position_y = y-1
                    return True, position_x, position_y
                elif not checked[0]:
                    checked[0] = True
                    taken += 1

            elif direction == 1:
                if y < (self.__height - 1) and self.additional_condition(organism, x, y+1, good_sense_of_smell):
                    position_x = x
                    position_y = y+1
                    return True, position_x, position_y
                elif not checked[1]:
                    checked[1] = True
                    taken += 1
            elif direction == 2:
                if x > 0 and self.additional_condition(organism, x-1, y, good_sense_of_smell):
                    position_x = x-1
                    position_y = y
                    return True, position_x, position_y
                elif not checked[2]:
                    checked[2] = True
                    taken += 1
            elif direction == 3:
                if x < (self.__width - 1) and self.additional_condition(organism, x+1, y, good_sense_of_smell):
                    position_x = x+1
                    position_y = y
                    return True, position_x, position_y
                elif not checked[3]:
                    checked[3] = True
                    taken += 1
            if taken == 4:
                return False, 0, 0

    def get_human(self):
        return self.__human

    def is_human_alive(self):
        if not self.__human:
            return False
        return True

    def human_special_ability(self):
        if not self.__human.get_special_ability() and self.__human.get_cooldown() == 0:
            self.__human.set_special_ability(True)
            self.__human.set_cooldown(5)
            self.add_comment("the human's special ability was turned on")
        elif self.__human.get_special_ability() and self.__human.get_cooldown() >= 0:
            self.add_comment("the human's special ability is already turned on, " + str(self.__human.get_cooldown()) + " turns left")
        else:
            self.add_comment("the human's special ability isn't ready yet, " + str(self.__human.get_cooldown()) + " turns left")

    def get_organism(self, x, y):
        return self.__map[y][x]

    def get_closest_hogweed(self, sheep_x, sheep_y):
        htr = None # hogweed to return
        shortest_distance = self.__width + self.__height
        for organism in self.__organisms:
            if isinstance(organism, SosnowskysHogweed):
                distance = abs(sheep_x - organism.get_positionX()) + abs(sheep_y - organism.get_positionY())
                if distance < shortest_distance:
                    shortest_distance = distance
                    htr = organism
        return htr

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def add_to_map(self, organism, x, y):
        self.__map[y][x] = organism

    def initialize_organism(self, index, x, y):
        if index == 0:
            Wolf(x, y, self)
        elif index == 1:
            Sheep(x, y, self)
        elif index == 2:
            Fox(x, y, self)
        elif index == 3:
            Tortoise(x, y, self)
        elif index == 4:
            Antelope(x, y, self)
        elif index == 5:
            CyberSheep(x, y, self)
        elif index == 6:
            Grass(x, y, self)
        elif index == 7:
            Dandelion(x, y, self)
        elif index == 8:
            Guarana(x, y, self)
        elif index == 9:
            Belladonna(x, y, self)
        elif index == 10:
            SosnowskysHogweed(x, y, self)

    def add_organism(self, organism, x, y):
        self.add_to_map(organism, x, y)
        self.__organisms.append(organism)

    def add_comment(self, comment):
        self.__comments.append(comment)

    def delete_from_map(self, x, y):
        self.__map[y][x] = None

    def delete_organism(self, organism):
        if isinstance(organism, Human):
            self.__organisms.remove(organism)
            self.__human = None
        else:
            self.__organisms.remove(organism)

    def delete_comments(self):
        self.__comments.clear()


