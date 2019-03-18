import pygame
#定义屏幕大小的常量,常量名所有字符大写
SCREEN_RECT=pygame.Rect(0,0,480,700)
#定义刷新帧数的常量
FRAME_PER_SEC=60
class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏精灵'''

    def __init__(self,image_name,speed=1):
        #调用父类初始化方法
        super().__init__()
        #定义对象属性
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed
    def update(self):
        #在屏幕的垂直方向移动
        self.rect.y+=self.speed
class BackGround(GameSprite):
    '''背景精灵'''
    def __init__(self,is_alt=False):
        #调用父类方法实现精灵创建
        super().__init__('./feiji/background.png')
        #判断是否交替图像，需要设置初始位置
        if is_alt:
            self.rect.y=-self.rect.height
    def update(self):
        #调用父类方法
        super().update()
        #判断是否移除屏幕，如果移出，图像到屏幕上方
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height

