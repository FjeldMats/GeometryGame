from math import atan2, cos, radians, sin
import pygame


class Enemy():
    def __init__(self, x, y , hp, speed, size, color, target):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = speed
        self.size = size
        self.color = color
        self.target = target
    
    def update(self):
        # get angle to target
        angle = self.get_angle_to_target()

        # move in direction of angle
        self.x += self.speed * sin(radians(angle))
        self.y += self.speed * cos(radians(angle))


    #TODO: find why its not moving to player 
    def get_angle_to_target(self):
        # get angle to target
        return atan2(self.target.y - self.y, self.target.x - self.x)  * 180 / 3.14159265359


    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

        #draw aiming line 
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.x + sin(radians(self.get_angle_to_target())) * (self.size*1.5), self.y + cos(radians(self.get_angle_to_target())) * (self.size*1.5)), 5)




