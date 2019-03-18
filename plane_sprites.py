import random
import pygame

# 定义屏幕大小的常量,常量名所有字符大写
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧数的常量
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#发射子弹事件
HERO_FIRE_EVENT=pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵创建
        super().__init__('./feiji/background.png')
        # 判断是否交替图像，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法
        super().update()
        # 判断是否移除屏幕，如果移出，图像到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__('./feiji/enemy0.png')
        # 敌机随机位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.y = -self.rect.height
        # bottom=y+self.rect.height
        # self.rect.bottom=0
        # 敌机随机速度
        self.speed = random.randint(1, 2)

    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            # kill可以将精灵从精灵组中销毁
            self.kill()

    def __del__(self):
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__('./feiji/hero1.png', 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #创建子弹精灵组
        self.bullets=pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0,1,2):
            #创建子弹精灵
            bullet=Bullet()
            #设置子弹位置
            bullet.rect.bottom=self.rect.y-20*i
            bullet.rect.centerx=self.rect.centerx
            #添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__('./feiji/bullet1.png',-2)
    def update(self):
        super().update()
        if self.rect.bottom<0:
            self.kill()
    def __del__(self):
        pass
