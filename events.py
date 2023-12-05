import pygame
from enemy import Enemy
from random import randint
from sound import transform, bite_bee, health_hero
import menu1

def event(enemies, scores, group_berry, berry, window, button):

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            make_berry(group_berry, berry)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                do_pause(window)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for bee in enemies:
                if bee.rect.collidepoint(x, y):
                    transform()
                    enemies.remove(bee)
                    bee.image = pygame.transform.scale(pygame.image.load('Image/Enemy/star1.png'), (50, 50))
                    bee.speed = 4
                    scores.amount_friends += 1

        if event.type == pygame.QUIT:
            exit()


def make_bee(enemies, window, friends):
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy(randint(4, 6))
        enemies.add(enemy)
        friends.add(enemy)


def make_friends(friends, window):
    friends.update()
    friends.draw(window)


def make_berry(group_berry, berry):
    group_berry.add(berry)


def move_berry(window, group_berry):
    group_berry.update()
    group_berry.draw(window)


def collide(hero, enemies, group_berry):
    if pygame.sprite.spritecollide(hero, enemies, True):
        bite_bee()
        hero.health -= 1
    if pygame.sprite.spritecollide(hero, group_berry, True):
        if hero.health < 3:
            hero.health += 1
            health_hero()


def do_pause(window):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            pause_text = pygame.font.SysFont('ardecode', 50). \
                render('Пауза! Нажми пробел, чтобы продолжить', True, (255, 255, 255))
            window.blit(pause_text, (250, 400))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False

            pygame.display.update()
