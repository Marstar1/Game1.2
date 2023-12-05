import pygame

def bg_music():
    pygame.mixer.music.load('Sound/theme3.mp3')
    pygame.mixer.music.play(-1)

def menu_music():
    pygame.mixer.music.load('Sound/theme1.mp3')
    pygame.mixer.music.play(-1)


def transform():
    transform = pygame.mixer.Sound('Sound/transformation.mp3')
    transform.play()


def bite_bee():
    bite = pygame.mixer.Sound('Sound/sound1.mp3')
    bite.play()


def health_hero():
    health = pygame.mixer.Sound('Sound/berry.mp3')
    health.play()
