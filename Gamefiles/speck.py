import pygame


class Speck:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def move(self, player, screen):

        x_max = screen.get_width()
        y_max = screen.get_height()

        self.x += player.rel_x_velocity 
        self.y += player.rel_y_velocity

        # wrap around when reach edge of screen
        if self.x < 0 or self.x > x_max:
            self.x = self.x % x_max
        if self.y < 0 or self.y > y_max:
            self.y = self.y % y_max
            
        

