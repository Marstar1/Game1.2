import pygame
import menu2


def bg_music():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load('Sound/game.mp3')
    pygame.mixer.music.play(-1)


def menu_music():
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load('Sound/menu.mp3')
    pygame.mixer.music.play(-1)


def bg_music1():
    pygame.mixer.music.load('Sound/level2.mp3')
    pygame.mixer.music.play(-1)


def bg_boss():
    pygame.mixer.music.load('Sound/boss.mp3')
    pygame.mixer.music.play()
    if menu2.game_state == "end":
        pygame.mixer.music.stop()


def end():
    pygame.mixer.music.load('Sound/end.mp3')
    pygame.mixer.music.play(-1)


def transform():
    trans = pygame.mixer.Sound('Sound/star.mp3')
    pygame.mixer.music.set_volume(0.3)
    trans.play()


def teleport():
    pygame.mixer.music.set_volume(0.3)
    tele = pygame.mixer.Sound('Sound/teleport.mp3')
    tele.play()


def bite_bee():
    bite = pygame.mixer.Sound('Sound/attack.mp3')
    bite.play()


def health_hero():
    health = pygame.mixer.Sound('Sound/health.mp3')
    health.play()


def death():
    attack = pygame.mixer.Sound('Sound/death.mp3')
    attack.play()


def win():
    victory = pygame.mixer.Sound('Sound/win.mp3')
    victory.play()
