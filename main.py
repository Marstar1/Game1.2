import pygame
import background as bg
import events
from hero import Hero
from sound import bg_music, bg_music1, bg_boss, end
from scores import Scores
from berry import Berry
import menu2
import time


def run():
    pygame.init()

    if menu2.game_state == "level1":
        pygame.display.set_caption('Mysterious Forest')
        window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
        clock = pygame.time.Clock()
        background = bg.Background1()
        hero = Hero(window)
        scores = Scores(window)
        spheres = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        friends = pygame.sprite.Group()
        group_berry = pygame.sprite.Group()

        pygame.time.set_timer(pygame.USEREVENT, 8000)

        bg_music()

        while True:
            berry = Berry()

            events.event(enemies, scores, group_berry, berry, window)
            if scores.game:
                background.update()
                background.render(window)
                hero.update()
                scores.show_health(hero)
                scores.draw_friends()
                scores.finish(hero, spheres, scores)
                level_text = pygame.font.SysFont('ardecode', 50). \
                    render('Уровень 1', True, (128, 255, 0))
                window.blit(level_text, (500, 150))
                events.make_friends(friends, window)
                events.make_bee1(enemies, window, friends)
                events.move_berry(window, group_berry)
                events.collide1(hero, enemies, group_berry, spheres, menu2)
            pygame.display.update()
            clock.tick(60)
            if menu2.game_state == "level2":
                break

    if menu2.game_state == "level2":

        pygame.display.set_caption('Mysterious Forest')
        window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
        clock = pygame.time.Clock()
        background = bg.Background2()
        hero = Hero(window)
        scores = Scores(window)
        spheres = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        friends = pygame.sprite.Group()
        group_berry = pygame.sprite.Group()

        pygame.time.set_timer(pygame.USEREVENT, 6000)

        bg_music1()

        while True:
            berry = Berry()

            events.event(enemies, scores, group_berry, berry, window)
            if scores.game:
                background.update()
                background.render(window)
                hero.update()
                scores.show_health(hero)
                scores.draw_friends()
                scores.finish(hero, spheres, scores)
                level_text = pygame.font.SysFont('ardecode', 50). \
                    render('Уровень 2', True, (255, 128, 0))
                window.blit(level_text, (500, 150))
                events.make_friends(friends, window)
                events.make_bee2(enemies, window, friends)
                events.move_berry(window, group_berry)
                events.collide2(hero, enemies, group_berry, spheres, menu2)
            pygame.display.update()
            clock.tick(60)
            if menu2.game_state == "level3":
                break

    if menu2.game_state == "level3":

        pygame.display.set_caption('Mysterious Forest')
        window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
        clock = pygame.time.Clock()
        background = bg.Background3()
        hero = Hero(window)
        scores = Scores(window)
        spheres = pygame.sprite.Group()
        bosses = pygame.sprite.Group()
        pygame.time.set_timer(pygame.USEREVENT, 8000)

        bg_boss()

        while True:
            events.eventboss(bosses, scores, window)
            if scores.game:
                background.render(window)
                hero.update()
                bosses.update()
                scores.show_health(hero)
                scores.draw_boss()
                level_text = pygame.font.SysFont('ardecode', 50). \
                    render('!!БОСС!!', True, (204, 0, 0))
                window.blit(level_text, (530, 150))
                scores.finish(hero, spheres, scores)
                events.make_boss(bosses, window)
                events.collide3(hero, bosses)
            pygame.display.update()
            clock.tick(60)
            if menu2.game_state == "end":
                time.sleep(6)
                break

    if menu2.game_state == "level0":
        pygame.display.set_caption('Mysterious Forest')
        window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
        clock = pygame.time.Clock()
        background = bg.Background0()
        hero = Hero(window)
        scores = Scores(window)
        spheres = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        friends = pygame.sprite.Group()
        group_berry = pygame.sprite.Group()

        pygame.time.set_timer(pygame.USEREVENT, 8000)

        end()

        while True:
            berry = Berry()

            events.event(enemies, scores, group_berry, berry, window)
            if scores.game:
                background.update()
                background.render(window)
                hero.update()
                scores.show_health(hero)
                scores.draw_friends()
                scores.finish(hero, spheres, scores)
                level_text = pygame.font.SysFont('ardecode', 50). \
                    render('Бесконечный режим', True, (128, 255, 0))
                window.blit(level_text, (450, 150))
                events.make_friends(friends, window)
                events.make_bee1(enemies, window, friends)
                events.move_berry(window, group_berry)
                events.collide0(hero, enemies, group_berry)
            pygame.display.update()
            clock.tick(60)
            if menu2.game_state == "end":
                time.sleep(6)
                break



if __name__ == '__main__':
    run()
