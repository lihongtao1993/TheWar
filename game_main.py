import pygame
from game_sprite import *


class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法创建精灵和精灵组
        self.__creat_sprite()
        # 设置定时器事件，创建敌机
        pygame.time.set_timer(ENEMY_SHOW_EVENTID, 1000)

    def __creat_sprite(self):
        bd1 = Background()
        bd2 = Background(True)
        self.back_Group = pygame.sprite.Group(bd1, bd2)
        self.enemy_Group = pygame.sprite.Group()
        # 因为英雄精灵需要在其他方法中使用，所以需要把英雄的精灵也定义成属性
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("游戏开始")
        while True:
            # 1、设置刷新帧率
            self.clock.tick(FPS)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新绘制精灵
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 判断按下按键事件
            # elif event.type == pygame.KEYDOWN:
            elif event.type == ENEMY_SHOW_EVENTID:
                print("敌机来了……")
                enemy = Enemy()
                self.enemy_Group.add(enemy)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed2 = 1
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed2 = -1
        elif key_pressed[pygame.K_UP]:
            self.hero.speed = -2
        elif key_pressed[pygame.K_DOWN]:
            self.hero.speed = 2
        else:
            self.hero.speed2 = 0
            self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_Group.update()
        self.back_Group.draw(self.screen)
        self.enemy_Group.update()
        self.enemy_Group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)


    # game_over方法不需要使用类属性或者对象属性，可以定义成静态方法
    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


# 主程序编写
# 为了防止引用的文件创建游戏，加个是否在主文件运行的判断
if __name__ == "__main__":
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()