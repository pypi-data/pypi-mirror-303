import pygame
from .Object import Object

class Circle(Object):

    position = (0,0)
    radius = 50
    color = (255,255,255)

    def __init__(self, position: tuple = (0, 0), radius: int = 50, color: tuple = (255, 255, 255)) -> object:
        self.position = position
        self.radius = radius
        self.color = color
    
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
