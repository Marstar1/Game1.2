import pygame
import background as bg
from random import randint
import menu2


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Image/Enemy/bee1.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = bg.WIDTH
        self.rect.y = randint(220, 520)
        if menu2.game_state == "level1":
            self.speed = 3
        if menu2.game_state == "level2":
            self.speed = 5
        if menu2.game_state == "level0":
            self.speed = 6

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

    def draw(self, window):
        window.blit(self.image, self.rect)


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Image/Enemy/boss.png'), (500, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 300
        self.health = 50
        self.speed = 0
        self.ospeed = 1

    def update(self):
        if self.health >= 15:
            self.rect.x -= self.speed
        else:
            self.rect.x -= self.ospeed

    def draw(self, window):
        window.blit(self.image, self.rect)


class Sphere(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Image/Enemy/sphere.png'), (300, 300))
        self.rect = self.image.get_rect()
        self.speed = 20
        self.rect.x = bg.WIDTH
        self.rect.y = 350

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed
