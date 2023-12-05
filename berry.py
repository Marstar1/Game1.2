import pygame
import background as bg

from random import randint


class Berry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.berry = ['Image/Berry/berry.png', 'Image/Berry/berry1.png', 'Image/Berry/berry2.png']
        self.image = pygame.transform.scale(pygame.image.load(self.berry[randint(0, 2)]).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect(center=(bg.WIDTH, randint(430, 570)))

    def update(self):
        self.rect.x -= 2
        if self.rect.x < 0:
            self.kill()
