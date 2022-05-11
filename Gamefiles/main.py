import os
import random
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
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("GeometryGame")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)


    score = 0
    enemy_spawn_cooldown = 4000
    player_gun_cooldown = 500

    last_enemy_spawn = pygame.time.get_ticks()

    # initialize player
    player = Player(screen)
    enemies = []
        
    # main loop
    done = False
    while not done:
        clock.tick(60)
        screen.fill((0,0,0))
        
        # event handling
        for event in pygame.event.get():
            handle_exit_event(event)

            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                player.resize(event.w, event.h)

            elif event.type == pygame.FULLSCREEN:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            
        # update player
        player.movement_event(event, player_gun_cooldown)
        player.update()
        player.display(screen, 30, player.angle)

        # check if bullet hits enemy
        for enemy in enemies:
            for bullet in player.bullets:
                bullet.hit_check(enemy)
        
        # remove dead enemies
        for enemy in enemies:
            if enemy.hp <= 0:
                enemies.remove(enemy)
                score += 1
        
        # remove all bullets that hit an enemy
        for bullet in player.bullets:
            if bullet.hit:
                player.bullets.remove(bullet)

        #spawn enemies
        now = pygame.time.get_ticks()
        if now - last_enemy_spawn > enemy_spawn_cooldown:

            # spawn enemy with min 500 px distance from player
            distance = 0
            x = 0
            y = 0
            while distance < 500:
                x = random.randint(player.x - 700, player.x + 700)
                y = random.randint(player.y - 700, player.y + 700)
                distance = abs(((x - player.x)**2 + (y - player.y)**2)**0.5)


            size  = random.randint(25, 100)
            enemies.append(Enemy(x,y,size*5,15/size,size,(255,0,0), player))
            last_enemy_spawn = pygame.time.get_ticks()

            enemy_spawn_cooldown = random.randint(2000, 6000)

        # update enemies
        for enemy in enemies:
            enemy.update()
            enemy.display(screen)
        
        # Drawing FPS and ticks
        fps_text = update_fps()
        screen.blit(fps_text, (0,0))
        screen.blit(font.render(str(pygame.time.get_ticks()), 1, pygame.Color("coral")), (40,0))
        screen.blit(font.render(str(now - last_enemy_spawn), 1, pygame.Color("coral")), (100,0))

        # Update the screen
        pygame.display.flip()