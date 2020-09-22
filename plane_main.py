import pygame
from 游戏精灵类 import *


class PlaneGame():
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法创建精灵和精灵组
        self.__creat_sprite()

    def __creat_sprite(self):
        pass

    def start_game(self):
        print("游戏开始")
        while True:
            pass


# 主程序编写
# 为了防止引用的文件创建游戏，加个是否在主文件运行的判断
if __name__ == "__main__":
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()