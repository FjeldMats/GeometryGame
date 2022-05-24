import pygame


class Bar:
    def __init__(self, x, y, width, height, color, value, max_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.value = value
        self.max_value = max_value
        self.value_percent = self.value / self.max_value
        self.value_percent = round(self.value_percent, 2)
        self.value_percent *= 100
    
    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width * self.value_percent / 100, self.height))
        
    def update(self, value):
        self.value = value
        self.value_percent = self.value / self.max_value
        self.value_percent = round(self.value_percent, 2)
        self.value_percent *= 100
    
