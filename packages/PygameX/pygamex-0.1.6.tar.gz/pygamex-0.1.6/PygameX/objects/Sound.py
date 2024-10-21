import pygame


class Sound:

    def __init__(self, sound: str, volume: float):
        self.volume = volume
        self.sound = sound
        self.__sound = pygame.mixer.Sound(sound)
        self.__sound.set_volume(volume)

    def play(self):
        self.__sound.play(0)