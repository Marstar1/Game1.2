import pygame

WIDTH = 1200
HEIGHT = 800


class Background1:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('Image/Background/bg3.jpg').convert(), (1200, HEIGHT))
        self.rect = self.image.get_rect()
        self.moving_speed = 1
        self.bgX1 = 0
        self.bgY1 = 0
        self.bgX2 = self.rect.width
        self.bgY2 = 0

    def update(self):

        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed

        if self.bgX1 <= - self.rect.width:
            self.bgX1 = self.rect.width
        if self.bgX2 <= - self.rect.width:
            self.bgX2 = self.rect.width

    def render(self, window):
        window.blit(self.image, (self.bgX1, self.bgY1))
        window.blit(self.image, (self.bgX2, self.bgY2))


class Background2:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('Image/Background/bg2.png').convert(), (1200, HEIGHT))
        self.rect = self.image.get_rect()
        self.moving_speed = 1
        self.bgX1 = 0
        self.bgY1 = 0
        self.bgX2 = self.rect.width
        self.bgY2 = 0

    def update(self):

        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed

        if self.bgX1 <= - self.rect.width:
            self.bgX1 = self.rect.width
        if self.bgX2 <= - self.rect.width:
            self.bgX2 = self.rect.width

    def render(self, window):
        window.blit(self.image, (self.bgX1, self.bgY1))
        window.blit(self.image, (self.bgX2, self.bgY2))


class Background0:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('Image/Background/bg8.jpg').convert(), (1200, HEIGHT))
        self.rect = self.image.get_rect()
        self.moving_speed = 1
        self.bgX1 = 0
        self.bgY1 = 0
        self.bgX2 = self.rect.width
        self.bgY2 = 0

    def update(self):

        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed

        if self.bgX1 <= - self.rect.width:
            self.bgX1 = self.rect.width
        if self.bgX2 <= - self.rect.width:
            self.bgX2 = self.rect.width

    def render(self, window):
        window.blit(self.image, (self.bgX1, self.bgY1))
        window.blit(self.image, (self.bgX2, self.bgY2))


class Background3:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('Image/Background/bg6.jpg').convert(), (1200, HEIGHT))
        self.rect = self.image.get_rect()
        self.moving_speed = 1
        self.bgX1 = 0
        self.bgY1 = 0
        self.bgX2 = self.rect.width
        self.bgY2 = 0

    def render(self, window):
        window.blit(self.image, (self.bgX1, self.bgY1))
        window.blit(self.image, (self.bgX2, self.bgY2))


