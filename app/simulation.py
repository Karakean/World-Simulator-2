from app.world import *

pygame.display.set_caption("World simulator. Mikolaj Nowak s184865")
icon = pygame.image.load('app\\icons\\small_world.png')
pygame.display.set_icon(icon)


class Simulation:
    def __init__(self):
        self.__screen = None
        self.__screen_width = 0
        self.__screen_height = 0
        self.__world = None

    def menu(self):
        self.__screen = pygame.display.set_mode((800, 600))
        self.__screen.fill(black)
        big_image = pygame.image.load('app\\icons\\big_world.png')
        greeting = font.render("Welcome to the World Simulator.", False, white, black)
        is_menu = True
        new_simulation = True
        b = [None for i in range(3)]
        b[0] = Button(black, 0, 450, 800, 50, "Start a new simulation.")
        b[1] = Button(black, 0, 500, 800, 50, "Load a saved simulation.")
        b[2] = Button(black, 0, 550, 800, 50, "Quit.")
        while is_menu:
            self.__screen.blit(big_image, (272, 125))
            self.__screen.blit(greeting, (75, 0))
            for i in range(3):
                b[i].draw(self.__screen)
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b[0].is_over(position):
                        is_menu = False
                    elif b[1].is_over(position):
                        is_menu = False
                        new_simulation = False
                    elif b[2].is_over(position):
                        return
                if event.type == pygame.MOUSEMOTION:
                    for i in range(3):
                        if b[i].is_over(position):
                            b[i].set_font(font, light_grey)
                        else:
                            b[i].set_font(font, white)
            pygame.display.update()
        if not new_simulation:
            self.load_simulation()
        else:
            self.create_new_simulation(greeting, big_image)

    def load_simulation(self):
        file = open("text_file.txt", "r")
        line = file.readline()
        size = line.split()
        x = int(size[0])
        y = int(size[1])
        file.close()
        self.initialize(x, y, False)

    def create_new_simulation(self, greeting, big_image):
        is_setting = True
        width = 20
        height = 20
        w = font.render("width: ", False, white, black)
        h = font.render("height: ", False, white, black)
        b = [None for i in range(5)]
        b[0] = Button(black, 200, 450, 50, 50, "<")
        b[1] = Button(black, 300, 450, 50, 50, ">")
        b[2] = Button(black, 200, 500, 50, 50, "<")
        b[3] = Button(black, 300, 500, 50, 50, ">")
        b[4] = Button(black, 375, 550, 100, 50, "OK")
        while is_setting:
            self.__screen.fill(black)
            self.__screen.blit(greeting, (75, 0))
            self.__screen.blit(big_image, (272, 125))
            self.__screen.blit(w, (50, 445))
            self.__screen.blit(h, (40, 495))
            width_value = font.render(str(width), False, white, black)
            height_value = font.render(str(height), False, white, black)
            self.__screen.blit(width_value, (250, 445))
            self.__screen.blit(height_value, (250, 495))
            for i in range(5):
                b[i].draw(self.__screen)
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b[0].is_over(position):
                        if width > 5:
                            width -= 1
                    if b[1].is_over(position):
                        if width < 35:
                            width += 1
                    if b[2].is_over(position):
                        if height > 5:
                            height -= 1
                    if b[3].is_over(position):
                        if height < 35:
                            height += 1
                    if b[4].is_over(position):
                        is_setting = False
                if event.type == pygame.MOUSEMOTION:
                    for i in range(5):
                        if b[i].is_over(position):
                            b[i].set_font(font, light_grey)
                        else:
                            b[i].set_font(font, white)
            pygame.display.update()
        self.initialize(width, height, True)

    def initialize(self, x, y, new_game):
        self.__world = World(x, y)
        if new_game:
            self.__world.generate_world()
        else:
            self.__world.load_world()
        if y >= 15:
            h = y*FIELD_SIZE
        else:
            h = 15*FIELD_SIZE
        self.__screen_width = x * FIELD_SIZE + 700
        self.__screen_height = h+5
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
        human = self.__world.get_human()
        self.simulation(human)

    def add_to_empty_place(self, x, y):
        prev_screen_width = self.__screen_width
        prev_screen_height = self.__screen_height
        self.__screen = pygame.display.set_mode((800, 600))
        is_choosing = True
        b = [None for i in range(12)]
        b[0] = Button(white, 0, 0, 800, 50, "a wolf")
        b[1] = Button(white, 0, 50, 800, 50, "a sheep")
        b[2] = Button(white, 0, 100, 800, 50, "a fox")
        b[3] = Button(white, 0, 150, 800, 50, "a tortoise")
        b[4] = Button(white, 0, 200, 800, 50, "an antelope")
        b[5] = Button(white, 0, 250, 800, 50, "a cyber-sheep")
        b[6] = Button(white, 0, 300, 800, 50, "grass")
        b[7] = Button(white, 0, 350, 800, 50, "a dandelion")
        b[8] = Button(white, 0, 400, 800, 50, "a guarana")
        b[9] = Button(white, 0, 450, 800, 50, "a belladonna")
        b[10] = Button(white, 0, 500, 800, 50, "a Sosnowsky\'s hogweed")
        b[11] = Button(white, 0, 550, 800, 50, "OK")
        chosen = 100
        while is_choosing:
            self.__screen.fill(white)
            for i in range(12):
                b[i].set_font(font2, black)
                b[i].draw(self.__screen)
            for i in range(1, 12):
                self.__screen.blit(image[i], (50, i*50-35))
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.__screen = pygame.display.set_mode((prev_screen_width, prev_screen_height))
                    is_choosing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__screen = pygame.display.set_mode((prev_screen_width, prev_screen_height))
                        is_choosing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(12):
                        if b[i].is_over(position):
                            for j in range(12):
                                b[j].set_color(white)
                            b[i].set_color(light_grey)
                            if i != 11:
                                chosen = i
                    if b[11].is_over(position):
                        self.__screen = pygame.display.set_mode((prev_screen_width, prev_screen_height))
                        if chosen != 100:
                            self.__world.initialize_organism(chosen, x, y)
                        is_choosing = False
                if event.type == pygame.MOUSEMOTION:
                    for i in range(12):
                        if b[i].is_over(position):
                            b[i].set_color(light_grey)
                        elif chosen != i:
                            b[i].set_color(white)
            pygame.display.update()

    def simulation(self, human):
        is_running = True
        w = self.__world.get_width()
        h = self.__world.get_height()
        b = [None for i in range(4)]
        b[0] = Button(white, w * FIELD_SIZE + 180, 2, 120, 50, "Next turn")
        b[1] = Button(white, w * FIELD_SIZE + 180, 62, 120, 50, "Special ability")
        b[2] = Button(white, w * FIELD_SIZE + 180, 122, 120, 50, "Save")
        b[3] = Button(white, w * FIELD_SIZE + 180, 182, 120, 50, "Quit")
        fields = [[None for x in range(w)]for y in range(h)]
        for i in range(h):
            for j in range(w):
                fields[i][j] = Button(white, 175 + j * FIELD_SIZE, i * FIELD_SIZE + 1, FIELD_SIZE, FIELD_SIZE, "")
        for i in range(4):
            b[i].set_font(font2, black)
        while is_running:
            self.__screen.fill(white)
            for i in range(4):
                b[i].draw(self.__screen, True)
            for i in range(h):
                for j in range(w):
                    fields[i][j].draw(self.__screen, True)
            is_alive = self.__world.is_human_alive()
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_running = False
                    elif event.key == pygame.K_UP and is_alive:
                        human.set_direction(1)
                    elif event.key == pygame.K_DOWN and is_alive:
                        human.set_direction(2)
                    elif event.key == pygame.K_LEFT and is_alive:
                        human.set_direction(3)
                    elif event.key == pygame.K_RIGHT and is_alive:
                        human.set_direction(4)
                    elif human:
                        human.set_direction(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b[0].is_over(position):
                        self.__world.next_turn()
                        if is_alive:
                            human.set_direction(0)
                    if b[1].is_over(position):
                        if is_alive:
                            self.__world.human_special_ability()
                        else:
                            self.__world.add_comment("The human is dead.")
                    if b[2].is_over(position):
                        self.__world.save_world()
                        self.__world.add_comment("Simulation saved successfully.")
                    if b[3].is_over(position):
                        is_running = False
                    for i in range(h):
                        for j in range(w):
                            if fields[i][j].is_over(position):
                                if not self.__world.get_organism(j, i):
                                    self.add_to_empty_place(j, i)
                if event.type == pygame.MOUSEMOTION:
                    for i in range(4):
                        if b[i].is_over(position):
                            b[i].set_color(light_grey)
                        else:
                            b[i].set_color(white)
                    for i in range(h):
                        for j in range(w):
                            if fields[i][j].is_over(position):
                                fields[i][j].set_color(light_grey)
                            else:
                                fields[i][j].set_color(white)
            self.__world.print_world(self.__screen)
            pygame.display.update()





