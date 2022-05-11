from math import cos, radians, sin
import pygame

class Bullet: 
    def __init__(self, x, y, angle, owner):
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = 5
        self.owner = owner
        self.hit = False
    
    def update(self):
        self.x += self.velocity * sin(radians(self.angle))  
        self.y += self.velocity * cos(radians(self.angle))


    def display(self, screen):
        if not self.hit:
            pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 5)

    #TODO: add hit detection
    def hit_check(self, enemy):
        if self.x > enemy.x - enemy.size and self.x < enemy.x + enemy.size:
            if self.y > enemy.y - enemy.size and self.y < enemy.y + enemy.size:
                self.hit = True
                enemy.hp -= 10
                self.hit=True