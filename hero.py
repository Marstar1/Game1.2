import pygame


class Hero:
    def __init__(self, window):
        self.index = 0
        self.move_left = [pygame.transform.scale(pygame.image.load('Image/Hero/f2.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f3.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f4.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f5.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f6.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f7.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f8.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f9.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f10.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f11.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f12.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f13.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f14.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f15.png').convert_alpha(), (250, 300)),
                          pygame.transform.scale(pygame.image.load('Image/Hero/f16.png').convert_alpha(), (250, 300))]

        self.move_right = [pygame.transform.scale(pygame.image.load('Image/Hero/f17.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f18.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f19.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f20.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f21.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f22.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f23.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f24.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f25.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f26.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f27.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f28.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f29.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f30.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f31.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f32.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f33.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f34.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f35.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f36.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f37.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f38.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f39.png').convert_alpha(), (250, 300)),
                           pygame.transform.scale(pygame.image.load('Image/Hero/f40.png').convert_alpha(), (250, 300))]
        self.window = window
        self.image = self.move_right[self.index]
        self.rect = self.image.get_rect(center=(300, 490))
        self.speed = 4
        self.health = 3

    def update(self):
        keys = pygame.key.get_pressed()
        self.image = self.move_right[self.index // 8]
        self.rect.x += self.speed
        self.speed = 0
        if keys[pygame.K_RIGHT]:
            self.image = self.move_right[self.index // 8]
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.image = self.move_left[self.index // 8]
            self.rect.x -= self.speed
        if keys[pygame.K_UP] and self.rect.y > 250.:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed
        if self.index < 80:
            self.index += 1
        else:
            self.index = 0

        self.window.blit(self.image, self.rect)
