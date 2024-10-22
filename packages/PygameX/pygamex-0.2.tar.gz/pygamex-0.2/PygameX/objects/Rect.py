import pygame

from .Object import Object


class Rect(Object):

    def __init__(self, position: tuple = (0, 0), size: tuple = (50, 50), color: tuple = (255, 255, 255)):
        self.position = position
        self.size = size
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, self.size))
