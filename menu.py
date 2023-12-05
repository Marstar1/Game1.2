import pygame


class Menu:

    # инициализация меню
    def __init__(self, window):
        self.font = pygame.font.SysFont('ardecode', 50)
        self.window = window
        self.main_background = pygame.transform.scale(pygame.image.load("Image/Background/menu.jpg").convert_alpha(), (1200, 1200))
        # перенести значения и функции из 1, 2 в этот файл