import pygame
import button1

pygame.init()

WIDTH, HEIGHT = 1200, 800
MAX_FPS = 60

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('Sound/menu.mp3')
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mysterious Forest")
main_background = pygame.transform.scale(pygame.image.load("Image/Background/menu.jpg").convert_alpha(), (1200, 1200))

font = pygame.font.SysFont('ardecode', 50)

Text_col = (255, 255, 255)

start_img = pygame.image.load('Image/Menu/button6.png').convert_alpha()
quit_img = pygame.image.load('Image/Menu/button3.png').convert_alpha()

start_button = button1.Button1(500, 350, start_img, 1)
quit_button = button1.Button1(500, 450, quit_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


begin = True
while begin:

    window.fill((0, 0, 0))
    window.blit(main_background, (0, -300))

    if start_button.draw(window):
        pass

    if quit_button.draw(window):
        begin = False

    draw_text("Mysterious Forest", font, Text_col, 450, 120)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            begin = False

    pygame.display.update()

pygame.quit()
