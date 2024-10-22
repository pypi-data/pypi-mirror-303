import pygame

from .Object import Object
from ..exceptions import *


class TextDisplay(Object):

    def __init__(self, position: tuple = (0, 0), size: int = 50, color: tuple = (255, 255, 255),
                 font_name: str = "arial", font_size=24, text: str = "Hello World!"):
        if not pygame.font.get_init():
            pygame.font.init()
            if not pygame.font.get_init():
                raise FontInitException()

        self.position = position
        self.size = size
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = text

        self.__text = self.font.render(self.text, True, self.color)
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = position

    def set_font(self, font_name: str, font_size, bold: bool = False, italic: bool = False):
        self.font = pygame.font.SysFont(font_name, font_size, bold, italic)

        self.update()

    def set_text(self, text: str):
        self.text = text

        self.update()

    def update(self):
        self.__text = self.font.render(self.text, True, self.color)
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = self.position

    def render(self, screen):
        screen.blit(self.__text, self.__text_rect)
