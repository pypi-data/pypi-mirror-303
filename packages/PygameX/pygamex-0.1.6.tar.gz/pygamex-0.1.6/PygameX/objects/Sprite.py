import pygame

from .Object import Object


class Sprite(Object):

    def __init__(self, position: tuple = (0, 0), sprite: str = ""):
        self.position = position
        self.__sprite = pygame.image.load(sprite)

    def set_sprite(self, new_sprite: str):
        self.__sprite = pygame.image.load(new_sprite)

    def render(self, screen):
        screen.blit(self.__sprite.convert(screen), self.position)
