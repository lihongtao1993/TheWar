import pygame
import os
pygame.init()
game_screen = pygame.display.set_mode(size=(480, 600))

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

while True:
    clock.tick(60)
    # 捕获事件列表
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)


    # 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 600
    # 绘制图像
    game_screen.blit(background, (0, 0))
    game_screen.blit(hero, hero_rect)
    pygame.display.update()


