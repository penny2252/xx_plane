import pygame
from plane_sprites import *
# Rect可以不需要初始化直接应用
# hero_rect = pygame.Rect(100, 500, 1200, 125)
# print('%d%d' % hero_rect.size)
# 要用init进行初始化，最后要用quit退出
pygame.init()
# 创建游戏窗口用display模块
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像，第一步加载图像，第二步用屏幕函数blit调用图像，3、update更新图像显示
bg = pygame.image.load('./feiji/background.png')
screen.blit(bg, (0, 0))
# pygame.display.update()
#绘制飞机
hero = pygame.image.load('./feiji/hero.gif')
screen.blit(hero, (200, 500))

#可以在所有绘制工作完成后，统一更新图线显示
pygame.display.update()

#创建时钟对象
clock=pygame.time.Clock()

hero_rect=pygame.Rect(200,500,100,124)


#创建敌机的精灵
enemy=GameSprite('./feiji/enemy1.png')
enemy1=GameSprite('./feiji/enemy1.png',2)
#创建敌机的精灵组
enemy_group=pygame.sprite.Group(enemy,enemy1)






# 游戏循环，意味着游戏循环正式开始

while True:
    #设置循环频率，每秒刷新帧数
    clock.tick(60)
    #捕获事件
    # event_list=pygame.event.get()
    # if len(event_list)>0:
    #     print(event_list)
    #当捕获到事件，执行
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()

    hero_rect.y+=-1
    #bottom=y+height
    if hero_rect.bottom<0:
    # if hero_rect.y+hero_rect.height<0:
        hero_rect.y=700
    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)

    #精灵组调用update方法(让组中所有精灵更新位置)
    # draw方法（让组中所有精灵绘制在屏幕）
    enemy_group.update()
    enemy_group.draw(screen)


    pygame.display.update()


pygame.quit()
