import pygame
import button1
import SQL

pygame.init()

WIDTH, HEIGHT = 1200, 800
MAX_FPS = 60

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('Sound/menu.mp3')
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mysterious Forest")
main_background = pygame.transform.scale(pygame.image.load("Image/Background/menu.jpg").convert_alpha(), (1200, 1200))

game_state = "menu"
font = pygame.font.SysFont('ardecode', 50)

Text_col = (255, 255, 255)

start_img = pygame.image.load('Image/Menu/button6.png').convert_alpha()
quit_img = pygame.image.load('Image/Menu/button3.png').convert_alpha()
back_img = pygame.image.load('Image/Menu/button5.png').convert_alpha()
table_img = pygame.image.load('Image/Menu/button9.png').convert_alpha()
end_img = pygame.image.load('Image/Menu/button8.png').convert_alpha()

start_button = button1.Button1(WIDTH / 2 - (252 / 2), 250, start_img, 1)
quit_button = button1.Button1(WIDTH / 2 - (252 / 2), 550, quit_img, 1)
table_button = button1.Button1(WIDTH / 2 - (252 / 2), 450, table_img, 1)
back_button = button1.Button1(WIDTH / 2 - (252 / 2), 650, back_img, 1)
end_button = button1.Button1(WIDTH / 2 - (252 / 2), 350, end_img, 1)


def draw_text1(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


sql = SQL
data = sql.get_data()

begin = True
while begin:
    window.fill((0, 0, 0))
    window.blit(main_background, (0, -300))

    if game_state == "menu":

        if start_button.draw(window):
            game_state = "level1"
            begin = False
        if table_button.draw(window):
            game_state = "records"
        if end_button.draw(window):
            game_state = "level0"
            begin = False
        if quit_button.draw(window):
            begin = False

    if game_state == "records":
        font1 = pygame.font.SysFont('ardecode', 30)
        row_counter = 0
        for row in data:
            row_img = font1.render(str(row[0]) + "       |       " + str(row[1]), True, (255, 255, 255))
            row_rect = row_img.get_rect()
            row_counter += 40
            row_rect.top = 120 + row_counter
            row_rect.centerx = window.get_rect().centerx
            window.blit(row_img, row_rect)
        if back_button.draw(window):
            game_state = "menu"

    draw_text1("Mysterious Forest", font, Text_col, 420, 120)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            begin = False

    pygame.display.update()

pygame.quit()
