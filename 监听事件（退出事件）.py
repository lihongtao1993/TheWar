import pygame
from 游戏精灵类 import *

pygame.init()
game_screen = pygame.display.set_mode(size=(490, 700))

# 1、加载背景图
background = pygame.image.load("./images/background.png")
# 2、blit绘制背景图
game_screen.blit(background, (0, 0))
# 3、update更新屏幕

hero = pygame.image.load("./images/me1.png")
game_screen.blit(hero, (200, 400))
pygame.display.update()

# 定义一个rect对象记录飞机的初始位置
hero_rect = pygame.Rect(200, 400, 102, 126)

# 创建一个游戏时钟对象
clock = pygame.time.Clock()



# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
enemy2 = GameSprite("./images/enemy1.png", 3)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1, enemy2)

while True:
    clock.tick(60)
    # for循环遍历事件列表,监听关闭事件
    for event in pygame.event.get():
        # 判读事件是不是退出事件
        if event.type == pygame.QUIT:
            print("您已退出游戏")
            # 终止pygame模块
            pygame.quit()
            # 退出系统
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 600
    # 绘制图像
    game_screen.blit(background, (0, 0))
    game_screen.blit(hero, hero_rect)
    # 让精灵组调用两个方法，update()和draw()
    enemy_group.update()
    enemy_group.draw(game_screen)

    pygame.display.update()


