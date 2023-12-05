import pygame
from hero import Hero

class Scores():
    def __init__(self, window):
        self.image_hp = pygame.transform.scale(pygame.image.load('Image/Stats/heart.png').convert_alpha(),(50, 50))
        self.image_friend = pygame.transform.scale(pygame.image.load('Image/Stats/star2.png').convert_alpha(),(50, 50))
        self.window = window
        self.amount_friends = 0
        self.game = True


    def show_health(self, hero):
        x = 10
        for hp in range(hero.health):
            self.window.blit(self.image_hp, (x, 20))
            x += 50



    def draw_friends(self):
        print_score = pygame.font.SysFont('ardecode', 90).\
            render(str(self.amount_friends), True, (209, 52,52))
        self.window.blit(self.image_friend,(1050, 20))
        self.window.blit(print_score, (1120, 20))



    def finish(self, hero):
        if hero.health <1:
            finish_text = pygame.font.SysFont('ardecode', 50).\
                render('Тебя покусали пчелы, приходи в другой раз', True, (255, 255, 255))
            self.window.blit(finish_text, (250, 400))
            self.game = False

        elif self.amount_friends > 25:
            finish_text = pygame.font.SysFont('ardecode', 50). \
                render("Поздравляю! Тебе удалось спасти лес от злых пчел!", True, (255, 255, 255))
            self.window.blit(finish_text, (150, 300))
            self.game = False
            finish_text = pygame.font.SysFont('ardecode', 50). \
                render("Ты превратил их в хранителей леса!", True, (255, 255, 255))
            self.window.blit(finish_text, (300, 450))
            self.game = False





