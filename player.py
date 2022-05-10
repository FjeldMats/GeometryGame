import pygame
from math import cos, radians, sin

from bullet import Bullet

class Player: 
    def __init__(self, screen):
        self.angle = 0
        self.angle_velocity = 0
        self.angle_direction = 0 # 0 = no movement
        self.bullets = []

        width, height = screen.get_size()
        self.x = width//2
        self.y = height//2

        self.aim_x = None
        self.aim_y = None

    def movement_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.angle_direction = 1
        elif keys[pygame.K_a]:
            self.angle_direction = -1
        else: 
            self.angle_direction = 0

        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.aim_x,self.aim_y,self.angle,self))
        
    def update(self):
        if self.angle_direction == 1:
            self.angle_velocity = 3
        elif self.angle_direction == -1:
            self.angle_velocity = -3
        else:
            self.angle_velocity = 0
        
        self.angle += self.angle_velocity


    def display(self, screen, size, angle):
    
        self.aim_x = self.x + sin(radians(angle)) * (size*1.5)
        self.aim_y = self.y + cos(radians(angle)) * (size*1.5)

        screen.blit(pygame.font.SysFont("Arial", 10).render(f"angle {angle}", 1, pygame.Color("coral")), (0,20))

        pygame.draw.rect(screen, (255,255,255), pygame.Rect((screen.get_size()[0]//2) - (size//2), (screen.get_size()[1]//2) - (size//2), size, size))

        # draw aiming line
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.aim_x, self.aim_y), 5)

        for bullet in self.bullets:
            bullet.update()
            bullet.display(screen)
            