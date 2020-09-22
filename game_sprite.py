import random
import pygame

# 设置屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
# 设置刷新帧率常量
FPS = 60
# hero = pygame.image.load("./images/me1.png")
# HERO_LOCATION = (190, 450)
# 创建敌机的定时器常量，
ENEMY_SHOW_EVENTID = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法,super一定要带()
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在平复的垂直方向上下移动
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self):
        # 调用父类方法让背景在垂直方向上下移动
        super().update()
        # 判断是否飞出了屏幕，如果是就重新设置初始位置
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 创建敌机类
class Enemy(GameSprite):
    def __init__(self):
        # 1、调用父类方法，创建敌机精灵
        super().__init__("./images/enemy1.png")
        # 设置随机速度
        self.speed = random.randint(1, 3)
        # 设置随机位置
        # 计算水平方向最大位置的值是屏幕最大宽带减去飞机的宽度
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


# 创建子弹类

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png")
        self.speed = -2
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.top = SCREEN_RECT.bottom - 262

    def update(self):
        super().update()



class Hero(GameSprite):
    def __init__(self):
        # 调用父类方法，加载英雄图片，并设置垂直方向的速度为0
        super().__init__("./images/me1.png", speed=0)
        # 2、设置飞机的水平位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 100
        self.speed2 = 0

    def update(self):
        super().update()
        self.rect.x += self.speed2
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
        if self.rect.y < 0:
            self.rect.y = 0


