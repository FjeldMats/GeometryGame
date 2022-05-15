import pygame
from math import atan2, cos, pi, radians, sin

from bullet import Bullet

class Player: 
    def __init__(self, screen, size):

        self.bullets = []
        self.last_shot = 0

        self.size = size

        self.angle = 0
        self.aim_x = None
        self.aim_y = None

        # fixed position in the middle of the screen
        width, height = screen.get_size()
        self.x = width//2
        self.y = height//2

        self.player_speed = 5
        #relative position everything around player
        self.rel_x = 0
        self.rel_y = 0

        self.rel_x_velocity = 0
        self.rel_y_velocity = 0

        self.rel_x_direction = 0 
        self.rel_y_direction = 0 

    def resize(self, width, height):
        self.x = width//2
        self.y = height//2
    
    def aim(self, x, y):
        self.angle = atan2(x - self.x, y - self.y) * 180 / pi


    def movement_event(self, event, gun_cooldown):

        keys = pygame.key.get_pressed()

        # handle wasd movement
        if keys[pygame.K_w]:
            self.rel_y_direction = 1
        elif keys[pygame.K_s]:
            self.rel_y_direction = -1
        else:
            self.rel_y_direction = 0


        if keys[pygame.K_a]:
            self.rel_x_direction = -1
        elif keys[pygame.K_d]:
            self.rel_x_direction = 1
        else:
            self.rel_x_direction = 0
            

        if keys[pygame.K_SPACE]:
            if pygame.time.get_ticks() - self.last_shot > gun_cooldown:
                self.bullets.append(Bullet(self.aim_x,self.aim_y,self.angle,self))
                self.last_shot = pygame.time.get_ticks()
        
    def update(self):
    
        if self.rel_x_direction == 1:
            self.rel_x_velocity = -1
        elif self.rel_x_direction == -1:
            self.rel_x_velocity = 1 
        else:
            self.rel_x_velocity = 0

        if self.rel_y_direction == 1:
            self.rel_y_velocity = 1
        elif self.rel_y_direction == -1:
            self.rel_y_velocity = -1
        else:
            self.rel_y_velocity = 0
        
        self.rel_x += self.rel_x_velocity * self.player_speed
        self.rel_y += self.rel_y_velocity * self.player_speed


    def display(self, screen):
    
        self.aim_x = self.x + sin(radians(self.angle)) * (self.size*1.5)
        self.aim_y = self.y + cos(radians(self.angle)) * (self.size*1.5)

        screen.blit(pygame.font.SysFont("Arial", 10).render(f"angle {self.angle}", 1, pygame.Color("coral")), (0,20))

        pygame.draw.rect(screen, (255,255,255), pygame.Rect((screen.get_size()[0]//2) - (self.size//2), (screen.get_size()[1]//2) - (self.size//2), self.size, self.size))

        # draw aiming line
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.aim_x, self.aim_y), 5)

        for bullet in self.bullets:
            bullet.update()
            bullet.display(screen)
            