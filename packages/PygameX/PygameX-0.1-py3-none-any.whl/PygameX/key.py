import pygame

QUIT = pygame.QUIT
ESC = pygame.K_ESCAPE

MOUSE_BUTTON_DOWN = pygame.MOUSEBUTTONDOWN
MOUSE_BUTTON_UP = pygame.MOUSEBUTTONUP

LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN

K_0 = pygame.K_0
K_1 = pygame.K_1
K_2 = pygame.K_2
K_3 = pygame.K_3
K_4 = pygame.K_4
K_5 = pygame.K_5
K_6 = pygame.K_6
K_7 = pygame.K_7
K_8 = pygame.K_8
K_9 = pygame.K_9

KEYDOWN = pygame.KEYDOWN
KEYUP = pygame.KEYUP

def get_pressed():
    return pygame.key.get_pressed()