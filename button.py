import pygame

class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path, sound_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image_path = image_path
        self.sound_path = sound_path
        self.image_path = pygame.image.load('Image/Menu/menu_button.png')
        self.image_path = pygame.transform.scale(self.image_path, (200, 80))
        self.hover_image = self.image_path
        if hover_image_path:
            self.hover_image = pygame.image.load('Image/Menu/menu_button1.png')
            self.hover_image = pygame.transform.scale(self.hover_image, (200, 80))
        self.rect = self.image_path.get_rect(topleft1=(x,y))
        self.sound_path = pygame.mixer.Sound('Sound/button.mp3')
        self.is_hovered = False

    def draw(self, window):
        current_image = self.hover_image if self.is_hovered else self.image_path
        window.blit(current_image, self.rect.topleft)

        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        window.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            #if self.sound_path:
                #self.sound_path.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


