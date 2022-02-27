import pygame

pygame.init()

font = pygame.font.SysFont('timesnewroman', 50)
font2 = pygame.font.SysFont('timesnewroman', 20)
font3 = pygame.font.SysFont('timesnewroman', 14)
black = (0, 0, 0)
white = (255, 255, 255)
light_grey = (170, 170, 170)


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__font = font
        self.__font_color = white

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.__x - 1, self.__y - 1, self.__width + 2, self.__height + 2), 0)
        pygame.draw.rect(win, self.__color, (self.__x, self.__y, self.__width, self.__height), 0)
        if self.__text != '':
            text = self.__font.render(self.__text, True, self.__font_color)
            win.blit(text, (self.__x + (self.__width / 2 - text.get_width() / 2), self.__y + (self.__height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if pos[0] > self.__x and pos[0] < self.__x + self.__width:
            if pos[1] > self.__y and pos[1] < self.__y + self.__height:
                return True
        return False

    def set_color(self, color):
        self.__color = color

    def set_font(self, custom_font, color):
        self.__font = custom_font
        self.__font_color = color