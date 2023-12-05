import pygame
import background as bg
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Image/Enemy/bee1.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.x = bg.WIDTH
        self.rect.y = randint(200, 620)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def draw(self, window):
        window.blit(self.image, self.rect)
