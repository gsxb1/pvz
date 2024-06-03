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

# 检查操作系统的事件
# 如果事件类型是否为QUIT（表示用户点击了窗口的关闭按钮）（pygame.quit()）
# 就关闭pygame，并关闭python解释器（sys.exit()）
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 创建一块白色的画布
    DS.fill((255, 255, 255))

    game.update()
    game.draw()
    pygame.display.update()
