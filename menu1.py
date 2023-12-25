# import sys
#
# import pygame
# import button1
# import menu2
#
# pygame.init()
#
# WIDTH, HEIGHT = 1200, 800
# MAX_FPS = 60
#
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.load('Sound/menu.mp3')
# pygame.mixer.music.play(-1)
#
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Pause Menu")
# main_background = pygame.transform.scale(pygame.image.load("Image/Background/menu.jpg").convert_alpha(), (1200, 1200))
#
# menu_state = "main"
# font = pygame.font.SysFont('ardecode', 50)
#
# Text_col = (255, 255, 255)
#
# resume_img = pygame.image.load('Image/Menu/button1.png').convert_alpha()
# options_img = pygame.image.load('Image/Menu/button2.png').convert_alpha()
# quit_img = pygame.image.load('Image/Menu/button3.png').convert_alpha()
# audio_img = pygame.image.load('Image/Menu/button4.png').convert_alpha()
# back_img = pygame.image.load('Image/Menu/button5.png').convert_alpha()
#
# resume_button = button1.Button1(WIDTH / 2 - (252 / 2), 300, resume_img, 1)
# options_button = button1.Button1(WIDTH / 2 - (252 / 2), 400, options_img, 1)
# quit_button = button1.Button1(WIDTH / 2 - (252 / 2), 500, quit_img, 1)
# audio_button = button1.Button1(WIDTH / 2 - (252 / 2), 300, audio_img, 1)
# back_button = button1.Button1(WIDTH / 2 - (252 / 2), 400, back_img, 1)
#
#
# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     window.blit(img, (x, y))
#
#
# run1 = True
# while run1:
#
#     window.fill((0, 0, 0))
#     window.blit(main_background, (0, -300))
#
#     if menu2.game_state == "pause":
#         if menu_state == "main":
#             draw_text("Пауза", font, Text_col, 510, 150)
#             if resume_button.draw(window):
#                 if menu2.game_state == "level1":
#                     menu2.game_state = "level1"
#                 if menu2.game_state == "level2":
#                     menu2.game_state = "level2"
#                 if menu2.game_state == "level3":
#                     menu2.game_state = "level3"
#             if options_button.draw(window):
#                 menu_state = "options"
#             if quit_button.draw(window):
#                 sys.exit()
#
#         if menu_state == "options":
#             if audio_button.draw(window):
#                 pygame.mixer.music.stop()
#             if back_button.draw(window):
#                 menu_state = "main"
#
#     # else:
#     #draw_text("Press SPACE to pause", font, Text_col, WIDTH / 2 - (252 / 2), 250)
#
#     #for event in pygame.event.get():
#         #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             #game_paused = True
#
#         #if event.type == pygame.QUIT:
#             #run1 = False
#
#     pygame.display.update()
#
# pygame.quit()
