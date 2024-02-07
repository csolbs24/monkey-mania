# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enemy_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")
    pygame.draw.circle(screen, "red", enemy_pos, 50)
    pygame.draw.circle(screen, "brown", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if enemy_pos.y < player_pos.y:
        enemy_pos.y += 200 * dt
    else:
        enemy_pos.y -= 200 * dt
    if enemy_pos.x < player_pos.x:
        enemy_pos.x += 200 * dt
    else:
        enemy_pos.x -= 200 * dt
    if enemy_pos.y != screen.get_height:
        enemy_pos.y += random.randint(-300,300)* dt
    #if enemy_pos.x != screen.get_height:
      #enemy_pos.x += random.randint(-300,300) * dt
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()