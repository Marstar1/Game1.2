import pygame
import background as bg
import events
from hero import Hero
from sound import bg_music
from scores import Scores
from berry import Berry


def run():
    pygame.init()

    pygame.display.set_caption('Mysterious Forest')
    window = pygame.display.set_mode((bg.WIDTH, bg.HEIGHT))
    clock = pygame.time.Clock()
    background = bg.Background()
    hero = Hero(window)
    scores = Scores(window)

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
            scores.finish(hero)
            events.make_friends(friends, window)
            events.make_bee(enemies, window, friends)
            events.move_berry(window, group_berry)
            events.collide(hero, enemies, group_berry)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    run()
