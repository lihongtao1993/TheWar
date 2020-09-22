import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法,super一定要带()
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y == 600:
            self.rect.y = 0
