import pygame
from .Object import Object

class Line(Object):

    point1 = (0,0)
    point2 = (0,0)
    color = (255,255,255)
    thickness = 3

    def __init__(self, point1: tuple = (0,0), point2: tuple = (50, 50), color: tuple = (255,255,255), thickness: int = 3):
        self.point1 = point1
        self.point2 = point2
        self.color = color
        self.thickness = thickness
    
    def render(self, screen):
        pygame.draw.line(screen, self.color, self.point1, self.point2, self.thickness)
