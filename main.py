import sys, pygame
from enemy import Enemy
from player import Player


def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

def handle_exit_event(event):
        if event.type == pygame.QUIT:
            sys.exit()


if __name__ == "__main__":
    
    # initialize pygame
    pygame.init()
    size = width, height = 854, 480
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GeometryGame")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    # initialize player
    player = Player(screen)
    enemies = []

    # spawn a singel enemy for testing
    enemies.append(Enemy(100,100,1,1,25,(255,0,0), player))
        
    # main loop
    done = False
    while not done:
        clock.tick(60)
        screen.fill((0,0,0))
        
        # event handling
        for event in pygame.event.get():
            handle_exit_event(event)
            
        # update player
        player.movement_event(event)
        player.update()
        player.display(screen, 30, player.angle)

        # update enemies
        for enemy in enemies:
            enemy.update()
            enemy.display(screen)
        
        # Drawing FPS
        fps_text = update_fps()
        screen.blit(fps_text, (0,0))

        # Update the screen
        pygame.display.flip()