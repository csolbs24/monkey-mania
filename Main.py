# Example file showing a circle moving on screen
import pygame
import random
import math
from Projectile import Projectile
from Enemy import Enemy
from Block import Block 

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
bullets = []
enemies = []
monkeyimage = pygame.image.load("gmonke.png").convert()
menubackground = pygame.image.load("start_menu.png").convert()
gamebackground = pygame.image.load("backdrop.png").convert()
bulletimage= pygame.image.load("monkebullet.png").convert()

dt = 0
game_state = "start_menu"
keys = pygame.key.get_pressed()
def draw_start_menu():
   screen.fill((0, 0, 0))
   
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Monke Game', True, (255, 255, 255))
   start_button = font.render('Press Space to start game', True, (255, 255, 255))
   screen.blit(menubackground, (screen_width - menubackground.get_width(), screen_height - menubackground.get_height()))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
   pygame.display.update()

player_pos = pygame.math.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemy_pos1 = pygame.math.Vector2(screen.get_width() / 3, screen.get_height() / 3)

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
        screen.blit(gamebackground, (0,0))
        if random.randrange(0, 60) == 6:
            enemy = Enemy()
            enemy._init_((random.randrange(0,100)) , (random.randrange(0,600)) , 40, (255,0,0))
            enemies.append(enemy)
        pygame.draw.circle(screen, (0,0,0), player_pos, 30)
        
        screen.blit(monkeyimage, (player_pos.x - 25, player_pos.y -25))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if player_pos.y > 0:
                player_pos.y -= 400 * dt 
        if keys[pygame.K_s]:
            if player_pos.y < screen_height:
                player_pos.y += 400 * dt
        if keys[pygame.K_a]:
            if player_pos.x > 0:
                player_pos.x -= 400 * dt
        if keys[pygame.K_d]:
            if player_pos.x < screen_width:
                player_pos.x += 400 * dt

        if keys[pygame.K_LEFT]:
            if random.randrange(0, 7,) == 6:
                bullet = Projectile()
                bullet._init_(player_pos.x,player_pos.y, 6, (0,255,0), "Left")
                bullets.append(bullet)
        elif keys[pygame.K_DOWN]:
            if random.randrange(0, 7,) == 6:
                bullet = Projectile()
                bullet._init_(player_pos.x,player_pos.y, 6, (0,255,0), "Down")
                bullets.append(bullet)
        elif keys[pygame.K_UP]:
            if random.randrange(0, 7) == 6:
                bullet = Projectile()
                bullet._init_(player_pos.x,player_pos.y, 6, (0,255,0), "Up")
                bullets.append(bullet)
        elif keys[pygame.K_RIGHT]:
            if random.randrange(0, 7) == 6:
                bullet = Projectile()
                bullet._init_(player_pos.x,player_pos.y, 6, (0,255,0), "Right")
                bullets.append(bullet)
        for  i in enemies:
            if i.y == player_pos.y:
                i.y += 0 * dt
            elif i.y < player_pos.y:
                i.y += 200 * dt
            elif i.y > player_pos.y:
                i.y -= 200 * dt

            if i.x == player_pos.x:
                i.x += 0 * dt
            elif i.x < player_pos.x:
                i.x += 200 * dt
            elif i.x > player_pos.x:
                i.x -= 200 * dt
            i.draw(screen)

        for i in bullets:
            if i.direction == "Left":
                i.x -= i.vel
            elif i.direction == "Right":
                i.x += i.vel
            elif i.direction == "Up":
                i.y -= i.vel
            elif i.direction == "Down":
                i.y += i.vel
            if i.y < 0 or i.y > screen_height or i.x < 0 or i.x > screen_width:
                    bullets.remove(i)
            for j in enemies:
                if (abs(j.y - i.y) < 46 and abs(j.x - i.x) < 46):
                    bullets.remove(i)
                    enemies.remove(j)

            i.draw(screen)
            screen.blit(bulletimage,(i.x - 6, i.y - 6))

        if keys[pygame.K_ESCAPE]:
            game_state = "start_menu"
        # flip() the display to put your work on screen
        pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

