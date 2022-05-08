from math import cos, sin
import sys, pygame


def draw_character(screen, size, angle):
    width, height = screen.get_size()


    #TODO:  why is it not drawing a circle? and why is it not drawing from the center of the screen?
    center = ((width//2), (height//2))
    aim_loc = ((height) * sin(angle), (height) * cos(angle))

    pygame.draw.rect(screen, (255,255,255), pygame.Rect((width//2) - size, (height//2) - size, size, size))

    # draw aiming line
    pygame.draw.line(screen, (255,255,255), center, aim_loc, 2)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 854, 480
    screen = pygame.display.set_mode(size)

    angle = 0
    angle_velocity = 0

    done = False

    clock = pygame.time.Clock()

    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #TODO: make it so that when you hold the arrow it moves at a constant speed, but keeps some smooth movement
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    angle_velocity += 0.01
                if keys[pygame.K_LEFT]:
                    angle_velocity -= 0.01
            elif event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    pass
                if keys[pygame.K_LEFT]:
                    pass
            
        color = (255,0,0)

        # update angle
        angle_velocity = angle_velocity * 0.95
        angle += angle_velocity 
  
        # Drawing Rectangle
        screen.fill((0,0,0))
        draw_character(screen, 30, angle)
       

        # Update the screen
        pygame.display.flip()