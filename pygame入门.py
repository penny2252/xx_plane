import pygame

# Rect可以不需要初始化直接应用
hero_rect = pygame.Rect(100, 500, 1200, 125)
print('%d%d' % hero_rect.size)
# 要用init进行初始化，最后要用quit退出
pygame.init()
# 创建游戏窗口用display模块
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像，第一步加载图像，第二步用屏幕函数blit调用图像，3、update更新图像显示
bg = pygame.image.load('./feiji/background.png')
screen.blit(bg, (0, 0))
# pygame.display.update()
#绘制飞机


#可以在所有绘制工作完成后，统一更新图线显示
pygame.display.update()

# 游戏循环
n=1
while True:
    n+=1
    if n>500:
        n=0
    bg = pygame.image.load('./feiji/background.png')
    screen.blit(bg, (0, 0))
    hero = pygame.image.load('./feiji/hero.gif')
    screen.blit(hero, (200, (500-n)))
    pygame.display.update()


pygame.quit()
