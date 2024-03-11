# Example file showing a circle moving on screen
import pygame
import random
import math
from Projectile import Projectile

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
bullets = []
dt = 0
game_state = "start_menu"
keys = pygame.key.get_pressed()
def draw_start_menu():
   screen.fill((0, 0, 0))
   background = pygame.image.load("start_menu.png").convert()
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Monke Game', True, (255, 255, 255))
   start_button = font.render('Press Space to start game', True, (255, 255, 255))
   screen.blit(background, (screen_width - background.get_width(), screen_height - background.get_height()))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
   pygame.display.update()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemy_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "game_run"
    # fill the screen with a color to wipe away anything from last frame
    if game_state == "game_run":
        screen.fill("green")
        background = pygame.image.load("start_menu.png").convert()
        screen.blit(background, (0,0))
        scroll = 0
        index_background = 0
        tiles = math.ceil(screen_width / background.get_width()) + 1
        pygame.draw.circle(screen, "red", enemy_pos, 50)
        pygame.draw.circle(screen, "brown", player_pos, 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt 
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        if keys[pygame.K_l]:
            bullet = Projectile()
            bullet._init_(player_pos.x,player_pos.y, 6, (255,0,0))
            bullets.append(bullet)
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += 200 * dt
        else:
            enemy_pos.y -= 200 * dt
        if enemy_pos.x < player_pos.x:
            enemy_pos.x += 200 * dt
        else:
            enemy_pos.x -= 200 * dt
        for i in bullets:
            i.x += i.vel
            i.draw(screen)
        #if enemy_pos.y != screen.get_height:
            #enemy_pos.y += random.randint(-300,300)* dt
        #if enemy_pos.x != screen.get_height:
            #enemy_pos.x += random.randint(-300,300) * dt
        if keys[pygame.K_ESCAPE]:
            game_state = "start_menu"
        # flip() the display to put your work on screen
        pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

