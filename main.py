import sys, pygame
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
    player = Player()
        
    # main loop
    done = False
    while not done:
        clock.tick(60)
        screen.fill((0,0,0))
        
        # event handling
        for event in pygame.event.get():
            handle_exit_event(event)
            
        # update
        player.movement_event(event)
        player.update()
        player.display(screen, 30, player.angle)
        
        # Drawing FPS
        fps_text = update_fps()
        screen.blit(fps_text, (0,0))

        # Update the screen
        pygame.display.flip()