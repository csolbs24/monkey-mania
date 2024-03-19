import pygame
class Projectile(pygame.sprite.Sprite):
    def _init_(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8
        self.direction = direction

    def draw(self,window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
    
    def setvel(newvel):
        vel = newvel