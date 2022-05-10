import pygame
from math import cos, radians, sin

class Player: 
    def __init__(self):
        self.angle = 0
        self.angle_velocity = 0
        self.angle_direction = 0 # 0 = no movement

    def movement_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.angle_direction = 1
        elif keys[pygame.K_a]:
            self.angle_direction = -1
        else: 
            self.angle_direction = 0
        
    def update(self):
        if self.angle_direction == 1:
            self.angle_velocity = 1
        elif self.angle_direction == -1:
            self.angle_velocity = -1
        else:
            self.angle_velocity = 0
        
        self.angle += self.angle_velocity


    def display(self, screen, size, angle):
        width, height = screen.get_size()

        center = ((width//2), (height//2))
        aim_loc = ((center[0] + sin(radians(angle)) * (size*3)), (center[1] + cos(radians(angle)) * (size*3)))

        screen.blit(pygame.font.SysFont("Arial", 18).render("Aiming at: " + str(aim_loc) + "angle" + str(angle), 1, pygame.Color("coral")), (0,25))

        pygame.draw.rect(screen, (255,255,255), pygame.Rect((width//2) - size, (height//2) - size, size, size))

        # draw aiming line
        pygame.draw.line(screen, (255,255,255), center, aim_loc, 2)