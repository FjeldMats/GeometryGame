import random

import pygame

from speck import Speck


class randomGeneratedBackground():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.specks = []
        self.genereate_specks(width, height, color)

    def genereate_specks(self, width, height, color):
        for _ in range(0, width//50):
            for _ in range(0, height//50):
                x = random.randint(0, width)
                y = random.randint(0, height)
                self.specks.append(Speck(x, y, color, random.randint(1, 2)))

    def display(self, screen):
        for speck in self.specks:
            speck.display(screen)

    def update(self, player, screen):
        for speck in self.specks:
            speck.move(player, screen)

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.specks = []
        self.genereate_specks(width, height, self.color)
