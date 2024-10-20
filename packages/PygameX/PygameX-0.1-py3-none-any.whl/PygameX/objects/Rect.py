import pygame
from .Object import Object

class Rect(Object):

    position = (0,0)
    size = (50,50)
    color = (255,255,255)

    def __init__(self, position: tuple = (0,0), size: tuple = (50, 50), color: tuple = (255,255,255)):
        self.position = position
        self.size = size
        self.color = color
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, self.size))
