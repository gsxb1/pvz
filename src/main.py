# 入口文件
import pygame
import sys
from pygame.locals import *
from const import *
from game import *

# 初始化pygame
pygame.init()

# 创建一个(1280,600)的窗口对象
DS = pygame.display.set_mode(GAME_SIZE)
# 对Game进行实例化
game = Game(DS)

# 无限循环检查操作系统的事件
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 如果事件类型是否为QUIT（表示用户点击了窗口的关闭按钮）（pygame.quit()）
            pygame.quit()
            sys.exit()
            # 关闭pygame，并关闭python解释器（sys.exit()）
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 如果事件类型为鼠标点击，获取鼠标点击的是左键还是右键
            game.mouseClickHandler(event.button)
    # 创建一块白色的画布
    DS.fill((255, 255, 255))

    game.update()
    game.draw()
    pygame.display.update()
