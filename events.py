import pygame
from enemy import Enemy, Sphere, Boss
from sound import transform, bite_bee, health_hero, teleport, death
import menu2
import tkinter
from tkinter import *


def event(enemies, scores, group_berry, berry, window):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT and (menu2.game_state == " level1 or " or menu2.game_state == "level2"):
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

                    scores.amount_friends += 1
        if event.type == pygame.QUIT:
            exit()


def eventboss(bosses, scores, window):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                do_pause(window)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for boss in bosses:
                if boss.rect.collidepoint(x, y):
                    boss.health -= 1
                    scores.boss_health -= 1

        if event.type == pygame.QUIT:
            exit()


def make_bee1(enemies, window, friends):
    enemies.draw(window)
    if len(enemies) < 5:
        enemy = Enemy()
        enemies.add(enemy)
        friends.add(enemy)


def make_bee2(enemies, window, friends):
    enemies.draw(window)
    if len(enemies) < 10:
        enemy = Enemy()
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


def make_sphere(window, spheres):
    spheres.update()
    spheres.draw(window)
    if len(spheres) < 1:
        sphere = Sphere()
        spheres.add(sphere)


def make_boss(bosses, window):
    bosses.update()
    bosses.draw(window)
    if len(bosses) < 1:
        boss = Boss()
        bosses.add(boss)


def collide1(hero, enemies, group_berry, spheres, menu2):
    if pygame.sprite.spritecollide(hero, enemies, True):
        bite_bee()
        hero.health -= 1
    if pygame.sprite.spritecollide(hero, group_berry, True):
        if hero.health < 3:
            hero.health += 1
            health_hero()
    if pygame.sprite.spritecollide(hero, spheres, True):
        menu2.game_state = "level2"
        teleport()


def collide2(hero, enemies, group_berry, spheres, menu2):
    if pygame.sprite.spritecollide(hero, enemies, True):
        bite_bee()
        hero.health -= 1
    if pygame.sprite.spritecollide(hero, group_berry, True):
        if hero.health < 3:
            hero.health += 1
            health_hero()
    if pygame.sprite.spritecollide(hero, spheres, True):
        menu2.game_state = "level3"
        teleport()


def collide3(hero, bosses):
    if pygame.sprite.spritecollide(hero, bosses, True):
        death()
        hero.health -= 3


def collide0(hero, enemies, group_berry):
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
            if event.type == pygame.QUIT:
                exit()
            pause_text = pygame.font.SysFont('ardecode', 50). \
                render('Пауза! Нажми пробел, чтобы продолжить', True, (255, 255, 255))
            window.blit(pause_text, (250, 400))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False

        pygame.display.update()


def name():
    def save_data():
        text = text_entry.get("1.0", END)

        print("Сохраненный текст:")
        print(text)

    window = Tk()
    window.title("Окно для ввода текста")

    text_entry = Text(window)
    text_entry.pack()

    save_button = Button(window, text="Сохранить", command=save_data)
    save_button.pack()

    window.mainloop()
