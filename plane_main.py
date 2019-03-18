import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建始终
        self.clock = pygame.time.Clock()
        # 创建私有方法，精灵和精灵组创建
        self.__creat_sprites()

    def __creat_sprites(self):
        # 创建背景精灵
        bg1 = BackGround()
        bg2 = BackGro und(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        print('kaishi')
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵
            self.__updat_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __updat_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏介绍')

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
