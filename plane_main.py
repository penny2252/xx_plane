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
        # 设置定时器事件——创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        #设置发射子弹事件
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __creat_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.bullet_group=pygame.sprite.Group()

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
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建精灵，添加到精灵组
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type==HERO_FIRE_EVENT:
                self.hero.fire()

            #键盘方向捕获方式1，只有按下才被捕获，然后触发移动
            # elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            #     self.hero.rect.x+=5
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     self.hero.rect.x -= 5
        #使用键盘提供的方式捕获键盘按键的元组,如果按下元组为1,这种方式相当于连续按键
        keys_pressed=pygame.key.get_pressed()
        #判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed=2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed=-2
        else:
            self.hero.speed=0



    def __check_collide(self):
        pass

    def __updat_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
