import pygame
class Enemy(pygame.sprite.Sprite):
    def _init_(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 20
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
