import pygame
import events
import menu2
from sound import win
import SQL
class Scores:
    def __init__(self, window):
        self.image_hp = pygame.transform.scale(pygame.image.load('Image/Stats/heart.png').convert_alpha(), (50, 50))
        self.image_hp_boss = pygame.transform.scale(pygame.image.load('Image/Stats/bosshp.png').convert_alpha(),
                                                    (50, 50))
        self.image_friend = pygame.transform.scale(pygame.image.load('Image/Stats/star2.png').convert_alpha(), (50, 50))
        self.window = window
        self.amount_friends = 0
        self.boss_health = 50
        self.game = True

    def show_health(self, hero):
        x = 10
        for hp in range(hero.health):
            self.window.blit(self.image_hp, (x, 20))
            x += 50

    def draw_friends(self):
        print_score = pygame.font.SysFont('ardecode', 90). \
            render(str(self.amount_friends), True, (209, 52, 52))
        self.window.blit(self.image_friend, (950, 20))
        self.window.blit(print_score, (1020, 20))

    def draw_boss(self):
        print_score = pygame.font.SysFont('ardecode', 90). \
            render(str(self.boss_health), True, (209, 52, 52))
        self.window.blit(self.image_hp_boss, (950, 20))
        self.window.blit(print_score, (1020, 20))

    def finish(self, hero, spheres, scores):
        if hero.health < 1 and (menu2.game_state == "level1" or menu2.game_state == "level2"):
            finish_text = pygame.font.SysFont('ardecode', 50). \
                render('Тебя покусали пчелы, приходи в другой раз', True, (255, 255, 255))
            self.window.blit(finish_text, (250, 400))
            self.game = False

        if hero.health < 1 and menu2.game_state == "level0":
            finish_text = pygame.font.SysFont('ardecode', 50). \
                render('Бесконечное путешествие оказалось конечным..', True, (255, 255, 255))
            self.window.blit(finish_text, (250, 400))
            SQL.name(scores)
            SQL.get_data()
            self.game = False
            menu2.game_state = "end"

        if hero.health < 1 and menu2.game_state == "level3":
            finish_text = pygame.font.SysFont('ardecode', 50). \
                render('Одолеть босса оказалось сложнее чем пчел...', True, (255, 255, 255))
            self.window.blit(finish_text, (250, 400))
            self.game = False
            menu2.game_state = "end"

        if scores.boss_health < 1 and menu2.game_state == "level3":
            finish_text = pygame.font.SysFont('ardecode', 50). \
                render('Поздравляем с прохождением игры!', True, (255, 255, 255))
            self.window.blit(finish_text, (300, 250))
            self.game = False
            win()
            menu2.game_state = "end"

        if (menu2.game_state == "level1") and self.amount_friends > 15:
            events.make_sphere(self.window, spheres)

        if (menu2.game_state == "level2") and self.amount_friends > 25:
            events.make_sphere(self.window, spheres)
