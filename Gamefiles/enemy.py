from math import atan2, cos, radians, sin
import pygame


class Enemy():
    def __init__(self, x, y, hp, speed, size, color, target):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = speed
        self.size = size
        self.color = color
        self.target = target

    def update(self):
        self.x += self.speed * sin(self.get_angle_to_target())
        self.y += self.speed * cos(self.get_angle_to_target())

    def get_angle_to_target(self):
        return atan2(self.target.x - self.x, self.target.y - self.y)

    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, 2)

        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + sin(self.get_angle_to_target())
                         * (self.size*1.5), self.y + cos(self.get_angle_to_target()) * (self.size*1.5)), 5)

        # draw remaning hp text
        screen.blit(pygame.font.SysFont("Arial", 13).render(
            f"hp {self.hp}", 1, (255, 255, 255)), (self.x - self.size, self.y - self.size))

    def distance_to(self, player):
        return ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5

    def hit_check(self, player):
        if self.distance_to(player) < player.size + self.size:
            self.hp -= 50
            return True
        return False
